document.addEventListener("DOMContentLoaded", function () {
    const accordionHeaders = document.querySelectorAll(".accordion-header");

    accordionHeaders.forEach((header) => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            content.style.display = content.style.display === "block" ? "none" : "block";
            const arrow = this.querySelector("span");
            arrow.innerHTML = content.style.display === "block" ? "&#9650;" : "&#9660;";
        });
    });

    const slider = document.querySelector('.slider');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');

    let currentIndex = 0;

    function goToSlide(index) {
        currentIndex = index;
        const translateX = -currentIndex * 100 + '%';
        slider.style.transform = `translateX(${translateX})`;
    }

    prevButton.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            goToSlide(currentIndex);
        }
    });

    nextButton.addEventListener('click', () => {
        if (currentIndex < 2) { // Cambia este valor al número total de slides menos 1
            currentIndex++;
            goToSlide(currentIndex);
        }
    });

    const toggle = document.getElementById('toggle');
    const navList = document.querySelector('.list');

    toggle.addEventListener('change', () => {
        if (toggle.checked) {
            navList.classList.add('active');
        } else {
            navList.classList.remove('active');
        }
    });

    const preguntas = document.querySelectorAll(".pregunta");

    preguntas.forEach((pregunta) => {
        pregunta.addEventListener("click", function () {
            this.classList.toggle("active");
        });
    });
});

// Preguntas frecuentes

const accordionItemHeaders = document.querySelectorAll(".accordion-item-header");

accordionItemHeaders.forEach(accordionItemHeader => {
    accordionItemHeader.addEventListener("click", event => {


        accordionItemHeader.classList.toggle("active");
        const accordionItemBody = accordionItemHeader.nextElementSibling;
        if (accordionItemHeader.classList.contains("active")) {
            accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
        }
        else {
            accordionItemBody.style.maxHeight = 0;
        }

    });
});
