
  document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll("nav a[href^='#']");

  function updateActiveNavLink() {
    let current = "";
    const scrollPosition = window.scrollY + 100; // Offset for fixed nav

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;

      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute("id");
      }
    });

    // If we're at the very top, highlight home
    if (window.scrollY < 50) {
      current = "home";
    }

    navLinks.forEach((link) => {
      link.classList.remove("active");
      const href = link.getAttribute("href");
      if (href === `#${current}`) {
        link.classList.add("active");
      }
    });
  }

  // Run on scroll
  window.addEventListener("scroll", updateActiveNavLink);
  
  // Run on page load
  updateActiveNavLink();

  // Smooth scrolling for nav links
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetSection = document.getElementById(targetId);
      
      if (targetSection) {
        const offsetTop = targetSection.offsetTop - 80; // Account for fixed nav
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
});

