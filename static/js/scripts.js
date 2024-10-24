document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('theme-toggle');
    const body = document.body;
    const table = document.querySelector('table');

    // Initialize theme based on current class
    if (body.classList.contains('dark-mode')) {
        table.classList.add('dark-mode');
    } else {
        table.classList.add('light-mode');
    }

    toggle.addEventListener('click', () => {
        const isDarkMode = body.classList.toggle('dark-mode');

        // Set theme class on the table based on the body class
        if (isDarkMode) {
            table.classList.remove('light-mode');
            table.classList.add('dark-mode');
        } else {
            table.classList.remove('dark-mode');
            table.classList.add('light-mode');
        }
    });
});
