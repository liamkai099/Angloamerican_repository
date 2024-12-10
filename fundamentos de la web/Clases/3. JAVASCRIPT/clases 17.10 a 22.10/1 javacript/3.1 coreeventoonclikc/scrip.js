
// BOTON MEGUSTA CON CONTADOR
var contador = 0; // inicializamos el contador en 0
var boton = document.getElementById("likebtn"); // obtenemos el botón

boton.addEventListener("click", function() {
    contador++; // incrementamos el contador
    boton.textContent = contador + " Me gusta"; // actualizamos el texto del botón
});

// BOTON MEGUSTA CON CONTADOR
var contadorM = 0;
var botonM = document.getElementById("likeboton"); // obtenemos el botón

botonM.addEventListener("click", function() {
    contadorM++; // incrementamos el contador
    botonM.textContent = contadorM + " Me gusta"; // actualizamos el texto del botón
});





const botonesLike = document.querySelectorAll('.pet-card button'); // Selecciona todos los botones "Me gusta"

botonesLike.forEach((boton, index) => {
    let likes = parseInt(boton.textContent.match(/\d+/)) || 1; // Inicializa los likes basados en el número en el texto del botón

    boton.addEventListener('click', function() {
        // Obtiene el título de la definición
        const titulo = this.parentElement.querySelector('h2').textContent;

        // Muestra la alarma con el título
        alert(`Te gustó la definición de: ${titulo}`);

        // Incrementa el número de likes
        likes += 1;

        // Actualiza el texto del botón con el nuevo conteo de "Me gusta"
        this.textContent = `Me gusta${likes}`;
        
        // Si ya existe un contador de likes visible, lo actualiza
        if (!this.nextSibling || !this.nextSibling.classList.contains('like-counter')) {
            // Crea un nuevo elemento para mostrar los likes si no existe
            const contadorLikes = document.createElement('span');
            contadorLikes.classList.add('like-counter');
            contadorLikes.textContent = ` Likes: ${likes}`;
            this.parentElement.appendChild(contadorLikes);
        } else {
            //actualiza el contador de likes
            this.nextSibling.textContent = ` Likes: ${likes}`;
        }
    });
});

