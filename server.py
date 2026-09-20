"""
DevDuo Studio - Hardened Production-Ready Server with Security Safeguards
Includes:
- Blocked access to sensitive files (config.json, leads.json, server.py, *.bat)
- Request body size limits (Anti-DoS)
- IP-based rate limiting on lead submissions
- Input sanitization & field length constraints
- Security headers (X-Frame-Options, X-Content-Type-Options, etc.)
- Protected /api/leads endpoint
"""
import http.server
import socketserver
import json
import os
import sys
import time
from datetime import datetime
import urllib.request
import urllib.parse
import html

# Force UTF-8 on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 3000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADS_FILE = os.path.join(BASE_DIR, 'leads.json')
CONFIG_FILE = os.path.join(BASE_DIR, 'config.json')

MAX_PAYLOAD_SIZE = 32 * 1024  # 32 KB maximum POST payload
RATE_LIMIT_WINDOW = 60        # 60 seconds
MAX_REQUESTS_PER_WINDOW = 5   # Max 5 lead submissions per minute per IP

# IP Request Tracker for Rate Limiting
ip_request_history = {}

# Forbidden extensions and sensitive files that CANNOT be served statically
FORBIDDEN_FILES = {
    'config.json',
    'leads.json',
    'server.py',
    'start_server.bat',
    '.env',
    '.gitignore'
}
FORBIDDEN_EXTENSIONS = {'.py', '.json', '.bat', '.cmd', '.env', '.sh', '.log'}

# Initialize leads.json if not exists
if not os.path.exists(LEADS_FILE):
    with open(LEADS_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=2)

# Initialize config.json
if not os.path.exists(CONFIG_FILE):
    default_config = {
        "telegram_bot_token": "",
        "telegram_chat_id": "",
        "admin_secret_key": "devduo2026"
    }
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=2)

def get_admin_secret():
    """Fetches admin secret key from config"""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
                return cfg.get("admin_secret_key", "devduo2026")
    except Exception:
        pass
    return "devduo2026"

def is_rate_limited(client_ip):
    """Check if client IP exceeded rate limit"""
    now = time.time()
    history = ip_request_history.get(client_ip, [])
    # Filter only requests within the window
    history = [t for t in history if now - t < RATE_LIMIT_WINDOW]
    if len(history) >= MAX_REQUESTS_PER_WINDOW:
        return True
    history.append(now)
    ip_request_history[client_ip] = history
    return False

def send_telegram_notification(lead_data):
    """Safely forwards lead to Telegram bot if configured"""
    try:
        if not os.path.exists(CONFIG_FILE):
            return
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        
        token = cfg.get("telegram_bot_token", "").strip()
        chat_id = cfg.get("telegram_chat_id", "").strip()

        if not token or not chat_id:
            return

        # Sanitize markdown special characters for Telegram Markdown format
        contact_clean = lead_data.get('contact', 'Не указан').replace('*', '').replace('_', '')
        project_clean = lead_data.get('project', 'Не указана').replace('*', '').replace('_', '')
        calc_clean = lead_data.get('calc_summary', '—').replace('*', '').replace('_', '')

        text = (
            f"🚀 *НОВАЯ ЗАЯВКА С САЙТА DEVDUO!*\n\n"
            f"👤 *Контакт:* `{contact_clean}`\n"
            f"📝 *Задача:* {project_clean}\n"
            f"💰 *Расчет:* {calc_clean}\n"
            f"⏰ *Время:* {lead_data.get('created_at', '')}\n"
        )

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = json.dumps({
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }).encode('utf-8')

        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            pass
    except Exception as e:
        print(f"[!] Telegram notification error: {e}")

class SecureDevDuoHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        """Inject Security Headers into all responses"""
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        self.send_header('Permissions-Policy', 'geolocation=(), camera=(), microphone=()')
        super().end_headers()

    def do_POST(self):
        # 1. Check endpoint
        if self.path != '/api/lead':
            self.send_error(404, "Endpoint not found")
            return

        client_ip = self.client_address[0]

        # 2. Rate Limiting Check
        if is_rate_limited(client_ip):
            self.send_response(429)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            err_resp = json.dumps({
                "success": False,
                "error": "Слишком много запросов. Пожалуйста, подождите минуту перед следующей отправкой."
            }, ensure_ascii=False)
            self.wfile.write(err_resp.encode('utf-8'))
            return

        # 3. Payload Size Limitation (Anti-DoS)
        try:
            content_length = int(self.headers.get('Content-Length', 0))
        except (ValueError, TypeError):
            content_length = 0

        if content_length <= 0:
            self.send_error(400, "Empty payload")
            return

        if content_length > MAX_PAYLOAD_SIZE:
            self.send_error(413, "Payload Too Large (Maximum 32 KB allowed)")
            return

        # 4. Safe Read and Parse
        try:
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
        except Exception:
            self.send_error(400, "Malformed JSON")
            return

        # 5. Strict Input Sanitization & Field Length Limits
        contact = str(data.get('contact', '')).strip()[:100]
        project = str(data.get('project', '')).strip()[:2000]
        calc_summary = str(data.get('calc_summary', '')).strip()[:150]

        if not contact and not project:
            self.send_error(400, "Contact or project details required")
            return

        # Escape HTML entities for secure storage
        safe_contact = html.escape(contact)
        safe_project = html.escape(project)
        safe_calc = html.escape(calc_summary)
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        lead_entry = {
            "id": int(datetime.now().timestamp()),
            "contact": safe_contact,
            "project": safe_project,
            "calc_summary": safe_calc,
            "created_at": created_at,
            "status": "new"
        }

        # 6. Safe Save to leads.json
        try:
            leads = []
            if os.path.exists(LEADS_FILE):
                with open(LEADS_FILE, 'r', encoding='utf-8') as f:
                    leads = json.load(f)
            # Limit stored leads to last 500 to prevent disk exhaustion
            leads.insert(0, lead_entry)
            leads = leads[:500]
            with open(LEADS_FILE, 'w', encoding='utf-8') as f:
                json.dump(leads, f, ensure_ascii=False, indent=2)
            print(f"[+] Securely stored lead from: {safe_contact} [IP: {client_ip}]")
        except Exception as e:
            print(f"[!] Storage error: {e}")

        # 7. Telegram Notification
        send_telegram_notification(lead_entry)

        # 8. Success Response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        resp = json.dumps({"success": True, "id": lead_entry["id"]}, ensure_ascii=False)
        self.wfile.write(resp.encode('utf-8'))

    def do_GET(self):
        clean_path = urllib.parse.urlparse(self.path).path
        filename = os.path.basename(clean_path).lower()
        _, ext = os.path.splitext(clean_path.lower())

        # 1. SECURITY FILTER: Block access to sensitive files
        if filename in FORBIDDEN_FILES or ext in FORBIDDEN_EXTENSIONS:
            # Check if this is the leads API endpoint
            if clean_path != '/api/leads':
                self.send_error(403, "Access Denied: Sensitive file is protected")
                return

        # 2. Leads API (Protected with admin key check)
        if clean_path == '/api/leads':
            # Check Admin Authentication Header or query param
            query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            admin_key = self.headers.get('X-Admin-Key', '') or query_params.get('key', [''])[0]
            expected_key = get_admin_secret()

            # Verify authorization (allow if correct key or if request comes from local loopback)
            client_ip = self.client_address[0]
            is_local = client_ip in ('127.0.0.1', '::1', 'localhost')

            if not is_local and admin_key != expected_key:
                self.send_error(401, "Unauthorized: Valid admin key required")
                return

            leads = []
            if os.path.exists(LEADS_FILE):
                try:
                    with open(LEADS_FILE, 'r', encoding='utf-8') as f:
                        leads = json.load(f)
                except Exception:
                    leads = []

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            resp = json.dumps({"leads": leads}, ensure_ascii=False)
            self.wfile.write(resp.encode('utf-8'))
            return

        # Standard static file serving for safe files (html, css, js, images)
        super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SecureDevDuoHandler) as httpd:
        print(f"[+] DEVDUO Secure Server running on http://localhost:{PORT}")
        print(f"[+] Protected: config.json, leads.json, server.py, *.bat")
        print(f"[+] Security: Rate-limiting, XSS filtering, DoS size limit enabled")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
