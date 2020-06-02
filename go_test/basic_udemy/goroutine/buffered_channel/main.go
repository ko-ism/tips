package main

import "fmt"

func main() {
	ch := make(chan int, 2)
	ch <- 100
	fmt.Println(len(ch))
	ch <- 200
	fmt.Println(len(ch))
	// ちゃんとクローズする処理をすれば、後続のrangeでエラーが発生しない
	close(ch)

	for c := range ch {
		fmt.Println(c)
	}

}
