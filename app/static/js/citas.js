document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var abrirModalButtons = document.querySelectorAll('#abrirModal');
    var cerrarModal = document.querySelector('.close');

  
    abrirModalButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        modal.style.display = 'block';
        var estadoCita = button.getAttribute('data-estado-cita');
        document.getElementById('estado-cita').value = estadoCita;
      });
    }); 
  
    cerrarModal.addEventListener('click', function() {
      modal.style.display = 'none';
    });
  
    window.addEventListener('click', function(event) {
      if (event.target == modal) {
        modal.style.display = 'none';
      }
    }); 
  });