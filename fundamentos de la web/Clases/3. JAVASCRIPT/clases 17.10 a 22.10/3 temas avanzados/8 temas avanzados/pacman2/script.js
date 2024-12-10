// Obtener el contexto del canvas
const canvas = document.getElementById("pacmanCanvas");
const ctx = canvas.getContext("2d");

// Tamaño del lienzo
canvas.width = 400;
canvas.height = 400;

// Variables del juego
let pacManRadius = 15;
let pacManX = 50;
let pacManY = 50;
let pacManSpeed = 5;
let pacManDirection = "right"; // Puede ser "right", "left", "up", "down"
let pacManAngle = 1.5 * Math.PI; // Dirección inicial de Pac-Man

// Función para dibujar a Pac-Man
function drawPacMan() {
  ctx.beginPath();
  ctx.arc(pacManX, pacManY, pacManRadius, pacManAngle, 2.5 * Math.PI);
  ctx.lineTo(pacManX, pacManY);
  ctx.fillStyle = "yellow";
  ctx.fill();
  ctx.closePath();
}

// Función para mover a Pac-Man
function movePacMan() {
  if (pacManDirection === "right") pacManX += pacManSpeed;
  if (pacManDirection === "left") pacManX -= pacManSpeed;
  if (pacManDirection === "up") pacManY -= pacManSpeed;
  if (pacManDirection === "down") pacManY += pacManSpeed;

  // Verificar los límites del lienzo
  if (pacManX > canvas.width) pacManX = 0;
  if (pacManX < 0) pacManX = canvas.width;
  if (pacManY > canvas.height) pacManY = 0;
  if (pacManY < 0) pacManY = canvas.height;
}

// Función para actualizar el juego
function update() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar el lienzo

  drawPacMan();
  movePacMan();

  requestAnimationFrame(update); // Llamar a la función repetidamente
}

// Controlar el movimiento de Pac-Man con las teclas
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") pacManDirection = "right";
  if (e.key === "ArrowLeft") pacManDirection = "left";
  if (e.key === "ArrowUp") pacManDirection = "up";
  if (e.key === "ArrowDown") pacManDirection = "down";
});

// Comenzar el juego
update();
