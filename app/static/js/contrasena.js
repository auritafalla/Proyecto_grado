/* The code is adding an event listener to the `DOMContentLoaded` event of the `document` object. This
event is fired when the initial HTML document has been completely loaded and parsed. */
document.addEventListener("DOMContentLoaded", function () {
    var passwordForm = document.getElementById("password-form");
    var customModal = document.getElementById("custom-modal");
    var modalMessage = document.getElementById("modal-message");
    var closeBtn = document.querySelector(".close");

    passwordForm.addEventListener("submit", function (event) {
        event.preventDefault();

        var oldPassword = document.getElementById("oldPassword").value;
        var newPassword = document.getElementById("newPassword").value;
        var confirmPassword = document.getElementById("confirmPassword").value;

        if (newPassword === oldPassword) {
            // Mostrar el mensaje de error en la ventana modal si la nueva contraseña es igual a la antigua
            modalMessage.innerHTML = "La nueva contraseña debe ser diferente a la contraseña antigua";
            modalMessage.classList.add("error-message"); // Agregar la clase de error
            customModal.style.display = "block";
        } else if (newPassword === confirmPassword) {
            // Mostrar el mensaje de éxito en la ventana modal si la contraseña se actualiza con éxito
            modalMessage.innerHTML = "Contraseña actualizada con éxito";
            modalMessage.classList.remove("error-message"); // Quitar la clase de error
            customModal.style.display = "block";
        } else {
            // Mostrar el mensaje de error en la ventana modal si la nueva contraseña y la confirmación no coinciden
            modalMessage.innerHTML = "La nueva contraseña y la confirmación no coinciden";
            modalMessage.classList.add("error-message"); // Agregar la clase de error
            customModal.style.display = "block";
        }
    });

    // Cerrar la ventana modal al hacer clic en la 'x'
    closeBtn.addEventListener("click", function () {
        customModal.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var passwordForm = document.getElementById("password-form");
    var customModal = document.getElementById("custom-modal");
    var modalMessage = document.getElementById("modal-message");
    var closeBtn = document.querySelector(".close");

    passwordForm.addEventListener("submit", function (event) {
        event.preventDefault();

        // Tu código de validación de contraseñas aquí...

    });

    // Cerrar la ventana modal al hacer clic en la 'x'
    closeBtn.addEventListener("click", function () {
        customModal.style.display = "none";
    });
});

    
