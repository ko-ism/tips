package main

import "fmt"

func conv() {
	f := 1.11
	fmt.Println(int(f))
}

func createMap() {
	m := map[string]int{"Mike": 20, "Nancy": 24, "Messi": 30}
	fmt.Printf("%T %v", m, m)
}

func main() {
	conv()
	createMap()
}
