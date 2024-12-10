document.addEventListener('DOMContentLoaded', function() {
  // Selección de los elementos
  const solicitudesCount = document.getElementById('solicitudes-count');  // Contador de solicitudes
  const connectionsCount = document.getElementById('connections-count');  // Contador de conexiones

  let solicitudes = 2;  // Número inicial de solicitudes
  let conexiones = 500; // Número inicial de conexiones

  // Función para actualizar los contadores
  function updateCounts() {
      solicitudesCount.textContent = `Solicitudes de Conexión (${solicitudes})`;
      connectionsCount.textContent = `Tus Conexiones (${conexiones} )`;
  }

  // Función para eliminar una solicitud de conexión
  function removeRequest(requestElement) {
      requestElement.remove();  // Eliminar la solicitud de la lista
      solicitudes--;  // Disminuir el número de solicitudes
      conexiones--;
      updateCounts();  // Actualizar los contadores
  }

  // Función para aceptar una solicitud de conexión
  function acceptRequest(requestElement) {
      requestElement.remove();  // Eliminar la solicitud de la lista
      solicitudes--;  // Disminuir el número de solicitudes pendientes
      conexiones++;  // Incrementar el número de conexiones
      updateCounts();  // Actualizar los contadores
  
  }

  // Manejo de eventos para los botones de aceptar
  document.querySelectorAll('.accept').forEach(button => {
      button.addEventListener('click', function() {
          const requestElement = this.closest('.request');
          acceptRequest(requestElement);  // Llamada a la función de aceptar solicitud
      });
  });

  // Manejo de eventos para los botones de rechazar
  document.querySelectorAll('.decline').forEach(button => {
      button.addEventListener('click', function() {
          const requestElement = this.closest('.request');
          removeRequest(requestElement);  // Llamada a la función de rechazar solicitud
      });
  });
});


// Obtén el botón de editar y el nombre del perfil
const botonEditar = document.querySelector(".boton");
const nombre = document.querySelector(".nombre");

// Agrega un evento de clic para cambiar el nombre
botonEditar.addEventListener("click", function () {
  nombre.textContent = "aitor099"; // Cambia el contenido del nombre
});
