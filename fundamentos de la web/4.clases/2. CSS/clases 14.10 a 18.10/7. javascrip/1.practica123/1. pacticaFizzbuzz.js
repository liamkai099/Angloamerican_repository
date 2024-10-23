//¿Listo para un desafío de codificación clásico? ¡Vamos a resolver FizzBuzz! Aquí 
//está la misión: recorreremos los números del 1 al 100 y haremos lo siguiente:

//Si el número es divisible por 3, imprimiremos «Fizz».

//Si el número es divisible por 5, imprimiremos «Buzz».

//Si el número es divisible por ambos 3 y 5, imprimiremos «FizzBuzz».

//Para cualquier otro número, simplemente lo imprimiremos como es.

for (let i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}