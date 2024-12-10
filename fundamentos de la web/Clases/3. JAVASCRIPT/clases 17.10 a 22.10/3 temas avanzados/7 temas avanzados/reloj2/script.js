let hr = document.getElementById('hour-hand');
let min = document.getElementById('minute-hand');
let sec = document.getElementById('second-hand');
let digitalTime = document.getElementById('digital-time'); // Elemento para mostrar la hora digital

function displayTime() {
    let date = new Date();
    
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();

    // Formatear la hora digital con ceros a la izquierda
    let formattedTime = `${hh.toString().padStart(2, '0')}:${mm.toString().padStart(2, '0')}:${ss.toString().padStart(2, '0')}`;
    digitalTime.textContent = formattedTime; // Actualizar la hora digital

    // Calcular la rotación de las manecillas
    let hRotation = 30 * (hh % 12) + mm / 2; // Cada hora es 30 grados (360 / 12), asegurando que la manecilla de la hora se mueva gradualmente
    let mRotation = 6 * mm;           // Cada minuto es 6 grados (360 / 60)
    let sRotation = 6 * ss;           // Cada segundo es 6 grados (360 / 60)
    
    // Actualizar las rotaciones de las manecillas
    hr.style.transform = `rotate(${hRotation}deg)`;
    min.style.transform = `rotate(${mRotation}deg)`;
    sec.style.transform = `rotate(${sRotation}deg)`;
}

// Llamar a displayTime cada segundo para actualizar el reloj analógico y digital
setInterval(displayTime, 1000);
