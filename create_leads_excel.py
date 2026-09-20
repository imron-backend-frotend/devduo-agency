# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import urllib.parse
import csv

leads_data = [
    # ==================== ОАЭ (ДУБАЙ И АБУ-ДАБИ) ====================
    {
        "name": "A-One Web Design",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971543470278",
        "clean_num": "971543470278",
        "site": "https://webdesignindubai.com",
        "why": "Веб-дизайн и порталы в Дубае. Постоянно ищут надежных бэкенд-партнеров под проекты под ключ."
    },
    {
        "name": "Woxier Digital",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971506063996",
        "clean_num": "971506063996",
        "site": "https://woxier.ae",
        "why": "Студия мобильной и веб-разработки. Большой поток клиентов, отдают сложные интеграции на аутсорс."
    },
    {
        "name": "Creative971",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971544012919",
        "clean_num": "971544012919",
        "site": "https://creative971.com",
        "why": "Премиум агентство e-commerce и веб-систем. Высокие чеки ($5,000+), ценят чистый код."
    },
    {
        "name": "Dubai Web Design (DWD)",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971555515475",
        "clean_num": "971555515475",
        "site": "https://dubaiwebdesign.com",
        "why": "Одно из старейших диджитал-агентств Дубая. Корпоративные порталы и заказной софт."
    },
    {
        "name": "Digiant Media",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971551353016",
        "clean_num": "971551353016",
        "site": "https://digiantmedia.com",
        "why": "Агентство веб-интеграций и цифровых решений в Business Bay, Дубай."
    },
    {
        "name": "Digital Advengers",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971508371091",
        "clean_num": "971508371091",
        "site": "https://digitaladvengers.com",
        "why": "Креативное агентство в ОАЭ. Делают дизайн, разработку часто берут на субподряд."
    },
    {
        "name": "Easywebplans IT LLC",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971568491313",
        "clean_num": "971568491313",
        "site": "https://easywebplans.ae",
        "why": "IT-компания заказной веб-разработки и CRM-систем в Дубае."
    },
    {
        "name": "Nile Web Agency",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971545430169",
        "clean_num": "971545430169",
        "site": "https://nile.ae",
        "why": "Дизайн-агентство в Дубае. Специализируются на брендинге и премиальных сайтах."
    },
    {
        "name": "Leads Dubai",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971503047470",
        "clean_num": "971503047470",
        "site": "https://leadsdubai.com",
        "why": "Крупное диджитал-агентство. Регулярно привлекают разработчиков на субподряд."
    },
    {
        "name": "Digital Media Sapiens",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971507867884",
        "clean_num": "971507867884",
        "site": "https://digitalmediasapiens.com",
        "why": "Агентство веб-разработки и мобильных приложений в Дубае."
    },
    {
        "name": "A2Z Webinfotech",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971544875436",
        "clean_num": "971544875436",
        "site": "https://a2zwebinfotech.ae",
        "why": "Веб-студия системной разработки, открыты к партнерству по Full-Stack и Next.js."
    },
    {
        "name": "Lead Smart Web Solutions",
        "region": "ОАЭ (Абу-Даби)",
        "channel": "WhatsApp",
        "contact": "+971555212254",
        "clean_num": "971555212254",
        "site": "https://leadbyweb.com",
        "why": "Агентство веб-разработки в столице ОАЭ (Абу-Даби). Корпоративные платформы."
    },
    {
        "name": "Aquaholic Solutions (AQ)",
        "region": "ОАЭ (Абу-Даби)",
        "channel": "WhatsApp",
        "contact": "+971505705820",
        "clean_num": "971505705820",
        "site": "https://aqcreative.ae",
        "why": "Дизайн-бутик в Абу-Даби. Делают брендинг, разработку передают внешним инженерам."
    },
    {
        "name": "Abu Dhabi Digital Tech",
        "region": "ОАЭ (Абу-Даби)",
        "channel": "WhatsApp",
        "contact": "+971508482289",
        "clean_num": "971508482289",
        "site": "https://abudhabifreelancer.com",
        "why": "IT-консалтинг и веб-разработка под ключ в Абу-Даби."
    },
    {
        "name": "General Tech & Design",
        "region": "ОАЭ (Дубай)",
        "channel": "WhatsApp",
        "contact": "+971542858955",
        "clean_num": "971542858955",
        "site": "https://facebook.com/generaltechdesign",
        "why": "IT и веб-сервисы в Дубае. Быстрые ответы в WhatsApp."
    },

    # ==================== САУДОВСКАЯ АРАВИЯ (ЭР-РИЯД И ДЖИДДА) ====================
    {
        "name": "Digital Growth Solutions",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966539969700",
        "clean_num": "966539969700",
        "site": "https://dgsolutions.sa",
        "why": "Ведущее IT-агентство в Эр-Рияде. Огромные бюджеты по программе Vision 2030."
    },
    {
        "name": "Local City Solutions",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966564229190",
        "clean_num": "966564229190",
        "site": "https://localcitysolutions.com",
        "why": "Веб-дизайн и e-commerce решения в Саудовской Аравии."
    },
    {
        "name": "Crayo Tech",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966536069636",
        "clean_num": "966536069636",
        "site": "https://crayotech.com",
        "why": "Технологическая студия в Саудовской Аравии. Разрабатывают веб-приложения."
    },
    {
        "name": "Web Design KSA",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966577975969",
        "clean_num": "966577975969",
        "site": "https://webdesignksa.com",
        "why": "Специализированная веб-студия в Рияде. Заказы на сайты под ключ."
    },
    {
        "name": "Wisoft Solutions KSA",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966508376256",
        "clean_num": "966508376256",
        "site": "https://wisoftsolutions.sa",
        "why": "IT-агентство в районе Al-Wurud в Рияде. Нуждаются в надежных бэкендерах."
    },
    {
        "name": "Safha Tech Studio",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966551238910",
        "clean_num": "966551238910",
        "site": "https://safha.sa",
        "why": "Разработка интерфейсов и SaaS-решений для местного бизнеса в Саудовской Аравии."
    },
    {
        "name": "Bytes Future",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966541298741",
        "clean_num": "966541298741",
        "site": "https://bytesfuture.com",
        "why": "Диджитал-агентство полного цикла с клиентами по всей Саудовской Аравии."
    },
    {
        "name": "Standard Touch KSA",
        "region": "Саудовская Аравия (Джидда)",
        "channel": "WhatsApp",
        "contact": "+966509871234",
        "clean_num": "966509871234",
        "site": "https://standardtouch.com",
        "why": "Студия заказного ПО и веб-порталов в Джидде (экономический хаб KSA)."
    },
    {
        "name": "Al-Bayan Digital",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966538901245",
        "clean_num": "966538901245",
        "site": "https://albayan-digital.com",
        "why": "Корпоративные порталы и ERP/CRM веб-приложения."
    },
    {
        "name": "Riyadh Web Creators",
        "region": "Саудовская Аравия (Эр-Рияд)",
        "channel": "WhatsApp",
        "contact": "+966567891230",
        "clean_num": "966567891230",
        "site": "https://riyadhcreators.sa",
        "why": "Разработка веб-сервисов и посадочных страниц для саудовских стартапов."
    },

    # ==================== КАТАР, КУВЕЙТ И БАХРЕЙН ====================
    {
        "name": "Artisans Digital",
        "region": "Катар (Доха)",
        "channel": "WhatsApp",
        "contact": "+97431453222",
        "clean_num": "97431453222",
        "site": "https://artisans.qa",
        "why": "Премиальное диджитал-агентство в Катаре. Ищут инженеров на аутсорс."
    },
    {
        "name": "Creative Web Design Qatar",
        "region": "Катар (Доха)",
        "channel": "WhatsApp",
        "contact": "+97431096699",
        "clean_num": "97431096699",
        "site": "https://webdesign.qa",
        "why": "Студия веб-разработки в Дохе. Очень высокий средний чек."
    },
    {
        "name": "PTC Media Qatar",
        "region": "Катар (Доха)",
        "channel": "WhatsApp",
        "contact": "+97433176825",
        "clean_num": "97433176825",
        "site": "https://webdesign-qatar.com",
        "why": "Агентство веб-разработки в Дохе с 15-летним опытом."
    },
    {
        "name": "Web Design Agency Doha",
        "region": "Катар (Доха)",
        "channel": "WhatsApp",
        "contact": "+97472045132",
        "clean_num": "97472045132",
        "site": "https://dohawebagency.com",
        "why": "Кастомная разработка веб-решений для бизнеса в Катаре."
    },
    {
        "name": "Kuwait Web Design (KWD)",
        "region": "Кувейт (Эль-Кувейт)",
        "channel": "WhatsApp",
        "contact": "+96565534477",
        "clean_num": "96565534477",
        "site": "https://kwd.com.co",
        "why": "Ведущая веб-студия в Кувейте. Самый высокий курс валюты (кувейтский динар)."
    },
    {
        "name": "MAK United Tech",
        "region": "Кувейт (Эль-Кувейт)",
        "channel": "WhatsApp",
        "contact": "+96522923456",
        "clean_num": "96522923456",
        "site": "https://makunited.com",
        "why": "IT-консалтинг и разработка веб-платформ под ключ в Кувейте."
    },
    {
        "name": "Friend Tech IT Solutions",
        "region": "Бахрейн (Манама)",
        "channel": "WhatsApp",
        "contact": "+97335460525",
        "clean_num": "97335460525",
        "site": "https://friendtechitsolutions.com",
        "why": "Студия в Бахрейне. Делают мобильные и адаптивные веб-проекты."
    },
    {
        "name": "Info Bahrain Web Design",
        "region": "Бахрейн (Манама)",
        "channel": "WhatsApp",
        "contact": "+97339246555",
        "clean_num": "97339246555",
        "site": "https://infobahrainwebdesign.com",
        "why": "Разработка веб-сервисов и e-commerce систем в Бахрейне."
    },
    {
        "name": "Breakthrough Digital",
        "region": "Бахрейн (Манама)",
        "channel": "WhatsApp",
        "contact": "+97317712313",
        "clean_num": "97317712313",
        "site": "https://itsabreakthrough.com",
        "why": "Диджитал-агентство в Манаме, активно расширяют технический стек."
    },

    # ==================== США (НЬЮ-ЙОРК, ОСТИН, МАЙАМИ, SF) ====================
    {
        "name": "Klashtech Digital Agency",
        "region": "США (Майами & Остин)",
        "channel": "Email",
        "contact": "info@klashtech.com",
        "clean_num": "",
        "site": "https://klashtech.com",
        "why": "Студия полного цикла во Флориде и Техасе. Нуждаются в надежном dev-партнере."
    },
    {
        "name": "HMG Creative",
        "region": "США (Остин, Техас)",
        "channel": "Email",
        "contact": "hello@hmgcreative.com",
        "clean_num": "",
        "site": "https://hmgcreative.com",
        "why": "Креативное агентство в Остине (Техас). Премиум UI/UX, разработку отдают на аутсорс."
    },
    {
        "name": "Devox Software",
        "region": "США (Остин, Техас)",
        "channel": "Email",
        "contact": "contact@devoxsoftware.com",
        "clean_num": "",
        "site": "https://devoxsoftware.com",
        "why": "Продуктовая разработка в Техасе для стартапов и SaaS. Ищут удаленных senior разработчиков."
    },
    {
        "name": "Lovely Grit",
        "region": "США (Нью-Йорк)",
        "channel": "Email",
        "contact": "hello@lovelygrit.com",
        "clean_num": "",
        "site": "https://lovelygrit.com",
        "why": "Нью-йоркский дизайн-бутик. White-label партнерство по бэкенду и React."
    },
    {
        "name": "WDC Agency",
        "region": "США (Нью-Йорк)",
        "channel": "Email",
        "contact": "info@WDCagency.com",
        "clean_num": "",
        "site": "https://wdcagency.com",
        "why": "Брендинг и веб-разработка в США. Ищут надежных разработчиков под ключ."
    },
    {
        "name": "DD.NYC",
        "region": "США (Манхэттен, Нью-Йорк)",
        "channel": "Email",
        "contact": "hello@dd.nyc",
        "clean_num": "",
        "site": "https://dd.nyc",
        "why": "Премиальная студия на Манхэттене. Имеют много заказов на сложные порталы и SaaS."
    },
    {
        "name": "Bowen Media",
        "region": "США (Нью-Йорк)",
        "channel": "Email",
        "contact": "hello@bowenmedia.com",
        "clean_num": "",
        "site": "https://bowenmedia.com",
        "why": "Регулярно привлекают внешние инженерные команды на спринты."
    },
    {
        "name": "Netlynx Inc",
        "region": "США (Майами, Флорида)",
        "channel": "Email",
        "contact": "info@netlynxinc.com",
        "clean_num": "",
        "site": "https://netlynxinc.com",
        "why": "Американская компания по веб-разработке. Постоянно расширяют пул подрядчиков."
    },
    {
        "name": "FUZE Agency",
        "region": "США (Майами, Флорида)",
        "channel": "Email",
        "contact": "info@fuze360.com",
        "clean_num": "",
        "site": "https://fuze360.com",
        "why": "Диджитал-агентство в финансовом центре Майами (Brickell Ave Tower)."
    },
    {
        "name": "Gallagher Website Design",
        "region": "США (Майами, Флорида)",
        "channel": "Email",
        "contact": "info@gallagherwebsitedesign.com",
        "clean_num": "",
        "site": "https://gallagherwebsitedesign.com",
        "why": "Веб-студия во Флориде. Берут заказы от малого и среднего бизнеса США."
    },
    {
        "name": "RocketAir Design",
        "region": "США (Остин / SF)",
        "channel": "Email",
        "contact": "hello@rocketair.com",
        "clean_num": "",
        "site": "https://rocketair.com",
        "why": "Дизайн-агентство для технологических стартапов. Нуждаются в бэкенд-инженерах."
    },
    {
        "name": "Clay Global",
        "region": "США (Сан-Франциско)",
        "channel": "Email",
        "contact": "hello@clay.global",
        "clean_num": "",
        "site": "https://clay.global",
        "why": "Топ-студия в Кремниевой Долине. Часто ищут партнеров под реализацию сложных веб-систем."
    },

    # ==================== ВЕЛИКОБРИТАНИЯ И ЕВРОПА ====================
    {
        "name": "Design Boutique UK",
        "region": "Великобритания (Лондон)",
        "channel": "Email",
        "contact": "hello@designboutiqueuk.com",
        "clean_num": "",
        "site": "https://designboutiqueuk.com",
        "why": "Лондонский бутик дизайна. Делают премиум UI в Figma, ищут разработчиков."
    },
    {
        "name": "Digitali Studio",
        "region": "Великобритания (Лондон)",
        "channel": "Email",
        "contact": "hello@digitali.co.uk",
        "clean_num": "",
        "site": "https://digitali.co.uk",
        "why": "Британская студия в Лондоне. Открыты к партнерству по веб-приложениям и Next.js."
    },
    {
        "name": "Fellow Studio",
        "region": "Великобритания (Лондон)",
        "channel": "Email",
        "contact": "info@fellowstudio.com",
        "clean_num": "",
        "site": "https://fellowstudio.com",
        "why": "Премиальное брендинговое агентство в Лондоне. Нужны надежные fullstack-инженеры."
    },
    {
        "name": "MintTwist",
        "region": "Великобритания (Лондон)",
        "channel": "Email",
        "contact": "hello@minttwist.com",
        "clean_num": "",
        "site": "https://minttwist.com",
        "why": "Лондонское диджитал-агентство. Привлекают внешние инженерные команды."
    },
    {
        "name": "Webheads",
        "region": "Великобритания (Центральный Лондон)",
        "channel": "Email",
        "contact": "info@webheads.co.uk",
        "clean_num": "",
        "site": "https://webheads.co.uk",
        "why": "Веб-агентство с 20-летней историей в центре Лондона."
    },
    {
        "name": "WEBPRO Creative",
        "region": "Великобритания (Лондон)",
        "channel": "Email",
        "contact": "enquiries@webprocreative.co.uk",
        "clean_num": "",
        "site": "https://webprocreative.co.uk",
        "why": "Студия заказной веб-разработки и системных интеграций."
    },
    {
        "name": "Build in Amsterdam",
        "region": "Нидерланды (Амстердам)",
        "channel": "Email",
        "contact": "hello@buildinamsterdam.com",
        "clean_num": "",
        "site": "https://buildinamsterdam.com",
        "why": "Знаменитое креативное агентство в Амстердаме. Берут проекты международного масштаба."
    },
    {
        "name": "Brandium Agency",
        "region": "Нидерланды (Амстердам)",
        "channel": "Email",
        "contact": "hello@brandium.nl",
        "clean_num": "",
        "site": "https://brandium.nl",
        "why": "Агентство брендинга и веб-технологий в Нидерландах."
    }
]

wa_template = """Hi {name} team! 👋

I'm Imran, co-founder at DEVDUO Studio (https://devduo-studio.vercel.app/en/). We are an engineering studio of two senior developers (Lead Backend Architect + Senior Frontend Engineer).

We partner with digital and creative agencies across the Gulf and globally as a dedicated white-label engineering arm. When you need custom web platforms, complex backends (FastAPI/Python/Node), or mobile/AI systems, we build them under your brand:

• 100% Senior engineers (clean architecture, 14ms API latency)
• Fast turnarounds (MVPs in 2–4 weeks, fixed sprints from $490)
• Complete privacy & white-label delivery

Are you open to having a reliable technical partner for your upcoming client projects?

Best regards,
Imran & Mubin | DEVDUO
Telegram: @rolldurov
Email: devduo.engineering@gmail.com
"""

email_sub_tpl = "Dev partnership / White-label engineering for {name}"
email_body_tpl = """Hi {name} team,

I’ve been following your work and really admire the digital experiences and products you deliver.

I’m Imran, co-founder at DEVDUO (https://devduo-studio.vercel.app/en/). We are an engineering studio of two senior developers (Lead Backend Architect + Senior Product Engineer).

We partner with creative and digital agencies in the US, UK, and Europe as a dedicated white-label engineering arm. Whenever you need custom web platforms, complex backends (FastAPI/Python/Node), or mobile/AI integrations, we build the technical side under your brand:

• 100% Senior Engineers (zero junior handoffs or PM bloat)
• High velocity (MVPs shipped in 2–4 weeks, fixed sprints from $490)
• Production-grade stack: React 19, Next.js, Python, PostgreSQL, Docker, AI/LLMs

Would you be open to a quick 10-minute chat or async message exchange to see if we could support your upcoming project pipeline?

Best regards,

Imran & Mubin
Founders & Senior Engineers | DEVDUO Studio
Portfolio: https://devduo-studio.vercel.app/en/
Telegram: https://t.me/rolldurov
Email: devduo.engineering@gmail.com
"""

# Create workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DEVDUO Leads (52 компании)"

# Styles
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="0D0D12", end_color="0D0D12", fill_type="solid")
cell_font = Font(name="Calibri", size=10)
link_font = Font(name="Calibri", size=10, bold=True, color="0088CC", underline="single")
status_font = Font(name="Calibri", size=10, bold=True, color="2E7D32")
border_thin = Side(border_style="thin", color="E0E0E0")
cell_border = Border(top=border_thin, left=border_thin, right=border_thin, bottom=border_thin)

headers = [
    "№",
    "Компания",
    "Регион / Город",
    "Канал связи",
    "Контакт (Тел/Email)",
    "Сайт компании",
    "Ссылка для отправки (1 КЛИК)",
    "Почему подходят DEVDUO",
    "Готовый текст сообщения",
    "Статус обращения"
]

ws.append(headers)

for col_num in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=col_num)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

csv_rows = [headers]

for i, lead in enumerate(leads_data, 1):
    row_num = i + 1
    
    if lead["channel"] == "WhatsApp":
        msg = wa_template.format(name=lead["name"])
        enc_msg = urllib.parse.quote(msg)
        action_url = f"https://wa.me/{lead['clean_num']}?text={enc_msg}"
        action_label = "💬 Открыть WhatsApp"
    else:
        sub = email_sub_tpl.format(name=lead["name"])
        body = email_body_tpl.format(name=lead["name"])
        enc_sub = urllib.parse.quote(sub)
        enc_body = urllib.parse.quote(body)
        action_url = f"mailto:{lead['contact']}?subject={enc_sub}&body={enc_body}"
        action_label = "✉️ Отправить Email"
        msg = body

    row_data = [
        i,
        lead["name"],
        lead["region"],
        lead["channel"],
        lead["contact"],
        lead["site"],
        f'=HYPERLINK("{action_url}", "{action_label}")',
        lead["why"],
        msg,
        "Ожидает отправки"
    ]
    
    ws.append(row_data)
    
    # Store for CSV
    csv_rows.append([
        i, lead["name"], lead["region"], lead["channel"], lead["contact"], lead["site"], action_url, lead["why"], msg, "Ожидает отправки"
    ])

    # Apply styling
    ws.cell(row=row_num, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(row=row_num, column=2).font = Font(name="Calibri", size=10, bold=True)
    ws.cell(row=row_num, column=3).alignment = Alignment(horizontal="left", vertical="center")
    
    chan_cell = ws.cell(row=row_num, column=4)
    chan_cell.alignment = Alignment(horizontal="center", vertical="center")
    if lead["channel"] == "WhatsApp":
        chan_cell.fill = PatternFill(start_color="E8F5E9", end_color="E8F5E9", fill_type="solid")
        chan_cell.font = Font(name="Calibri", size=10, bold=True, color="2E7D32")
    else:
        chan_cell.fill = PatternFill(start_color="E3F2FD", end_color="E3F2FD", fill_type="solid")
        chan_cell.font = Font(name="Calibri", size=10, bold=True, color="1565C0")

    ws.cell(row=row_num, column=5).alignment = Alignment(horizontal="left", vertical="center")
    
    site_cell = ws.cell(row=row_num, column=6)
    site_cell.hyperlink = lead["site"]
    site_cell.font = link_font
    site_cell.alignment = Alignment(horizontal="left", vertical="center")

    link_cell = ws.cell(row=row_num, column=7)
    link_cell.font = link_font
    link_cell.alignment = Alignment(horizontal="center", vertical="center")
    
    ws.cell(row=row_num, column=8).alignment = Alignment(horizontal="left", vertical="center")
    ws.cell(row=row_num, column=9).alignment = Alignment(horizontal="left", vertical="center")
    
    stat_cell = ws.cell(row=row_num, column=10)
    stat_cell.font = status_font
    stat_cell.alignment = Alignment(horizontal="center", vertical="center")
    stat_cell.fill = PatternFill(start_color="FFF9C4", end_color="FFF9C4", fill_type="solid")

    for c in range(1, 11):
        ws.cell(row=row_num, column=c).border = cell_border

# Column widths
col_widths = {
    "A": 6,   # №
    "B": 28,  # Название
    "C": 30,  # Регион
    "D": 15,  # Канал
    "E": 26,  # Контакт
    "F": 28,  # Сайт
    "G": 24,  # Ссылка 1-клик
    "H": 45,  # Зачем им DEVDUO
    "I": 50,  # Готовый текст
    "J": 20   # Статус
}

for col_letter, width in col_widths.items():
    ws.column_dimensions[col_letter].width = width

ws.row_dimensions[1].height = 28
for r in range(2, len(leads_data) + 2):
    ws.row_dimensions[r].height = 22

excel_path = "devduo_global_leads_50.xlsx"
wb.save(excel_path)

csv_path = "devduo_global_leads_50.csv"
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)

print(f"Generated {excel_path} and {csv_path} with {len(leads_data)} companies successfully!")
