/* main.js */

document.addEventListener('DOMContentLoaded', () => {
  // --- Theme Toggle (Light/Dark Mode) ---
  const themeToggle = document.getElementById('themeToggle');
  const htmlElement = document.documentElement;
  
  // Check local storage or system preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    htmlElement.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    htmlElement.setAttribute('data-theme', 'dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Toggle icon
      themeToggle.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
    });
    
    // Set initial icon
    themeToggle.innerHTML = htmlElement.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
  }

  // --- RTL Toggle ---
  const rtlToggle = document.getElementById('rtlToggle');
  if (rtlToggle) {
    rtlToggle.addEventListener('click', () => {
      const isRTL = htmlElement.getAttribute('dir') === 'rtl';
      htmlElement.setAttribute('dir', isRTL ? 'ltr' : 'rtl');
    });
  }

  // --- Sticky Header ---
  const header = document.querySelector('.global-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // --- Scroll Animations (Intersection Observer) ---
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        // Optional: stop observing once animated
        // observer.unobserve(entry.target); 
      }
    });
  }, observerOptions);

  const animatedElements = document.querySelectorAll('.animate-on-scroll');
  animatedElements.forEach(el => observer.observe(el));

  // --- Back to Top Button ---
  const backToTopBtn = document.getElementById('backToTop');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- Counter Animation ---
  const counters = document.querySelectorAll('.counter-value');
  if (counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const endValue = parseInt(target.getAttribute('data-target'));
          let startValue = 0;
          const duration = 2000;
          const increment = endValue / (duration / 16); // 60fps
          
          const updateCounter = () => {
            startValue += increment;
            if (startValue < endValue) {
              target.innerText = Math.ceil(startValue);
              requestAnimationFrame(updateCounter);
            } else {
              target.innerText = endValue;
            }
          };
          
          updateCounter();
          obs.unobserve(target);
        }
      });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));
  }
});
