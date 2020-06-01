package main

import "fmt"

func main() {
	// Q1
	l := []int{100, 300, 23, 11, 23, 2, 4, 6, 4}
	var ans1 int
	for _, v := range l {
		if v > ans1 {
			ans1 = v
		}
	}
	fmt.Println(ans1)

	// Q2
	m := map[string]int{
		"apple":  200,
		"banana": 300,
		"grapes": 150,
		"orange": 80,
		"papaya": 500,
		"kiwi":   90,
	}
	var ans2 int
	for _, v := range m {
		ans2 += v
	}
	fmt.Println(ans2)
}
