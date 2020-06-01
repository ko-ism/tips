package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("Hello World")
	fmt.Println("Hello " + "World")
	fmt.Println(string("Hello World"[0]))
	fmt.Println("Hello World"[0])
	var s string = "Hello World"

	s = strings.Replace(s, "o", "O", 2)
	fmt.Println(s)
	fmt.Println(strings.Contains(s, "World"))

	fmt.Println(`Test
                       Test
Test`)

	fmt.Println("\"")
	fmt.Println(`"`)
}
