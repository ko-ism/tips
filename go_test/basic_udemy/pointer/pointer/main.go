package main

import "fmt"

func one(x *int) {
	*x = 1
}

func main() {
	var n int = 100
	fmt.Println(n)   // 100
	fmt.Println(&n)  // 0xc0000140a8
	fmt.Println(*&n) // 100

	one(&n)
	fmt.Println(n)

	fmt.Println(&n)

	var p *int = &n

	fmt.Println(p)

	fmt.Println(*p)
}
