export default async function handler(req, res) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method Not Allowed' });
  }

  try {
    const data = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    const contact = String(data.contact || '').trim().slice(0, 100);
    const project = String(data.project || '').trim().slice(0, 2000);
    const calcSummary = String(data.calc_summary || '').trim().slice(0, 150);

    if (!contact && !project) {
      return res.status(400).json({ success: false, error: 'Contact or project required' });
    }

    const leadEntry = {
      id: Date.now(),
      contact,
      project,
      calc_summary: calcSummary,
      created_at: new Date().toISOString().replace('T', ' ').slice(0, 19),
      status: 'new'
    };

    // Forward to Telegram if configured via Vercel Environment Variables
    const botToken = process.env.TELEGRAM_BOT_TOKEN;
    const chatId = process.env.TELEGRAM_CHAT_ID;

    if (botToken && chatId) {
      try {
        const text = `🚀 *НОВАЯ ЗАЯВКА С САЙТА DEVDUO!*\n\n👤 *Контакт:* \`${contact}\`\n📝 *Задача:* ${project}\n💰 *Расчет:* ${calcSummary}\n⏰ *Время:* ${leadEntry.created_at}`;
        await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: chatId,
            text,
            parse_mode: 'Markdown'
          })
        });
      } catch (tgErr) {
        console.error('Telegram notification error:', tgErr);
      }
    }

    return res.status(200).json({ success: true, id: leadEntry.id });
  } catch (err) {
    return res.status(500).json({ success: false, error: 'Internal server error' });
  }
}
