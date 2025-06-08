document.addEventListener('DOMContentLoaded', () => {
    const sidebarLinks = document.querySelectorAll('.sidebar ul li a');
    const contentSections = document.querySelectorAll('.content-section');
    const currentSectionTitle = document.getElementById('current-section-title');

    function showSection(id) {
        contentSections.forEach(section => {
            section.style.display = 'none';
        });
        const activeSection = document.getElementById(id);
        if (activeSection) {
            activeSection.style.display = 'block';
            currentSectionTitle.textContent = activeSection.querySelector('.section-title') ? activeSection.querySelector('.section-title').textContent : (id.charAt(0).toUpperCase() + id.slice(1)).replace('-', ' '); // Título dinâmico
        }
    }

    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault(); // Evita o comportamento padrão do link
            sidebarLinks.forEach(item => item.classList.remove('active'));
            link.classList.add('active');
            const targetId = link.getAttribute('href').substring(1); // Remove o '#'
            showSection(targetId);
        });
    });

    // Mostra a seção do dashboard por padrão ao carregar a página
    showSection('dashboard');
});