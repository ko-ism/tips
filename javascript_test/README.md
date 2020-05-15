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

- メリット②辞書も適用できる
```
let obj1 = { foo: 'bar', x:42};
let obj2 = { foo: 'baz', y:13};
let clonedObj = { ...obj1 };
let mergedObj = { ...obj1, ...obj2 };
console.log(clonedObj); // Object {foo: "bar", x: 42}
console.log(mergedObj); // Object {foo: "baz", x: 42, y: 13}
```

- Rest Parametersとしての利用
```
// Rest Parameters
function sum(...theArgs){
    return theArgs.reduce((previous, current) => {
        return previous + current;
    })
}
console.log(sum(1,2,3)); // 6

function f(a, ...args){
    console.log(args);
}

f(1, 2, 3); // Array(2) [2, 3]
```

### 分割代入、代入色々
```
[a, b, ...rest] = [10, 20, 30, 40, 50];
console.log(a); // 10
console.log(b); // 20
console.log(rest); //Array(3) [30, 40, 50]

[a ,, b, c=1] = [10, 20, 30];
console.log(a); // 10
console.log(b); // 30
console.log(c); // 1 四番目の配列はないが、初期値を1と設定しているため1となる

// 辞書形式も同様
const {b, a:aa, ...rest} = {a: 10, b: 20, c: 30, d: 40};
console.log(aa); // 10
console.log(b); // 20
console.log(rest); // Object {c: 30, d: 40}

// 関数を引数に取ると効果的
function drawES2015Chart({size = 'big', coords = {x:0, y:0}, radius = 25} = {}){
    console.log(size, coords, radius);
}

drawES2015Chart(); // 上記、初期値{}で実行される

drawES2015Chart({
    coords: {x: 18, y: 30},
    radius: 30
}); // big, Object {x: 18, y: 30}, 30
```
### タグ付きテンプレートリテラル
- ダブルクォートやシングルクォート（""や''）ではなく、``` `` ```で括ると変数を組み込める
