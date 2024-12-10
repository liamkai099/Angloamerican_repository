/*  Te dejo un poco de código para empezar, el resto debes completarlo tú.

let hr = document.getElementById(‘’);
let min = 
let sec = 

function displayTime(){
	let date = new Date();
	
	let hh = date.getHours();
	let mm =
	let ss =

	let hRotation = 30*hh + mm/2;
	let mRotation = 6*mm;
	let sRotation = 6*ss;
	
	hr.style.transform = `rotate(${}deg)`;
	min.style.transform = 
	sec.style.transform = 
}

setInterval(); */

let hr = document.getElementById('hour-hand');
let min = document.getElementById('minute-hand');
let sec = document.getElementById('second-hand');

function displayTime() {
    let date = new Date();
    
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    
    let hRotation = 30 * hh + mm / 2; // Cada hora es 30 grados (360 / 12)
    let mRotation = 6 * mm;           // Cada minuto es 6 grados (360 / 60)
    let sRotation = 6 * ss;           // Cada segundo es 6 grados (360 / 60)
    
    hr.style.transform = `rotate(${hRotation}deg)`;
    min.style.transform = `rotate(${mRotation}deg)`;
    sec.style.transform = `rotate(${sRotation}deg)`;
}

// Actualizar la hora cada segundo
setInterval(displayTime, 1000);
