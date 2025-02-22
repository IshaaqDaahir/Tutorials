var colors = ['red', 'blue', 'green', 'yellow'];
var selectedColor = colors[0];

 switch(selectedColor){
    case 'red':
        console.log('The color is red\n');
        break;
    case 'blue':
        console.log('The color is blue\n');
        break;
    case 'green':
        console.log('The color is green\n');
        break;
    case 'yellow':
        console.log('The color is yellow\n');
        break;
    default:
        console.log('There was an error\n');
}
/*
//Using && 
//true: if both of the conditions are true.
var goodMood = true;
var gotSleep = true;
var gotPaid = true;

if (goodMood && gotSleep && gotPaid){
    console.log('Today is a good day');
}
else{
    console.log('I am grumpy ')
}

var a = "World!";
var b = `Hello ${a}`;

console.log(b); 

var gotSleep = false;
var gotPaid = false;
var goodMood = false;

if (goodMood || gotSleep || gotPaid){
    console.log('Today is a good day');
}
else{
    console.log('I am grumpy ')
}

for(var i = 0; i <= 10; i++){
    console.log(i + '\n');
}

var food = ['grapes','cheese','bread','olives'];

for(var eachItemInside of food){
    console.log(eachItemInside);
}

var incrementor = 0;
var text = '';

while(incrementor <10){
    text += 'The incrementor has gone up to ' + incrementor  + '\n';
    incrementor++;
} 
console.log(text);

var incrementor = 0;
var text = '';

while(incrementor <10){
    text += `The incrementor has gone up to ${incrementor} \n`;
    incrementor++;
} 
console.log(text);

var i = 0;
while (i < 10){
    console.log(i);
    i++;
}

let text1 = 'hello, world!';
let text2 = 'hello, wars!'.toUpperCase();

console.log(text2);

var myString ='I am really hungry for some';
var myUpperString = myString.toUpperCase();
var foods = ['yam','tuwo','fate','shinkafa'];

console.log(`${myString} ${foods[0]}`);

//We do not really need \n for new line here.
for (var eachItem of foods){
    console.log(`${myString} ${eachItem}\n`)
}

for (i = 0; i < foods.length; i++){
    console.log(`${myString} ${foods[i]}`);
} 

var a = ['a','b','c','d'];
var i = 0;

while (a[i]){
    i++;
}
console.log(i);

//Finding length using a while loop.
i = 0;
var foods = ['yam','tuwo','fate','shinkafa'];
while(foods[i]){
    i++;
}
console.log('The length of foods is ', i);

//If index in foods is even, convert to uppercase, else don't convert 
var myString ='I am really hungry for some';
var foods = ['yam','tuwo','fate','shinkafa'];

for (i = 0; i < foods.length; i++){      // You either put '4' or foods.length, the answer is the same.
        if (i % 2 === 0){
            console.log(`${myString} ${foods[i].toUpperCase()}`);
    }
    else{
        console.log(`${myString} ${foods[i]}`);

    }
}

function nitdaAccepted() {
    console.log('Congrats, you have been accepted into NBS');
    console.log('Enroll to Bitcoin theory course at 5thwork.com');
}
nitdaAccepted();


function doStuff(){
    var myString = 'Here is a message';
    var upperString = myString.toUpperCase();
    console.log(myString);
    console.log(upperString);
}
doStuff();

function addNums(num1, num2){
    var sum = num1 + num2;
    console.log(`The total is ${sum}`);
}
addNums(4, 36)

function returnSum(num1, num2){
    var sum = num1 + num2;
    return sum;
}
console.log(returnSum(5, 3));

var greeting = 'Hello, and good morning!';

function capitalizeFunction(anyString){
    anyString = anyString.toUpperCase();
    return anyString;
}

var capitalizeExpression = function(anyString){
    anyString = anyString.toUpperCase();
    return anyString;
}

var capitalizeArrow = anyString => anyString.toUpperCase();

console.log(capitalizeExpression(greeting));
console.log(capitalizeFunction(greeting));
console.log(capitalizeArrow(greeting));

var numArray = [1,2,3,4,5,6,7,8,9]

function evenNumbers(arr){
    for (i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 0){
            console.log(arr[i]);
        }
    }
}
evenNumbers(numArray);
var numArray = [1,2,3,4,5,6,7,8,9]

function oddNumbers(arr){
    for (i = 0; i < arr.length; i++){
        if(arr[i] % 2 !== 0){
            console.log(arr[i]);
        }
    }
}
oddNumbers(numArray);  

//Generating Random Numbers.
function randomInt(min, max){
    let numOfValues = max - min + 1;
    let randomNum = Math.random();
    let randomVal = randomNum * numOfValues;
    
    console.log(randomVal);
}
randomInt(5, 10);
*/