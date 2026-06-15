
    const sections = Array.from(document.querySelectorAll('section[id]'));
    const navLinkElements = document.querySelectorAll('.nav-link');
    const navLinksMenu = document.getElementById('nav-links');
    const menuToggle = document.getElementById('menu-toggle');

    // Resalta la sección que está más cerca de la parte superior (considerando header fijo)
    function updateActiveNav() {
      const offset = 120; // ajustar según altura del header
      let currentId = sections[0] ? sections[0].id : '';
      for (const sec of sections) {
        const rect = sec.getBoundingClientRect();
        if (rect.top <= offset) {
          currentId = sec.id;
        }
      }
      navLinkElements.forEach(link => {
        if (link.getAttribute('href') === `#${currentId}`) link.classList.add('active');
        else link.classList.remove('active');
      });
    }

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          updateActiveNav();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    window.addEventListener('resize', updateActiveNav);
    document.addEventListener('DOMContentLoaded', updateActiveNav);
    updateActiveNav();

    menuToggle?.addEventListener('click', () => {
      const isOpen = navLinksMenu.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', isOpen);
      menuToggle.innerHTML = isOpen ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
    });

    document.querySelectorAll('#nav-links a').forEach(link => {
      link.addEventListener('click', () => {
        if (navLinksMenu.classList.contains('open')) {
          navLinksMenu.classList.remove('open');
          menuToggle.setAttribute('aria-expanded', 'false');
          menuToggle.innerHTML = '<i class="fa-solid fa-bars"></i>';
        }
      });
    });

    const skillCards = document.querySelectorAll('.skill-card');
    const skillsContainer = document.getElementById('skills-container');

    // Observa el contenedor de habilidades y lanza la animación en secuencia
    const fastStagger = 80; // ms entre cada icono
    const containerObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          skillCards.forEach((card, i) => {
            setTimeout(() => card.classList.add('visible'), i * fastStagger);
          });
          obs.unobserve(entry.target);
        }
      });
    }, { root: null, rootMargin: '0px 0px -30% 0px', threshold: 0 });

    if (skillsContainer) containerObserver.observe(skillsContainer);