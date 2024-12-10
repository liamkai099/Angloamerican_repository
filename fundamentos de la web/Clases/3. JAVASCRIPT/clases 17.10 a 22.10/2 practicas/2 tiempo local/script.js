// Mostrar alerta al cargar la página
window.onload = function () {
    alert("Cargando Reporte del Clima");
};

// Función para ocultar el banner de cookies
function acceptCookies() {
    const cookieBanner = document.querySelector("footer");
    cookieBanner.style.display = "none"; // Oculta el banner
}

// Función para cambiar la ciudad, temperaturas, imágenes y descripciones
function changeCity(cityName) {
    const cityTitle = document.querySelector("h1"); // Cambiar el título de la ciudad
    const tempCards = document.querySelectorAll(".card p:last-child"); // Seleccionar las temperaturas de las tarjetas
    const weatherIcons = document.querySelectorAll(".card img"); // Seleccionar las imágenes de las tarjetas
    const weatherDescriptions = document.querySelectorAll(".card p:nth-child(2)"); // Seleccionar las descripciones de las tarjetas

    // Actualizar el título
    cityTitle.textContent = cityName;

    // Datos de cada ciudad con temperaturas, imágenes y descripciones
    const cityData = {
        "Buenos Aires": {
            temps: ["22°C | 15°C", "20°C | 13°C", "18°C | 11°C", "21°C | 14°C", "24°C | 17°C"],
            images: ["Nublado.png", "Lluvioso.png", "Tormenta.png", "Parcialmente nublado.png", "Soleado.png"],
            descriptions: ["Nublado", "Lluvioso", "Tormentas", "Parcialmente nublado", "Soleado"]
        },
        "Ciudad de México": {
            temps: ["25°C | 16°C", "23°C | 14°C", "22°C | 12°C", "24°C | 15°C", "26°C | 18°C"],
            images: ["Soleado.png", "Nublado.png", "Lluvioso.png", "Tormentas.png", "Parcialmente nublado.png"],
            descriptions: ["Soleado", "Nublado", "Lluvioso", "Tormentas", "Parcialmente nublado"]
        },
        "Santiago": {
            temps: ["18°C | 12°C", "19°C | 10°C", "17°C | 9°C", "20°C | 11°C", "21°C | 13°C"],
            images: ["Nublado.png", "Parcialmente nublado.png", "Lluvioso.png", "Tormentas.png", "Soleado.png"],
            descriptions: ["Nublado", "Parcialmente nublado", "Lluvioso", "Tormentas", "Soleado"]
        },
        "Sao Paulo": {
            temps: ["28°C | 20°C", "27°C | 19°C", "29°C | 21°C", "30°C | 22°C", "31°C | 23°C"],
            images: ["Soleado.png", "Lluvioso.png", "Nublado.png", "Tormentas.png", "Parcialmente nublado.png"],
            descriptions: ["Soleado", "Lluvioso", "Nublado", "Tormentas", "Parcialmente nublado"]
        },
        "Quito": {
            temps: ["16°C | 10°C", "17°C | 9°C", "15°C | 8°C", "18°C | 11°C", "19°C | 12°C"],
            images: ["Tormentas.png", "Nublado.png", "Lluvioso.png", "Parcialmente nublado.png", "Soleado.png"],
            descriptions: ["Tormentas", "Nublado", "Lluvioso", "Parcialmente nublado", "Soleado"]
        }
    };

    // Obtener los datos de la ciudad seleccionada
    const selectedCityData = cityData[cityName];

    // Actualizar las temperaturas, imágenes y descripciones
    if (selectedCityData) {
        tempCards.forEach((card, index) => {
            card.textContent = selectedCityData.temps[index] || "--°C | --°C"; // Actualiza las temperaturas
        });
        weatherIcons.forEach((icon, index) => {
            icon.src = `images/${selectedCityData.images[index]}`; // Cambia la ruta de la imagen
            icon.alt = selectedCityData.images[index].replace(".png", ""); // Actualiza el texto alternativo de la imagen
        });
        weatherDescriptions.forEach((description, index) => {
            description.textContent = selectedCityData.descriptions[index] || "Descripción no disponible"; // Actualiza las descripciones
        });
    }
}



















