# tips
## 基礎
### this (basic_test/this_test.js)
- thisを呼び出す際の、呼び出す場所によってwindowオブジェクトか、自身のオブジェクトを指すかが分かれる

### アロー関数
- https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Functions/Arrow_functions
- 関数内でアロー関数を定義し、そのなかでthisを呼び出すと、自身のオブジェクトを指す

```
  let normalFn;
  normalFn = {
      id: 43,
      counter: function(){
          console.log(this);
          setTimeout(() => {
              // この場合のthisは、normalFn objを指す
              console.log(this);
          }, 1000)
      }
  }
  normalFn.counter();
```


```
  let normalFn;
  normalFn = {
      id: 43,
      counter: function(){
          console.log(this);
          setTimeout( function() {
              // この場合のthisは、window objを指す
              console.log(this);
          }, 1000)
      }
  }
  normalFn.counter();
```

### クロージャ関数
- クロージャは、関数とその関数が宣言されたレキシカルスコープの組み合わせ
- 柔軟に関数を定義することができる
- private変数を使うときはクロージャ関数を使うと良い

```
function addStringFactory(tail){
    return function concat(str){
        return str + tail;
    }
}

let addAs = addStringFactory('AAAAA');
let addBs = addStringFactory('BBBBB');

let str = 'Tom'
str = addAs(str);
console.log(str); // TomAAAAA
```

### スプレッド構文
- 配列をそのまま渡せる
```
function sum(x, y, z){
    return x + y + z;
}

console.log(sum(1, 2, 3)); // 6

const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6

// 一昔前は、applyを使って書いていた
console.log(sum.apply(null, numbers)); // 6
```

- メリット①簡単に、配列結合ができる、追加も。
```
let arr1 = [0, 1, 2];
let arr2 = [3, 4, 5];
arr3 = arr1.concat(arr2);
// 配列の結合もconcatせずにできる
arr4 = [...arr1, ...arr2];
// 配列の結合時、追加も簡単にできる
arr5 = [...arr1, 10, ...arr2];
console.log(arr5);
```

