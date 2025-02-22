/* //Display greeting to a person.
function displayGreeting(name){
    const message =`Hello, ${name}!`;
    console.log(message);
}
displayGreeting("Is'haaq Daahir");
 */
//To set a default value for the salutation.
/* function displayGreeting(name, salutation = 'Hello'){
    console.log(`${salutation}, ${name}`);
}
displayGreeting("Is'haaq Daahir")
//To set a default value for the salutation again.
displayGreeting("Is'haaq Daahir", 'Hi') */

//Creating a greeting message using Return value.
/* function createGreetingMessage(name){
    const message =`Hello, ${name}!`;
    return message;
}
const greetingMessage = createGreetingMessage("Is'haaq Daahir");
console.log(greetingMessage);
 */

/* //Functions as parameters for functions. Consider setTimeout, which begins a timer and will execute-
//code when it completes. We need to tell it what code we want to execute.
function displayDone(){
    console.log('3 seconds has elapsed');
}
//Timer value is in milliseconds.
setTimeout(displayDone, 3000); */

/* //Anonymous function. We have created a function, but didn't have to give it a name.
setTimeout(function(){
    console.log('3 seconds has elapsed');
}, 3000); */

/* //Fat Arrow Function. We use special indicator '=>' symbol to skip writing 'function'.
setTimeout(() => {
    console.log('3 seconds has elapsed');
}, 3000); */

// TERNARY EXPRESSIONS.
//SYNTAX: let variable = condition ? <return this if true> : <return this if false>

/* let firstNumber = 20;
let secondNumber = 10;
let biggestNumber = firstNumber > secondNumber ? firstNumber : secondNumber;

//It means: If firstNumber is greater than secondNumber, the assign firstNumber to biggestNumber, else assign secondNumber.

//The Ternary Expression is just a compact way of writing the code below:
let biggestNumber;
if (firstNumber > secondNumber){
    biggestNumber = firstNumber;
} else {
    biggestNumber = secondNumber;
} */

//GITHUB ARRAYS.
/* let iceCreamFlavors = ['Chocolate','Strawberry','Vanilla','Pistachio']
//You can leverage the index to change the value like this as follows.
    iceCreamFlavors[0] = 'Banana'

//And you can insert a new value at a given index like this as follows:
iceCreamFlavors[4] = 'Shinkafa Kaza';
//console.log(iceCreamFlavors)

//To find the length, we do as follows:
console.log(iceCreamFlavors.length) */

//LOOPS AND ARRAYS.
let iceCreamFlavors = ['Chocolate','Strawberry','Vanilla','Pistachio']

for ( let i = 0; i < iceCreamFlavors.length; i++){
    console.log(iceCreamFlavors[i])
}
