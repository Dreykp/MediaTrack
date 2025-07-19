const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

    function updateIcons(currentTheme) {
      if (currentTheme === 'dark') {
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
      } else {
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
      }
    }

    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-theme', savedTheme);
    updateIcons(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
      let currentTheme = htmlElement.getAttribute('data-theme');
      let newTheme = currentTheme === 'light' ? 'dark' : 'light';
      htmlElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateIcons(newTheme);
    });