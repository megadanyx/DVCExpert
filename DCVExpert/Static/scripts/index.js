document.addEventListener('DOMContentLoaded', function() {
    // Funcție pentru a verifica dacă suntem pe un dispozitiv mobil
    const isMobile = () => window.innerWidth < 768;
    
    // Funcție pentru a crea carusel pentru o secțiune specifică
    const createCarousel = (cardsSelector, containerSelector, titleSelector, carouselName) => {
        // Obține toate cardurile și containerul
        const cards = document.querySelectorAll(cardsSelector);
        const container = document.querySelector(containerSelector);
        
        if (!cards.length || !container) return;
        
        let currentIndex = 0;
        let slideInterval;
        
        // Crează butoanele de navigare
        const createNavButtons = () => {
            const navContainer = document.createElement('div');
            navContainer.className = `${carouselName}-carousel-nav`;
            
            const prevButton = document.createElement('button');
            prevButton.className = `${carouselName}-prev-btn`;
            prevButton.innerHTML = '&#10094;';
            prevButton.setAttribute('aria-label', 'Previous');
            
            const nextButton = document.createElement('button');
            nextButton.className = `${carouselName}-next-btn`;
            nextButton.innerHTML = '&#10095;';
            nextButton.setAttribute('aria-label', 'Next');
            
            navContainer.appendChild(prevButton);
            navContainer.appendChild(nextButton);
            
            // Adaugă container-ul de navigare în DOM
            const parentElement = container.parentNode;
            parentElement.appendChild(navContainer);
            
            // Adaugă event listeners
            prevButton.addEventListener('click', showPrevCard);
            nextButton.addEventListener('click', showNextCard);
        };
        
        // Arată un card specific după index
        const showCard = (index) => {
            if (!isMobile()) {
                // Dacă nu e mobil, arată toate cardurile
                cards.forEach(card => {
                    card.style.display = '';
                });
                return;
            }
            
            // Ascunde toate cardurile
            cards.forEach(card => {
                card.style.display = 'none';
            });
            
            // Asigură-te că indexul se învârte în cerc
            currentIndex = (index + cards.length) % cards.length;
            
            // Arată cardul curent
            cards[currentIndex].style.display = 'block';
            cards[currentIndex].style.animation = 'fadeIn 0.5s ease-in-out';
        };
        
        // Funcții de navigare
        const showNextCard = () => {
            showCard(currentIndex + 1);
            resetInterval();
        };
        
        const showPrevCard = () => {
            showCard(currentIndex - 1);
            resetInterval();
        };
        
        // Pornește derularea automată
        const startAutoSlide = () => {
            if (isMobile()) {
                slideInterval = setInterval(showNextCard, 5000);
            }
        };
        
        // Resetează intervalul când se navighează manual
        const resetInterval = () => {
            clearInterval(slideInterval);
            startAutoSlide();
        };
        
        // Aplică logica de carusel bazată pe dimensiunea ecranului
        const applyCarouselLogic = () => {
            const navContainer = document.querySelector(`.${carouselName}-carousel-nav`);
            
            if (isMobile()) {
                // Vizualizare mobilă - activează carusel
                showCard(currentIndex);
                startAutoSlide();
                
                // Arată butoanele de navigare dacă nu există
                if (!navContainer) {
                    createNavButtons();
                } else {
                    navContainer.style.display = 'flex';
                }
            } else {
                // Vizualizare desktop - arată toate cardurile
                cards.forEach(card => {
                    card.style.display = '';
                });
                
                // Ascunde butoanele de navigare pe desktop
                if (navContainer) {
                    navContainer.style.display = 'none';
                }
                
                // Șterge intervalul dacă există
                if (slideInterval) {
                    clearInterval(slideInterval);
                }
            }
        };
        
        // Configurarea inițială
        applyCarouselLogic();
        
        // Returnează funcția pentru a gestiona redimensionarea ferestrei
        return applyCarouselLogic;
    };
    
    // Inițializează caruselele
    const teacherCarouselLogic = createCarousel(
        '.benefit_card', 
        '.benefit_cards', 
        '.benefit_title', 
        'teacher'
    );
    
    const courseCarouselLogic = createCarousel(
        '.Cours', 
        '.Courses', 
        '.courses_section h2', 
        'course'
    );
    
    // Ascultă redimensionarea ferestrei
    window.addEventListener('resize', function() {
        teacherCarouselLogic();
        courseCarouselLogic();
    });
});