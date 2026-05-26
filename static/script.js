const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');
const themeToggle = document.getElementById('themeToggle');

const saveTheme = (theme) => {
  localStorage.setItem('siteTheme', theme);
  document.body.classList.toggle('light', theme === 'light');
  document.body.classList.toggle('dark', theme === 'dark');
  themeToggle.textContent = theme === 'light' ? '🌙' : '☀️';
};

const currentTheme = localStorage.getItem('siteTheme') || 'dark';
saveTheme(currentTheme);

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const nextTheme = document.body.classList.contains('light') ? 'dark' : 'light';
    saveTheme(nextTheme);
  });
}

if (menuToggle) {
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}

const navItems = document.querySelectorAll('.nav-links a');
navItems.forEach((item) => {
  item.addEventListener('click', () => {
    navLinks.classList.remove('active');
  });
});

// See more / See less toggle for projects
const seeMoreBtn = document.getElementById('seeMoreBtn');
if (seeMoreBtn) {
  const hiddenCards = document.querySelectorAll('.project-card.hidden');
  if (hiddenCards.length === 0) {
    // nothing to show — hide the button
    seeMoreBtn.style.display = 'none';
  } else {
    seeMoreBtn.style.display = 'inline-block';
    // initialize hidden cards as display:none
    hiddenCards.forEach(c => c.style.display = 'none');

    seeMoreBtn.addEventListener('click', () => {
      const stillHidden = document.querySelectorAll('.project-card.hidden');
      const isHidden = stillHidden.length > 0 && stillHidden[0].style.display !== 'block';
      if (isHidden) {
        stillHidden.forEach(c => c.style.display = 'block');
        seeMoreBtn.textContent = 'See less';
      } else {
        stillHidden.forEach((c, i) => { if (i >= 0) c.style.display = 'none'; });
        seeMoreBtn.textContent = 'See more';
        window.scrollTo({ top: document.getElementById('projects').offsetTop - 60, behavior: 'smooth' });
      }
    });
  }
}
