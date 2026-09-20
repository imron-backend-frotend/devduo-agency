# -*- coding: utf-8 -*-
import urllib.parse

companies = [
    {
        "country": "USA (New York)",
        "name": "Lovely Grit",
        "type": "Boutique Web & Creative Studio",
        "email": "hello@lovelygrit.com",
        "site": "https://lovelygrit.com",
        "target_note": "Дизайн-бутик в Нью-Йорке. Делают красивый брендинг, часто ищут бэкенд-партнеров на аутсорс."
    },
    {
        "country": "USA (New York)",
        "name": "WDC Agency",
        "type": "Digital Web & Branding Agency",
        "email": "info@WDCagency.com",
        "site": "https://wdcagency.com",
        "target_note": "Агентство веб-дизайна в США. Идеально предложить white-label разработку под их ключ."
    },
    {
        "country": "USA (New York)",
        "name": "DD.NYC",
        "type": "Award-winning UI/UX & Web Studio",
        "email": "hello@dd.nyc",
        "site": "https://dd.nyc/contact/",
        "target_note": "Топ-студия в Манхэттене. Имеют много заказов на сложные порталы и SaaS, отдают разработку на субподряд."
    },
    {
        "country": "USA (New York)",
        "name": "Bowen Media",
        "type": "Digital Creative & Web Agency",
        "email": "hello@bowenmedia.com",
        "site": "https://bowenmedia.com/contact/",
        "target_note": "Креативное агентство полного цикла. Регулярно нанимают удаленные команды инженеров под спринты."
    },
    {
        "country": "USA",
        "name": "Netlynx Inc",
        "type": "Web & App Solutions",
        "email": "info@netlynxinc.com",
        "site": "https://netlynxinc.com",
        "target_note": "Американская компания по веб-разработке. Постоянно расширяют пул технических подрядчиков."
    },
    {
        "country": "UK (London)",
        "name": "Design Boutique UK",
        "type": "Boutique Creative & Web Agency",
        "email": "hello@designboutiqueuk.com",
        "site": "https://designboutiqueuk.com",
        "target_note": "Лондонский бутик дизайна. Делают премиум UI в Figma, ищут разработчиков для верстки и бэкенда."
    },
    {
        "country": "UK (London)",
        "name": "Digitali",
        "type": "Digital Design & Web Studio",
        "email": "hello@digitali.co.uk",
        "site": "https://digitali.co.uk",
        "target_note": "Британская студия в Лондоне. Открыты к партнерству по веб-приложениям и Next.js проектам."
    },
    {
        "country": "UK (London)",
        "name": "Fellow Studio",
        "type": "Branding & Digital Experience",
        "email": "info@fellowstudio.com",
        "site": "https://fellowstudio.com",
        "target_note": "Премиальное брендинговое агентство в Лондоне. Им нужны надежные full-stack инженеры."
    },
    {
        "country": "UK (London)",
        "name": "MintTwist",
        "type": "Digital Agency London",
        "email": "hello@minttwist.com",
        "site": "https://minttwist.com",
        "target_note": "Известное агентство в Лондоне. Часто привлекают внешние инженерные команды на сложные проекты."
    },
    {
        "country": "UK (London)",
        "name": "Webheads",
        "type": "Web Design & Development Agency",
        "email": "info@webheads.co.uk",
        "site": "https://webheads.co.uk",
        "target_note": "Лондонское агентство с 20-летней историей. Регулярно ищут сильных бэкендеров и fullstack-разработчиков."
    }
]

# Subject line tailored for high open rates in US/UK
subject = "Dev partnership / White-label engineering for {name}"

# Pitch template
body_template = """Hi {name} team,

I’ve been following your work and really admire the digital experiences and designs you deliver.

I’m Imran, co-founder at DEVDUO (https://imron-backend-frotend.github.io/devduo-agency/en/). We are an engineering studio of two senior developers (Lead Backend Architect + Senior Product Engineer).

We partner with creative and design-first agencies in the US and UK as a dedicated white-label engineering arm. Whenever you need custom web platforms, complex backends (FastAPI/Python/Node), or mobile/AI integrations, we build the technical side under your brand:

• 100% Senior Engineers (zero junior handoffs or PM bloat)
• High velocity (MVPs shipped in 2–4 weeks, fixed sprints from $490)
• Production-grade stack: React 19, Next.js, Python, PostgreSQL, Docker, AI/LLMs

Would you be open to a quick 10-minute chat or async message exchange to see if we could support your upcoming project pipeline?

Best regards,

Imran & Mubin
Founders & Senior Engineers | DEVDUO Studio
Portfolio: https://imron-backend-frotend.github.io/devduo-agency/en/
Telegram: https://t.me/rolldurov
Email: devduo.engineering@gmail.com
"""

out_lines = []
out_lines.append("=" * 80)
out_lines.append("DEVDUO — US & UK AGENCY OUTREACH LIST (10 TARGET COMPANIES)")
out_lines.append("English Website: https://imron-backend-frotend.github.io/devduo-agency/en/")
out_lines.append("Direct Telegram: https://t.me/rolldurov")
out_lines.append("=" * 80 + "\n")

for i, comp in enumerate(companies, 1):
    comp_subject = subject.format(name=comp["name"])
    comp_body = body_template.format(name=comp["name"])
    
    # Generate clickable mailto link
    encoded_subject = urllib.parse.quote(comp_subject)
    encoded_body = urllib.parse.quote(comp_body)
    mailto_link = f"mailto:{comp['email']}?subject={encoded_subject}&body={encoded_body}"
    
    out_lines.append(f"[{i}] {comp['name']} — {comp['country']}")
    out_lines.append(f"    Type: {comp['type']}")
    out_lines.append(f"    Website: {comp['site']}")
    out_lines.append(f"    Direct Email: {comp['email']}")
    out_lines.append(f"    Почему подходит: {comp['target_note']}")
    out_lines.append(f"    CLICK-TO-SEND MAIL LINK: {mailto_link}")
    out_lines.append("-" * 80 + "\n")

with open("usa_uk_leads.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Created usa_uk_leads.txt successfully!")
