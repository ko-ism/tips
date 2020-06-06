/*
Package mylib is my special lib.
*/
package mylib

import "fmt"

// Person2 doc
type Person2 struct {
	// Name
	Name string
	// Age
	Age int
}

// Say is say method of Person2
func (p *Person2) Say() {
	fmt.Println("Person2")
}

// Average return the average of a series of numbers
func Average(s []int) int {
	total := 0
	for _, i := range s {
		total += i
	}
	return int(total / len(s))
}
