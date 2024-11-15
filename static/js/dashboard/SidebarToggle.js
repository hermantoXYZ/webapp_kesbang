document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelector('.sidebar');
    var barIcon = document.querySelector('.sidebar-toggle');
    var closeBtn = document.querySelector('.close-btn');

    barIcon.addEventListener('click', function(e) {
        e.preventDefault();
        sidebar.classList.toggle('show');
    });

    closeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        sidebar.classList.remove('show');
    });

    // Close the sidebar if the user clicks outside of it
    window.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && event.target !== barIcon) {
            sidebar.classList.remove('show');
        }
    });
});