package main

import "fmt"

/* func Hello(name string) string{
//This "%v" is for the value inside the "name", but there are still many letters to use for printing of different values.
	message := fmt.Sprintf("Hi, %v. Welcome!", name)

	return message
} */

//func main(){
	//fmt.Printf(Hello("Calistus")) 

//Pointers; they store the address of a value
/* func foo() *int{
	x := 1
	return &x
}

func main(){
	var y *int
	y = foo()
	fmt.Printf("%d", *y)
} */

//FOR LOOP FORMATS.
/*func main(){
	for i := 0; i < 10; i++{
		fmt.Printf("Hi\n")
	} */

	/* i := 0
	for i < 10 {
		fmt.Printf("Hi\n")
		i++
	} */

//BREAKING A LOOP.
/* i := 0
for i < 10 {
	if i == 5 {
		break
	}
	i++
	fmt.Printf("Hi\n")
} */

//CONTINUING A LOOP. It skips the line the condition was met.
/* i := 0
for i < 10 {
	i++
	if i == 5 {
		continue
	}
	fmt.Printf("Hi\n")
	} */

//SCAN FUNCTION.//Reading for user inputs.

/* var appleNum int
fmt.Printf("Enter number of apples please! \n")

fmt.Scanf("%d", &appleNum)
fmt.Printf("Number of apples = %d", appleNum)
 */

 //Excercise in Introduction to Golang Part 3. Truncation of a floating point number to an integer number. 
 /* var decimalNum float64
 	fmt.Printf("Enter a decimal number please! \n")
 
 	fmt.Scanf("%f", &decimalNum)
 	fmt.Printf("Equivalent integer number for %f = %d", decimalNum, int(decimalNum)) */


 //Excercise in Introduction to Golang Part 3. Conversion of an integer number to a floating point number. 
 /* var integerNum int
 	fmt.Printf("Enter an integer number please! \n")
 
	fmt.Scanf("%d", &integerNum)
//"%f" here is for us to get decimal number, that is a floating point number.
	fmt.Printf("Equivalent floating point number for %d = %f", integerNum, float32(integerNum)) */

//ARRAYS IN GO.

/* var x [5] int
	x[2] = 6
	x[4] = 2
	fmt.Printf("%d\n", x[4]) */

//ARRAY LITERALS.
//Here, you have to state the length of the array.
/* var x [5]int = [5]int {1, 2, 3, 4, 5}

fmt.Printf("%d\n", x[2]) */

//Here, no need to state the length, but this "..." means any length. That is, the number of elements is equal to the length.
/* x := [...]int {1, 2, 3, 4}

fmt.Printf("%d\n", x[3]) */

//ITERATING THROUGH ARRAYS.
//NOTE:"range" returns two values, that is, "Index" and "Element"
//ARRAY 1.

/* var x [5]int = [5]int {1, 2, 3, 4, 5}

for i, v := range x{
	fmt.Printf("Index: %d, Value: %d\n", i, v)
} */

//ITERATING THROUGH ARRAYS.
//ARRAY 2.

/* x := [...]int {1, 2, 3, 4}

for i, v := range x{
	fmt.Printf("Index: %d, Value: %d\n", i, v)
} */

//SLICE.

/* arr := [...]string {"a", "b", "c", "d", "e", "f"}

s1 := arr[1:4]
s2 := arr[2:5]

//NOTE:"%s" here is for string value.
	fmt.Printf("s1 = %s\n", s1)
	fmt.Printf("s2 = %s\n", s2)

s1[2] = "z"

	fmt.Printf("s1 = %s\n", s1)
	fmt.Printf("s2 = %s\n", s2)
	fmt.Printf("arr = %s\n", arr)
 */

//LENGTH AND CAPACITY.

/* arr := [...]string {"a", "b", "c", "d", "e", "f"}

slice1 := arr[1:3]
slice2 := arr[2:5]
//NOTE:Capacity of a slice or an array is the length of the array, and the length of the slice from the start of it in the array. 
	fmt.Printf("slice1 %d, %d\n", len(slice1), cap(slice1))
	fmt.Printf("slice2 %d, %d", len(slice2), cap(slice2)) */

//ACCESSING SLICES.

/*arr := [...]string {"a", "b", "c", "d", "e", "f"}

s1 := arr[1:4]
s2 := arr[2:5]

	fmt.Printf("%s\n", s1[1])
	fmt.Printf("%s\n", s2[2]) 

//SLICE LITERALS.

//Empty square brackets means it is a slice.
slice := []int {1, 2, 3}

fmt.Printf("%d\n", slice[2]) 

//ARRAY FUNCTION "make()".

//Making an array with length equals to capacity with slots to put your values.
slice := make([]int, 10)

slice[2] = 5
fmt.Printf("%d\n", slice[2]) 

//Making an array with length and capacity separately with slots to put your values.
slice := make([]int, 10, 15)

slice[8] = 7
fmt.Printf("%d\n", slice[8]) 

//ARRAY FUNCTION "append()".
//Adding elements to the end of a slice, like push in JavaScript.
slice := make([]int, 0, 3)
slice1 := append(slice, 100, 50, 34, 45, 33)

fmt.Printf("%d\n", slice1[4])
 

//MAPS.
//FORMAT AND HOW TO ACCESS THEM.
//Defining a map literal.
idMap := map[string]int {
	"joe" : 123, "joy" : 113, "john" : 153, "jibrin" : 156}
	
//This prints the whole map
fmt.Println(idMap)

//Returns Zero if key is not present, and returns the value if presents.
fmt.Println(idMap["adam"])

//Adding a key and value pair. Which can be multiple but in defferent lines as you can see below.
idMap["isah"] = 500 
idMap["adamu"] = 560 

//Deleting a key and value pair. Which can be multiple but in defferent lines as you can see below.
delete(idMap, "joy")
delete(idMap, "joe")

//MAP FUNCTIONS.
//Test whether a key exist. "value" is the key value and "presence" is for presence of key which returns Boolean.
value, presence := idMap["Hassan"]
fmt.Println(value, presence)

//"len()" returns number of values in the map.
fmt.Println(len(idMap))

//ITERATING THROUHG A MAP WITH "for" LOOP.
//It lists all the keys and their values in the map.
for key, val := range idMap {
	fmt.Println(key, val)
}*/

//STRUCT. 
//Making your own type.
//Struct Literal
 /* type person struct {
	name string
	address string
	phone int
	city string
	state string
	country string
}
//Accessing Struct Members.
func main(){
	var p1 person
	var p2 person
//p1 specification
p1.name = "Is'haaq" 
p1.address = "437 Dr Halima street"
p1.phone = 8148394765
p1.city = "Zaria"
p1.state = "Kaduna"
p1.country = "Nigeria"

//p2 specification
p2.name = "Daahir"
p2.address = "437 Dr Halima street"
p2.phone = 8148394765
p2.city = "Beijing"
p2.state = "Beijing"
p2.country = "China"

fmt.Printf("Name: %s\nAddress: %s\nPhone: %d\nCity: %s\nState: %s\nCountry: %s\n", p1.name, p1.address, p1.phone, p1.city, p1.state, p1.country)
//This is for an empty line between the two results.
fmt.Println("\n")
fmt.Printf("Name: %s\nAddress: %s\nPhone: %d\nCity: %s\nState: %s\nCountry: %s\n", p2.name, p2.address, p2.phone, p2.city, p2.state, p2.country)
} */
//PASS STRUCT AS FUNCTION ARGUMENT.
//The function to be called.

type person struct {
	name string
	address string
	phone int
	city string
	state string
	country string
}
//Accessing Struct Members.
func main(){
	var p1 person
	var p2 person
//p1 specification
p1.name = "Is'haaq" 
p1.address = "437 Dr Halima street"
p1.phone = 8148394765
p1.city = "Zaria"
p1.state = "Kaduna"
p1.country = "Nigeria"

//p2 specification
p2.name = "Daahir"
p2.address = "437 Dr Halima street"
p2.phone = 8148394765
p2.city = "Beijing"
p2.state = "Beijing"
p2.country = "China"

//Print p1 info. by calling a function.
printPerson(p1)

//Print p2 info. by calling a function.
printPerson(p2)
}
//This is the function to be called, you can either put it before the main function or after but not inside.
func printPerson(pers person) {
	fmt.Printf("Name: %s\nAddress: %s\nPhone: %d\nCity: %s\nState: %s\nCountry: %s\n\n", pers.name, pers.address, pers.phone, pers.city, pers.state, pers.country)
}