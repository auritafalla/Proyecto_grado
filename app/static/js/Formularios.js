document.addEventListener("DOMContentLoaded", function () {
    const opcionSelect = document.getElementById('opcion');
    const formContainers = document.querySelectorAll('.form-container');

    function showForm(formId) {
        formContainers.forEach(container => {
            container.style.display = 'none';
        });

        const selectedForm = document.getElementById(formId);
        if (selectedForm) {
            selectedForm.style.display = 'block';
            images.forEach(image => {
                image.style.display = 'block';
            });
        }
    }

    function clearFormAndRefresh(formId) {
        var form = document.getElementById(formId);
        form.reset();
        form.style.display = 'none';
        images.forEach(image => {
            image.style.display = 'block';
        });
    }

    // Al cargar la página, mostrar solo las opciones
    showForm('');

    opcionSelect.addEventListener('change', () => {
        const selectedOption = opcionSelect.value;
        showForm(`${selectedOption}-form`);
    });

    // Añade este código para manejar las opciones en pantallas pequeñas
    if (window.innerWidth <= 730) {
        opcionSelect.addEventListener('change', () => {
            const selectedOption = opcionSelect.value;
            showForm(`${selectedOption}-form`);
        });
    }
});


document.getElementById('abrir-modal').addEventListener('click', function() {
    document.getElementById('mi-modal').style.display = 'block';
});

document.getElementById('cerrar-modal').addEventListener('click', function() {
    document.getElementById('mi-modal').style.display = 'none';
});