package main

import (
	"fmt"
	"os/user"
	"time"
)

func main() {
	fmt.Println("hello ", time.Now())
	fmt.Print(user.Current())
}
