package main

import "fmt"
func main(){

//STATIC TYPE DECLARATION IN GO.

	/* var x float64
	x = 20.0
	fmt.Println(x)
//By adding "%T" to the code, the type of the variable will be printed. 
//And "Printf" in this format is a most for correct results.
	fmt.Printf("x is of type %T\n", x) */

//DYNAMIC TYPE DECLARATION OR TYPE INFERENCE IN GO.

	/* var x float64 = 20.0
//Notice in case of type inference, we initialized the variable "y" with ":=" operator. Because it is not declared under "var". 
//This is because it is not declared explicitly like "x" variable.
//And for us to get our "type" printed, we must put a comma "," before "x or y" after our double quote string.
	var y = 42
	fmt.Println(x)
	fmt.Println(y)
	fmt.Printf("x is of type %T\n", x)
	fmt.Printf("y is of type %T\n", y) */

//MIXED VARIABLE DECLARATION IN GO.

//Notice our arrangement of declaration, list your variables, then you start initializing them from the last variable, respectively.
	/* var a, b, c = 3, 4, "foo"

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Printf("a is of type %T\n", a)
	fmt.Printf("b is of type %T\n", b)
	fmt.Printf("c is of type %T\n", c) */

//USING "const" KEYWORD. (const variable type = value), format.

//Note that it is a good programming practice to define constants in CAPITALS
	/* const LENGTH int = 10
	const WIDTH int = 5
	var area int

	area = LENGTH * WIDTH
//We use "%d" in the printing in order to get our result displayed correctly. That is for returning a value. 
//That is, if we want to print a value that was computed and stored.  
	fmt.Printf("value of area: %d", area)
 */

//ARITHMETIC OPERATORS.

/* var a int = 21
var b int = 10
var c int

//Every statement uses the formula before it for computation.
c = a + b
	fmt.Printf("Line 1 - Value of c is %d\n", c)
c = a - b
	fmt.Printf("Line 2 - Value of c is %d\n", c)
c = a * b
	fmt.Printf("Line 3 - Value of c is %d\n", c)
c = a / b
	fmt.Printf("Line 4 - Value of c is %d\n", c)
c = a % b 
	fmt.Printf("Line 5 - Value of c is %d\n", c)
a++
	fmt.Printf("Line 6 - Value of a is %d\n", a)
//The "a--" here uses the result of "a++" as its value for the computation.
a--
	fmt.Printf("Line 7 - Value of a is %d\n", a) */

//RELATIONAL OPERATORS.

/* var a int = 21
var b int = 10

if ( a == b ){
	fmt.Printf("Line 1 - a is equal to b\n")
} else {
	fmt.Printf("Line 1 - a is not equal to b\n")
}
if ( a < b ){
	fmt.Printf("Line 2 - a is less than b\n")
} else {
	fmt.Printf("Line 2 - a is not less than b\n")
}
if ( a > b ){
	fmt.Printf("Line 3 - a is greater than b\n")
} else {
	fmt.Printf("Line 3 - a is not greater than b\n")
}
//Let us change value of "a" and "b".
a = 5
b = 20
if ( a <= b){
	fmt.Printf("Line 4 - a is either less than or equal to b\n")
}
if ( b >= a){
	fmt.Printf("Line 5 - b is either greater than or equal to a\n")
} */

//LOGICAL OPERATORS.

/* var a bool = true
var b bool = false

if ( a && b ){
	fmt.Printf("Line 1 - Condition is true\n")
}
if ( a || b ){
	fmt.Printf("Line 2 - Condition is true\n")
}
//Let us change the value of "a" and "b".
a = false
b = true
if ( a && b ){
	fmt.Printf("Line 3 - Condition is true\n")
} else {
	fmt.Printf("Line 3 - Condition is not true\n")
}
if ( !(a && b) ){
	fmt.Printf("Line 4 - Condition is true\n")

} */

//BITWISE OPERATORS.

/* var a uint = 60 	// 60 = 0011 1100
var b uint = 13 	// 13 = 0000 1101
var c uint = 0

c = a & b	// 12 = 0000 1100
	fmt.Printf("Line 1 - Value of c is %d\n", c)

c = a | b	// 61 = 0011 1101
	fmt.Printf("Line 2 - Value of c is %d\n", c)

c = a ^ b	// 49 = 0011 0001
	fmt.Printf("Line 3 - Value of c is %d\n", c)

c = a << 2	// 240 = 1111 0000
	fmt.Printf("Line 4 - Value of c is %d\n", c)

c = a >> 2	// 15 0000 1111
	fmt.Printf("Line 5 - Value of c is %d\n", c) */

//ASSIGNMENT OPERATORS.

/* var a int = 21
var c int

c = a 
	fmt.Printf("Line 1 - = Operator Example, Value of c = %d\n", c)

c += a
	fmt.Printf("Line 2 - += Operator Example, Value of c = %d\n", c)

c -= a
	fmt.Printf("Line 3 - -= Operator Example, Value of c = %d\n", c)

c *= a
	fmt.Printf("Line 4 - *= Operator Example, Value of c = %d\n", c)

c /= a 
	fmt.Printf("Line 5 - /= Operator Example, Value of c = %d\n", c)

c = 200

c <<= 2
	fmt.Printf("Line 6 - <<= Operator Example, Value of c = %d\n", c)

c >>= 2 
fmt.Printf("Line 7 - >>= Operator Example, Value of c = %d\n", c)

c &= 2
	fmt.Printf("Line 8 - &= Operator Example, Value of c = %d\n", c)

c ^= 2
	fmt.Printf("Line 9 - ^= Operator Example, Value of c = %d\n", c)

c |= 2
	fmt.Printf("Line 10 - |= Operator Example, Value of c = %d\n", c) */

//MISCELLANEOUS OPERATORS.

/* var a int = 4
var b int32
var c float32
var ptr *int

//Example of type operator.
fmt.Printf("Line 1 - Type of variable a = %T\n", a)
fmt.Printf("Line 2 - Type of variable b = %T\n", b)
fmt.Printf("Line 3 - Type of variable c = %T\n", c)

//Example of "&" and "*" operators. "&" operator provides actual address of a variable attached.
//And "*" provides pointer to the variable.
ptr = &a	// "ptr" now contains the address of "a".
fmt.Printf("Value of a is %d\n", a)
fmt.Printf("*ptr is %d.\n", *ptr) */

//OPERATORS PRECEDENCE.

var a int = 20
var b int = 10
var c int = 15
var d int = 5
var e int;

e = ( a + b ) * c / d;	// ( 30 * 15 ) / 5
	fmt.Printf("Value of ( a + b ) * c / d is : %d\n", e)

e = (( a + b ) * c ) / d;	// ( 30 * 15 ) / 5
	fmt.Printf("Value of (( a + b ) * c) / d is : %d\n", e)

e = ( a + b ) * ( c / d)	// (30) * (15/5)
	fmt.Printf("Value of ( a + b ) * ( c / d ) is : %d\n", e)

e = a + ( b * c ) / d	// 20 + (150/5)
	fmt.Printf("Value of a + ( b * c ) / d is : %d\n", e)

}
