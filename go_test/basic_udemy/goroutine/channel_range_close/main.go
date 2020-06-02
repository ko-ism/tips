package main

import "fmt"

func goroutine1(s []int, c chan int) {
	defer close(c)
	sum := 0
	for _, v := range s {
		sum += v
		// これで途中経過のデータのやり取りも渡せる
		c <- sum
	}

}

func main() {
	s := []int{1, 2, 3, 4, 5}
	c := make(chan int, 1) // この場合、チャネルはlen(s)でなくて一つでいいかな
	go goroutine1(s, c)
	for i := range c {
		fmt.Println(i)
	}
}
