const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

if (menuToggle) {
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

const navAnchors = document.querySelectorAll('.nav-links a');
navAnchors.forEach(anchor => {
  anchor.addEventListener('click', () => {
    navAnchors.forEach(a => a.classList.remove('active'));
    anchor.classList.add('active');
    if (navLinks) navLinks.classList.remove('open');
  });
});

function setupFilters(filterContainerId, itemsContainerId) {
  const filterContainer = document.getElementById(filterContainerId);
  const itemsContainer = document.getElementById(itemsContainerId);
  if (!filterContainer || !itemsContainer) return;

  const buttons = filterContainer.querySelectorAll('[data-filter]');
  const items = Array.from(itemsContainer.children);

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const value = button.getAttribute('data-filter');
      buttons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');

      items.forEach(item => {
        const tags = item.getAttribute('data-tags') || '';
        const show = value === 'All' || tags.includes(value);
        item.classList.toggle('hidden', !show);
      });
    });
  });
}

setupFilters('researchFilters', 'researchGrid');
setupFilters('pubFilters', 'pubGrid');
setupFilters('memberFilters', 'memberGrid');

const tagLinks = document.querySelectorAll('[data-filter-target]');
tagLinks.forEach(link => {
  link.addEventListener('click', () => {
    const target = link.getAttribute('data-filter-target');
    const researchButtons = document.querySelectorAll('#researchFilters [data-filter]');
    const researchGrid = document.getElementById('researchGrid');
    if (!researchGrid) return;

    researchButtons.forEach(btn => {
      const isActive = btn.getAttribute('data-filter') === target;
      btn.classList.toggle('active', isActive);
    });

    Array.from(researchGrid.children).forEach(item => {
      const tags = item.getAttribute('data-tags') || '';
      item.classList.toggle('hidden', !tags.includes(target));
    });
  });
});
