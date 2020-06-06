package main

import (
	"fmt"
	"mylib"
	"mylib/under"
)

func main() {
	s := []int{1, 2, 3, 4, 5}
	result := mylib.Average(s)
	fmt.Println(result)

	mylib.Say()
	under.Hello()

	person := mylib.Person{Name: "Mike", Age: 20}
	fmt.Println(person)
}
