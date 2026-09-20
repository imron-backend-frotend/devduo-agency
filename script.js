// DevDuo Studio - Interactive Logic

document.addEventListener('DOMContentLoaded', () => {
  initNavbarAnimations();
  initTerminal();
  initCalculator();
  initCustomSelects();
  initFAQ();
  initModal();
  initCardTilt();
  initCopyButtons();
  initLeadsViewer();
  initHeroParallax();
  initProposalModal();
  initLiveTelegramWidget();
  initCsvExport();
});

// 1. Interactive Terminal & Code Simulator
function initTerminal() {
  const codeFiles = {
    'server.ts': `// Microservice API Gateway & Auth
import { FastifyInstance } from 'fastify';
import { DuoEngine } from '@devduo/core';

export async function bootstrap(app: FastifyInstance) {
  const engine = new DuoEngine({
    clustering: true,
    edgeReplication: true,
    maxThroughputRps: 150_000
  });

  app.post('/api/v1/ship-product', async (req, reply) => {
    const { spec, targetDeadline } = req.body;
    const project = await engine.deployArchitecture({
      founders: ['Imran', 'Mubin'],
      qualityGrade: 'A+',
      zeroLegacyGuarantee: true
    });
    return reply.status(200).send({ status: 'live', url: project.edgeUrl });
  });
}`,
    'ai_agent.py': `# Autonomous High-Load Neural Agent
import asyncio
from devduo.neural import AutonomousModel, VectorStream

class DuoProductionAgent:
    def __init__(self):
        self.brain = AutonomousModel(model="gemini-flash-high")
        self.stream = VectorStream(latency_target_ms=12)

    async def execute_task(self, prompt: str) -> dict:
        print("[⚡] Ingesting enterprise knowledge base...")
        embedding = await self.stream.embed(prompt)
        response = await self.brain.synthesize(embedding)
        return {"result": response, "latency_ms": 9.4, "confidence": 0.998}

if __name__ == "__main__":
    agent = DuoProductionAgent()
    asyncio.run(agent.execute_task("Analyze cloud telemetry"))`,
    'docker-compose.yml': `version: '3.9'
services:
  app-gateway:
    image: devduo/gateway:v2.4
    ports:
      - "443:443"
    environment:
      - NODE_ENV=production
      - REDIS_CLUSTER=enabled
      - METRICS_PORT=9090
    deploy:
      replicas: 4
      restart_policy:
        condition: on-failure
  database:
    image: postgres:16-alpine
    shm_size: 1g
    volumes:
      - pgdata:/var/lib/postgresql/data`
  };

  const codeDisplay = document.getElementById('code-display');
  const fileTabs = document.querySelectorAll('.file-tab');
  const runBtn = document.getElementById('run-code-btn');
  const terminalLogs = document.getElementById('terminal-logs');

  if (fileTabs && codeDisplay) {
    fileTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        fileTabs.forEach(t => t.classList.remove('active-tab', 'text-white', 'border-b-2', 'border-white'));
        fileTabs.forEach(t => t.classList.add('text-zinc-400'));
        tab.classList.add('active-tab', 'text-white', 'border-b-2', 'border-white');
        tab.classList.remove('text-zinc-400');
        
        const fileName = tab.dataset.file;
        if (codeFiles[fileName]) {
          codeDisplay.textContent = codeFiles[fileName];
        }
      });
    });
  }

  if (runBtn && terminalLogs) {
    runBtn.addEventListener('click', () => {
      runBtn.disabled = true;
      runBtn.innerHTML = `<span class="inline-block animate-spin mr-1">↻</span> Компиляция...`;
      
      terminalLogs.innerHTML = `<div class="text-zinc-500 font-mono text-xs">==> Инициализация CI/CD конвейера DevDuo...</div>`;

      const steps = [
        { text: "✔ Анализ статического типа: 0 ошибок, 0 ворнингов", delay: 300, color: "text-emerald-400" },
        { text: "✔ Запуск 142 модульных тестов: 100% покрытия пройдено", delay: 700, color: "text-emerald-400" },
        { text: "✔ Оптимизация Vite бандла: 34.2 KB (gzip) сгенерировано", delay: 1100, color: "text-sky-400" },
        { text: "✔ Подключение к защищенному Edge кластеру (Latency 14ms)", delay: 1500, color: "text-zinc-300" },
        { text: "🚀 Успешный релиз: Продукт развернут в продакшене!", delay: 1900, color: "text-white font-bold bg-emerald-500/20 px-2 py-1 rounded inline-block" }
      ];

      steps.forEach(step => {
        setTimeout(() => {
          const line = document.createElement('div');
          line.className = `font-mono text-xs mt-1 ${step.color}`;
          line.textContent = step.text;
          terminalLogs.appendChild(line);
          terminalLogs.scrollTop = terminalLogs.scrollHeight;
        }, step.delay);
      });

      setTimeout(() => {
        runBtn.disabled = false;
        runBtn.innerHTML = `<span>▶</span> Выполнить пайплайн`;
      }, 2300);
    });
  }
}

// 2. Interactive Cost & Timeline Calculator
function initCalculator() {
  const projectType = document.getElementById('calc-type');
  const projectScope = document.getElementById('calc-scope');
  const projectUrgency = document.getElementById('calc-urgency');
  const priceDisplay = document.getElementById('calc-price');
  const timeDisplay = document.getElementById('calc-time');

  if (!projectType || !priceDisplay) return;

  function calculate() {
    let basePrice = parseInt(projectType.value, 10);
    let scopeMult = parseFloat(projectScope.value);
    let urgencyMult = parseFloat(projectUrgency.value);
    const isEn = document.documentElement.lang === 'en';

    let total = Math.round(basePrice * scopeMult * urgencyMult);
    let weeks = 2;

    if (basePrice >= 70000 || basePrice === 1250) weeks = 4;
    else if (basePrice >= 50000 || basePrice === 950) weeks = 3;
    else if (basePrice >= 35000 || basePrice === 490) weeks = 2;
    else if (basePrice < 35000 || basePrice === 390) weeks = 1;
    else weeks = 2;

    if (scopeMult > 1.2) weeks += 1;
    if (urgencyMult > 1.1) weeks = Math.max(1, Math.round(weeks * 0.7));

    if (isEn) {
      priceDisplay.textContent = `from $${total.toLocaleString('en-US')}`;
      timeDisplay.textContent = `Timeline: ${weeks}–${weeks + 1} wks`;
    } else {
      priceDisplay.textContent = `от ${total.toLocaleString('ru-RU')} ₽`;
      timeDisplay.textContent = `Срок: ${weeks}–${weeks + 1} нед.`;
    }
  }

  projectType.addEventListener('change', calculate);
  projectScope.addEventListener('change', calculate);
  projectUrgency.addEventListener('change', calculate);

  calculate();
}

// Custom Glassmorphic Select Dropdowns
function initCustomSelects() {
  const wrappers = document.querySelectorAll('.custom-select-wrapper');

  function closeAllDropdowns() {
    document.querySelectorAll('.custom-select-dropdown').forEach(dropdown => {
      dropdown.classList.add('hidden');
    });
    document.querySelectorAll('.chevron-icon').forEach(chevron => {
      chevron.style.transform = 'rotate(0deg)';
    });
  }

  wrappers.forEach(wrapper => {
    const btn = wrapper.querySelector('.custom-select-btn');
    const dropdown = wrapper.querySelector('.custom-select-dropdown');
    const chevron = wrapper.querySelector('.chevron-icon');
    const selectedText = wrapper.querySelector('.selected-text');
    const targetInput = wrapper.querySelector('input[type="hidden"]');
    const options = wrapper.querySelectorAll('.custom-option');

    if (!btn || !dropdown) return;

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isClosed = dropdown.classList.contains('hidden');
      closeAllDropdowns();
      if (isClosed) {
        dropdown.classList.remove('hidden');
        if (chevron) chevron.style.transform = 'rotate(180deg)';
      }
    });

    options.forEach(opt => {
      opt.addEventListener('click', (e) => {
        e.stopPropagation();
        const value = opt.dataset.value;
        const label = opt.dataset.label;
        const icon = opt.dataset.icon;
        const iconColor = opt.dataset.iconColor || 'text-white';

        // Update hidden input and trigger calculation
        if (targetInput) {
          targetInput.value = value;
          targetInput.dispatchEvent(new Event('change'));
        }

        // Update button text & icon
        if (selectedText) {
          selectedText.innerHTML = `<i data-lucide="${icon}" class="w-3.5 h-3.5 ${iconColor}"></i><span>${label}</span>`;
          if (window.lucide) window.lucide.createIcons();
        }

        // Update active class & checkmarks
        options.forEach(o => {
          o.classList.remove('selected', 'text-white');
          o.classList.add('text-zinc-300');
          const check = o.querySelector('.check-icon');
          if (check) check.classList.add('hidden');
        });
        opt.classList.add('selected', 'text-white');
        opt.classList.remove('text-zinc-300');
        const activeCheck = opt.querySelector('.check-icon');
        if (activeCheck) activeCheck.classList.remove('hidden');

        closeAllDropdowns();
      });
    });
  });

  document.addEventListener('click', () => {
    closeAllDropdowns();
  });
}

// 3. FAQ Accordion
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const button = item.querySelector('.faq-button');
    const answer = item.querySelector('.faq-answer');
    const icon = item.querySelector('.faq-icon');

    if (button && answer) {
      button.addEventListener('click', () => {
        const isOpen = !answer.classList.contains('hidden');
        
        // Close others
        document.querySelectorAll('.faq-answer').forEach(a => a.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach(i => i.style.transform = 'rotate(0deg)');

        if (!isOpen) {
          answer.classList.remove('hidden');
          if (icon) icon.style.transform = 'rotate(45deg)';
        }
      });
    }
  });
}

// 4. Modal for Direct Telegram / Booking
function initModal() {
  const modal = document.getElementById('contact-modal');
  const openButtons = document.querySelectorAll('.open-contact-modal');
  const closeBtn = document.getElementById('close-modal-btn');
  const modalForm = document.getElementById('modal-contact-form');

  if (!modal) return;

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    });
  });

  const closeModal = () => {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  };

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  if (modalForm) {
    modalForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const contactInput = document.getElementById('modal-contact-input').value;
      const projectInput = document.getElementById('modal-project-input').value;
      const calcPrice = document.getElementById('calc-price')?.textContent || '';
      const calcTime = document.getElementById('calc-time')?.textContent || '';

      const submitBtn = modalForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = `<span>Отправка заявки...</span>`;
      }

      try {
        await fetch('/api/lead', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contact: contactInput,
            project: projectInput,
            calc_summary: `${calcPrice} (${calcTime})`
          })
        });

        showToast('⚡ Заявка принята и сохранена! Мы свяжемся с вами в течение 15 минут.');
        if (typeof updateLeadsBadge === 'function') updateLeadsBadge();
      } catch (err) {
        showToast('⚡ Заявка принята!');
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = `<span>Отправить заявку</span><i data-lucide="arrow-right" class="w-4 h-4"></i>`;
          if (window.lucide) window.lucide.createIcons();
        }
        closeModal();
        modalForm.reset();
      }
    });
  }
}

// 5. 3D Card Tilt Effect
function initCardTilt() {
  const tiltCards = document.querySelectorAll('.tilt-card');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -5;
      const rotateY = ((x - centerX) / centerX) * 5;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
    });
  });
}

// 6. Copy Links & Toast
function initCopyButtons() {
  const copyButtons = document.querySelectorAll('.copy-trigger');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.dataset.copyText || '@rolldurov';
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast(`Скопировано в буфер: ${textToCopy}`);
      });
    });
  });
}

function showToast(message) {
  let toast = document.getElementById('global-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'global-toast';
    toast.className = 'fixed bottom-6 right-6 z-50 px-5 py-3 rounded-xl bg-zinc-900/95 border border-white/20 text-white font-medium shadow-2xl flex items-center gap-3 backdrop-blur-md transition-all duration-300 transform translate-y-12 opacity-0';
    document.body.appendChild(toast);
  }
  
  toast.innerHTML = `<span class="text-emerald-400 text-lg">✔</span> ${message}`;
  toast.classList.remove('translate-y-12', 'opacity-0');
  toast.classList.add('translate-y-0', 'opacity-100');

  setTimeout(() => {
    toast.classList.remove('translate-y-0', 'opacity-100');
    toast.classList.add('translate-y-12', 'opacity-0');
  }, 3500);
}

// 7. Advanced Navbar Animations (Floating Island, Magnetic Indicator, Scroll Progress)
function initNavbarAnimations() {
  const header = document.getElementById('navbar-header');
  const progressBar = document.getElementById('scroll-progress-bar');
  const navMenu = document.getElementById('nav-menu');
  const indicator = document.getElementById('nav-indicator');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');

  // Scroll handler: Floating Island + Progress Bar + Scrollspy
  function handleScroll() {
    const scrollY = window.scrollY || window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;

    // A. Floating Capsule Transition
    if (header) {
      if (scrollY > 35) {
        header.classList.add('nav-scrolled');
      } else {
        header.classList.remove('nav-scrolled');
      }
    }

    // B. Progress Bar
    if (progressBar && docHeight > 0) {
      const scrollPercent = Math.min(100, Math.max(0, (scrollY / docHeight) * 100));
      progressBar.style.width = scrollPercent + '%';
    }

    // C. Scrollspy
    let currentSectionId = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 140;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href === `#${currentSectionId}`) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // Magnetic Sliding Capsule Hover Effect
  if (navMenu && indicator) {
    navLinks.forEach(link => {
      link.addEventListener('mouseenter', () => {
        const left = link.offsetLeft;
        const top = link.offsetTop;
        const width = link.offsetWidth;
        const height = link.offsetHeight;

        indicator.style.left = left + 'px';
        indicator.style.top = top + 'px';
        indicator.style.width = width + 'px';
        indicator.style.height = height + 'px';
        indicator.style.opacity = '1';
      });
    });

    navMenu.addEventListener('mouseleave', () => {
      indicator.style.opacity = '0';
    });
  }
}

// 8. Leads Viewer & Local Admin Panel
async function fetchLeads() {
  try {
    let adminKey = localStorage.getItem('devduo_admin_key') || '';
    const headers = {};
    if (adminKey) {
      headers['X-Admin-Key'] = adminKey;
    }
    let res = await fetch('/api/leads', { headers });
    if (res.status === 401) {
      adminKey = prompt('Введите секретный ключ администратора для доступа к заявкам:');
      if (adminKey) {
        localStorage.setItem('devduo_admin_key', adminKey);
        res = await fetch('/api/leads', { headers: { 'X-Admin-Key': adminKey } });
      } else {
        return [];
      }
    }
    if (!res.ok) return [];
    const data = await res.json();
    return data.leads || [];
  } catch (err) {
    return [];
  }
}

async function updateLeadsBadge() {
  const badge = document.getElementById('leads-count-badge');
  const leads = await fetchLeads();
  if (badge) {
    badge.textContent = leads.length;
  }
}

async function renderLeadsList() {
  const container = document.getElementById('leads-list');
  if (!container) return;
  container.innerHTML = '<div class="text-center py-6 text-zinc-500 font-mono text-xs">Загрузка заявок...</div>';
  
  const leads = await fetchLeads();
  updateLeadsBadge();

  if (leads.length === 0) {
    container.innerHTML = `
      <div class="text-center py-10 text-zinc-500 font-mono text-xs">
        <i data-lucide="inbox" class="w-8 h-8 mx-auto mb-2 opacity-40"></i>
        Пока нет входящих заявок. Отправьте тестовую заявку через форму!
      </div>
    `;
    if (window.lucide) window.lucide.createIcons();
    return;
  }

  container.innerHTML = leads.map(l => {
    let cleanContact = (l.contact || 'Не указан').replace(/</g, "&lt;").replace(/>/g, "&gt;");
    let isTg = cleanContact.startsWith('@');
    let tgLink = isTg ? `https://t.me/${cleanContact.replace('@', '')}` : '';
    let projectText = (l.project || '').replace(/</g, "&lt;").replace(/>/g, "&gt;");
    let calcText = (l.calc_summary || '').replace(/</g, "&lt;").replace(/>/g, "&gt;");

    return `
      <div class="p-4 rounded-2xl bg-black/60 border border-white/10 hover:border-white/20 transition-all flex flex-col gap-2.5">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 font-mono text-xs font-bold border border-emerald-500/20">
              ${cleanContact}
            </span>
            ${tgLink ? `<a href="${tgLink}" target="_blank" rel="noopener noreferrer" class="text-sky-400 hover:underline text-xs font-mono flex items-center gap-1"><i data-lucide="send" class="w-3 h-3"></i> Чат в Telegram</a>` : ''}
          </div>
          <span class="text-[11px] font-mono text-zinc-500">${l.created_at || ''}</span>
        </div>
        <p class="text-xs text-zinc-300 leading-relaxed font-sans bg-white/[0.02] p-2.5 rounded-xl border border-white/5">
          ${projectText ? projectText : '<span class="text-zinc-500 italic">Описание задачи не заполнено</span>'}
        </p>
        ${calcText ? `<div class="text-[11px] font-mono text-zinc-400 flex items-center gap-1.5"><i data-lucide="calculator" class="w-3 h-3 text-sky-400"></i> Расчет: <span class="text-white font-semibold">${calcText}</span></div>` : ''}
      </div>
    `;
  }).join('');

  if (window.lucide) window.lucide.createIcons();
}

function initLeadsViewer() {
  const openBtn = document.getElementById('open-leads-btn');
  const closeBtn = document.getElementById('close-leads-btn');
  const refreshBtn = document.getElementById('refresh-leads-btn');
  const modal = document.getElementById('leads-modal');

  updateLeadsBadge();

  if (openBtn && modal) {
    openBtn.addEventListener('click', () => {
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      renderLeadsList();
    });
  }

  const closeLeads = () => {
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
  };

  if (closeBtn) closeBtn.addEventListener('click', closeLeads);
  if (refreshBtn) refreshBtn.addEventListener('click', renderLeadsList);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeLeads();
    });
  }
}

// 9. 3D Hero Mouse Parallax Physics
function initHeroParallax() {
  const container = document.getElementById('hero-visual-container');
  const laptop = document.getElementById('hero-laptop-wrap');
  const star1 = document.getElementById('hero-star-1');
  const star2 = document.getElementById('hero-star-2');

  if (!container || !laptop) return;
  if (window.matchMedia('(pointer: coarse)').matches) return;

  let mouseX = 0;
  let mouseY = 0;
  let currentX = 0;
  let currentY = 0;
  let isHovered = false;

  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    if (e.clientY < window.innerHeight * 1.2) {
      mouseX = (e.clientX - centerX) / (window.innerWidth / 2);
      mouseY = (e.clientY - centerY) / (window.innerHeight / 2);
      isHovered = true;
    } else {
      isHovered = false;
    }
  });

  window.addEventListener('mouseleave', () => {
    isHovered = false;
  });

  function animate() {
    if (!isHovered) {
      mouseX = 0;
      mouseY = 0;
    }

    currentX += (mouseX - currentX) * 0.08;
    currentY += (mouseY - currentY) * 0.08;

    const rotY = currentX * 14;
    const rotX = -currentY * 14;

    laptop.style.transform = `perspective(1000px) rotateY(${rotY.toFixed(2)}deg) rotateX(${rotX.toFixed(2)}deg) translateZ(10px)`;

    if (star1) {
      star1.style.transform = `translate(${(currentX * -20).toFixed(2)}px, ${(currentY * -20).toFixed(2)}px) rotate(${(currentX * 15).toFixed(2)}deg)`;
    }
    if (star2) {
      star2.style.transform = `translate(${(currentX * 18).toFixed(2)}px, ${(currentY * 18).toFixed(2)}px)`;
    }

    requestAnimationFrame(animate);
  }

  animate();
}

// 10. Commercial Proposal / PDF Estimate Generator
function initProposalModal() {
  const openButtons = document.querySelectorAll('.open-proposal-btn, #download-pdf-btn');
  const modal = document.getElementById('proposal-modal');
  const closeBtn = document.getElementById('close-proposal-btn');
  const printBtn = document.getElementById('print-proposal-btn');

  if (!modal) return;

  const openProposal = () => {
    const typeOption = document.querySelector('[data-target="calc-type"] .custom-option.selected');
    const scopeOption = document.querySelector('[data-target="calc-scope"] .custom-option.selected');
    const urgencyOption = document.querySelector('[data-target="calc-urgency"] .custom-option.selected');
    
    const priceElem = document.getElementById('calc-price');
    const timeElem = document.getElementById('calc-time');

    const productType = typeOption ? typeOption.dataset.label : 'MVP Веб-сервис (SaaS)';
    const scopeText = scopeOption ? scopeOption.dataset.label : 'С готовым ТЗ / дизайном';
    const urgencyText = urgencyOption ? urgencyOption.dataset.label : 'Обычный темп';
    const priceText = priceElem ? priceElem.textContent : 'от 39 000 ₽';
    const timeText = timeElem ? timeElem.textContent : '1–2 недели';

    const now = new Date();
    const dateFormatted = now.toLocaleDateString('ru-RU', { day: '2-digit', month: '2-digit', year: 'numeric' });
    const randomId = Math.floor(1000 + Math.random() * 9000);

    const docTypeElem = document.getElementById('proposal-product-type');
    const docScopeElem = document.getElementById('proposal-scope-text');
    const docUrgencyElem = document.getElementById('proposal-urgency-text');
    const docPriceElem = document.getElementById('proposal-price');
    const docTimeElem = document.getElementById('proposal-time');
    const docDateElem = document.getElementById('proposal-date');
    const docMetaElem = document.getElementById('proposal-meta-id');

    if (docTypeElem) docTypeElem.textContent = productType;
    if (docScopeElem) docScopeElem.textContent = scopeText;
    if (docUrgencyElem) docUrgencyElem.textContent = urgencyText;
    if (docPriceElem) docPriceElem.textContent = priceText;
    if (docTimeElem) docTimeElem.textContent = `Срок реализации: ${timeText}`;
    if (docDateElem) docDateElem.textContent = dateFormatted;
    if (docMetaElem) docMetaElem.textContent = `DEVDUO-KP-${now.getFullYear()}-${randomId}`;

    const livePopup = document.getElementById('live-chat-popup');
    if (livePopup) livePopup.classList.add('hidden');

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    if (window.lucide) window.lucide.createIcons();
  };

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openProposal();
    });
  });

  const closeModal = () => {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  };

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      printSinglePageProposal();
    });
  }

  // Highlight calculator when jumped to via #calculator anchor
  const calcNavLinks = document.querySelectorAll('a[href="#calculator"]');
  calcNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      const calcBox = document.getElementById('calculator');
      if (calcBox) {
        calcBox.classList.add('ring-4', 'ring-sky-400', 'ring-offset-4', 'ring-offset-black');
        setTimeout(() => {
          calcBox.classList.remove('ring-4', 'ring-sky-400', 'ring-offset-4', 'ring-offset-black');
        }, 2200);
      }
    });
  });
}

// Dedicated 1-Page Clean Proposal Printer (Zero blank pages)
function printSinglePageProposal() {
  const typeOption = document.querySelector('[data-target="calc-type"] .custom-option.selected');
  const scopeOption = document.querySelector('[data-target="calc-scope"] .custom-option.selected');
  const urgencyOption = document.querySelector('[data-target="calc-urgency"] .custom-option.selected');
  
  const priceElem = document.getElementById('calc-price');
  const timeElem = document.getElementById('calc-time');

  const productType = typeOption ? typeOption.dataset.label : 'MVP Веб-сервис (SaaS)';
  const scopeText = scopeOption ? scopeOption.dataset.label : 'С готовым ТЗ / дизайном';
  const urgencyText = urgencyOption ? urgencyOption.dataset.label : 'Обычный темп';
  const priceText = priceElem ? priceElem.textContent : 'от 39 000 ₽';
  const timeText = timeElem ? timeElem.textContent : '1–2 недели';

  const dateElem = document.getElementById('proposal-date');
  const metaElem = document.getElementById('proposal-meta-id');
  const proposalDate = dateElem ? dateElem.textContent : new Date().toLocaleDateString('ru-RU');
  const proposalId = metaElem ? metaElem.textContent : 'DEVDUO-KP-2026';

  let printFrame = document.getElementById('devduo-isolated-print-frame');
  if (printFrame) {
    printFrame.remove();
  }

  printFrame = document.createElement('iframe');
  printFrame.id = 'devduo-isolated-print-frame';
  printFrame.style.position = 'fixed';
  printFrame.style.right = '0';
  printFrame.style.bottom = '0';
  printFrame.style.width = '0';
  printFrame.style.height = '0';
  printFrame.style.border = 'none';
  printFrame.style.visibility = 'hidden';
  document.body.appendChild(printFrame);

  try {
    const frameDoc = printFrame.contentWindow.document;
    frameDoc.open();
    frameDoc.write(`<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Коммерческое предложение ${proposalId}</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 14mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    html, body {
      background: #ffffff;
      color: #0f172a;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 11.5px;
      line-height: 1.45;
      height: auto;
    }
    .page-container {
      border: 2px solid #0f172a;
      border-radius: 12px;
      padding: 22px 26px;
      background: #ffffff;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 14px;
      border-bottom: 2px solid #0f172a;
      margin-bottom: 16px;
    }
    .brand-title {
      font-size: 22px;
      font-weight: 900;
      letter-spacing: 0.5px;
      color: #0f172a;
    }
    .brand-sub {
      font-size: 11px;
      color: #64748b;
      font-family: monospace;
      margin-top: 2px;
    }
    .meta-right {
      text-align: right;
      font-family: monospace;
      font-size: 11px;
      color: #475569;
    }
    .meta-right strong {
      color: #0f172a;
    }
    .summary-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 18px;
    }
    .card {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 12px 14px;
    }
    .card-label {
      font-family: monospace;
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #64748b;
      margin-bottom: 4px;
    }
    .card-title {
      font-size: 14px;
      font-weight: 700;
      color: #0f172a;
    }
    .card-sub {
      font-size: 11px;
      color: #475569;
      margin-top: 2px;
    }
    .price-big {
      font-size: 24px;
      font-weight: 900;
      font-family: monospace;
      color: #0284c7;
    }
    .time-badge {
      font-size: 11px;
      font-weight: 700;
      color: #059669;
      font-family: monospace;
      margin-top: 3px;
    }
    .section-title {
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #0f172a;
      margin-bottom: 10px;
      font-family: monospace;
    }
    .sprints-list {
      display: flex;
      flex-direction: column;
      gap: 7px;
      margin-bottom: 18px;
    }
    .sprint-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 8px 12px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
    }
    .sprint-num {
      font-weight: 800;
      font-family: monospace;
      color: #0284c7;
      font-size: 12px;
    }
    .sprint-text strong {
      color: #0f172a;
    }
    .footer-note {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 12px;
      border-top: 1px solid #cbd5e1;
      font-size: 11px;
      color: #64748b;
      font-family: monospace;
    }
  </style>
</head>
<body>
  <div class="page-container">
    <div class="header">
      <div>
        <div class="brand-title">DEVDUO <span style="color:#0284c7;">D²</span></div>
        <div class="brand-sub">Инженерная студия двух Senior-разработчиков</div>
      </div>
      <div class="meta-right">
        <div>КП: <strong>${proposalId}</strong></div>
        <div>Дата: <strong>${proposalDate}</strong></div>
        <div>Статус: <strong style="color:#059669;">Актуально</strong></div>
      </div>
    </div>

    <div class="summary-grid">
      <div class="card">
        <div class="card-label">Параметры разработки</div>
        <div class="card-title">${productType}</div>
        <div class="card-sub">Объем: ${scopeText}</div>
        <div class="card-sub">Темп: ${urgencyText}</div>
      </div>
      <div class="card">
        <div class="card-label">Ориентировочный бюджет</div>
        <div class="price-big">${priceText}</div>
        <div class="time-badge">Срок реализации: ${timeText}</div>
      </div>
    </div>

    <div class="section-title">План работ и состав спринтов:</div>
    <div class="sprints-list">
      <div class="sprint-item">
        <span class="sprint-num">01.</span>
        <div class="sprint-text"><strong>Архитектура & Data Modeling:</strong> проектирование схемы БД (PostgreSQL/Redis), API-контрактов и безопасной структуры сервиса.</div>
      </div>
      <div class="sprint-item">
        <span class="sprint-num">02.</span>
        <div class="sprint-text"><strong>Fullstack-разработка:</strong> быстрая сборка современного интерфейса (Next.js/React) и надежного бэкенда (FastAPI/Node.js).</div>
      </div>
      <div class="sprint-item">
        <span class="sprint-num">03.</span>
        <div class="sprint-text"><strong>Интеграции & Платежи:</strong> подключение Telegram-ботов, платежных шлюзов, внешних CRM или OpenAI API.</div>
      </div>
      <div class="sprint-item">
        <span class="sprint-num">04.</span>
        <div class="sprint-text"><strong>DevOps & Безопасность:</strong> контейнеризация Docker, настройка CI/CD, защита от DoS, XSS и шифрование данных.</div>
      </div>
      <div class="sprint-item">
        <span class="sprint-num">05.</span>
        <div class="sprint-text"><strong>Гарантия качества:</strong> 14 дней бесплатной гарантийной поддержки и исправления любых замечаний после релиза.</div>
      </div>
    </div>

    <div class="footer-note">
      <div>Исполнители: <strong style="color:#0f172a;">Имран & Мубин (Senior Engineers)</strong></div>
      <div>Связь в Telegram: <strong style="color:#0284c7;">@rolldurov</strong> (https://t.me/rolldurov)</div>
    </div>
  </div>
</body>
</html>`);
    frameDoc.close();

    printFrame.contentWindow.focus();
    setTimeout(() => {
      printFrame.contentWindow.print();
    }, 200);
  } catch (err) {
    window.print();
  }
}

// 11. Live Telegram Floating Widget
function initLiveTelegramWidget() {
  const toggleBtn = document.getElementById('live-chat-toggle-btn');
  const popup = document.getElementById('live-chat-popup');
  const closeBtn = document.getElementById('close-live-chat-btn');

  if (!toggleBtn || !popup) return;

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    popup.classList.toggle('hidden');
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      popup.classList.add('hidden');
    });
  }

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!popup.classList.contains('hidden') && !popup.contains(e.target) && !toggleBtn.contains(e.target)) {
      popup.classList.add('hidden');
    }
  });
}

// 12. Export Leads to CSV / Excel
function initCsvExport() {
  const exportBtn = document.getElementById('export-leads-csv-btn');
  if (!exportBtn) return;

  exportBtn.addEventListener('click', async () => {
    const leads = await fetchLeads();
    if (!leads || leads.length === 0) {
      alert('Нет сохраненных заявок для экспорта.');
      return;
    }

    // Generate CSV with UTF-8 BOM for proper Russian display in Microsoft Excel
    let csvContent = '\uFEFFID;Дата;Контакт;Задача;Расчет;Статус\n';

    leads.forEach(l => {
      const id = l.id || '';
      const date = `"${(l.created_at || '').replace(/"/g, '""')}"`;
      const contact = `"${(l.contact || '').replace(/"/g, '""')}"`;
      const project = `"${(l.project || '').replace(/"/g, '""').replace(/\n/g, ' ')}"`;
      const calc = `"${(l.calc_summary || '').replace(/"/g, '""')}"`;
      const status = `"${(l.status || 'new').replace(/"/g, '""')}"`;

      csvContent += `${id};${date};${contact};${project};${calc};${status}\n`;
    });

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `devduo_leads_${new Date().toISOString().slice(0, 10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  });
}



