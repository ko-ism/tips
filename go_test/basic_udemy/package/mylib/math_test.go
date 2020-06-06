package mylib

import (
	"fmt"
	"testing"
)

var Debug bool = true

func ExampleAverage() {
	v := Average([]int{1, 2, 3, 4, 5})
	fmt.Println(v)
}

func TestAverage(t *testing.T) {
	v := Average([]int{1, 2, 3, 4, 5})
	if v != 3 {
		t.Error("Expected 3, got", v)
	}
}

func ExamplePerson2_Say() {
	p := Person2{Name: "Mike", Age: 20}
	fmt.Println(p)
}
