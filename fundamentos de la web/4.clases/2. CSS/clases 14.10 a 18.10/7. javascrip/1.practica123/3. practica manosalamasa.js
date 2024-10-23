// Función que crea un objeto pizza
function pizzaOven(corteza, salsa, queso, topings) {
    let pizza = {
        corteza: corteza,
        salsa: salsa,
        queso: queso,
        topings: topings,
    };
    return pizza;
}

// Primera pizza: estilo Chicago
let pizza1 = pizzaOven("estilo Chicago", "tradicional", ["mozzarella"], ["pepperoni", "salchicha"]);
console.log("primera pizza: Estilo Chicago ",pizza1);

// Segunda pizza: iberica
let pizza2 = pizzaOven("lanzada a mano", "marinara", ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
console.log("Segunda pizza: iberica" ,pizza2);

// Tercera pizza: personalizada1
let pizza3 = pizzaOven("crujiente", "salsa BBQ", ["cheddar", "mozzarella"], ["pollo", "maíz", "jalapeños"]);
console.log("Tercera pizza: personalizada1", pizza3);

// Cuarta pizza: personalizada2
let pizza4 = pizzaOven("masa fina", "pesto", ["parmesano", "gouda"], ["espinacas", "tomates secos", "alcachofas"]);
console.log("Cuarta pizza: personalizada2",pizza4);
