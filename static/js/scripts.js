// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function () {
    // Sidebar collapsible menu functionality
    document.querySelectorAll('.sidebar h4').forEach(header => {
        header.addEventListener('click', () => {
            header.classList.toggle('active');
            const collapsibleMenu = header.nextElementSibling;
            collapsibleMenu.style.display = 
                collapsibleMenu.style.display === 'block' ? 'none' : 'block';
        });
    });

    // Smooth scroll for specific navigation links with 'scroll-link' class
    const scrollLinks = document.querySelectorAll('.scroll-link');
    scrollLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetSection = document.querySelector(link.getAttribute('href'));
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Dashboard navigation button handling
    const dashboardLinks = document.querySelectorAll('.dashboard-btn');
    dashboardLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetPage = this.getAttribute('data-page');
            window.location.href = `/${targetPage}`;
        });
    });
});