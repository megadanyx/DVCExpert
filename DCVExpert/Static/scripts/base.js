document.addEventListener('DOMContentLoaded', function () {
    var loginButton = document.querySelector('.login'); 
    var loginWindow = document.querySelector('.login-window'); 
    var signinButton = document.querySelector('.signin'); 
    var signinWindow = document.querySelector('.signin-window'); 
    var loadingOverlay = document.getElementById('loading-overlay');
    var bodyContent = document.querySelector('body');

    // Verifică dacă loginButton și loginWindow există înainte de a adăuga event listener
    if (loginButton && loginWindow) {
        loginButton.addEventListener('click', function (event) {
            event.stopPropagation();
            loginWindow.style.display = (loginWindow.style.display === 'block') ? 'none' : 'block';
        });

        document.addEventListener('click', function (event) {
            if (!loginButton.contains(event.target) && !loginWindow.contains(event.target)) {
                loginWindow.style.display = 'none';
            }
        });
    }

    // Verifică dacă signinButton și signinWindow există
    if (signinButton && signinWindow) {
        signinButton.addEventListener('click', function (event) {
            event.stopPropagation();
            signinWindow.style.display = (signinWindow.style.display === 'block') ? 'none' : 'block';
        });
    }

    // Ascunde overlay-ul după ce pagina s-a încărcat complet
    if (loadingOverlay) {
        loadingOverlay.classList.add('hidden');
        bodyContent.classList.remove('blurred');
    }

    // Verifică dacă loginForm există înainte de a adăuga event listener
    var loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function () {
            if (loadingOverlay) {
                loadingOverlay.classList.remove('hidden');
            }
        });
    }

    menuToggle = document.querySelector(".menu-toggle")
    navBarLinks   = document.querySelector(".nav-links")

    menuToggle.addEventListener("click", function() {
        // menuToggle.classList.toggle('active')
        navBarLinks.classList.toggle("nav-active");


        if (navBarLinks.classList.contains('nav-active')) {
            menuToggle.innerHTML = '&#10006;'; // simbolul ✖
        } else {
            menuToggle.innerHTML = '☰'; // simbolul inițial
        }

    });

});        