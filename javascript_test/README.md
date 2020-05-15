# tips
## 基礎
- Udemy講座：JavaScriptの動作を論理的に解説！JavaScript中級者への道　
- https://nttcsol.udemy.com/course/road-to-javascript-master/learn/lecture/16596662

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

### ループ
- 一般的なループ記法
```
for(let i = 0; i < keyFruits.length; i++){
    console.log(i, fruits[keyFruits[i]]);
}
```
- for inの記法もできるが、hasOwnPropertyを利用しないと、必要のないプロパティもループ処理されてしまう
```
const fruits = {banana: 'バナナ', apple: 'リンゴ', orange: 'オレンジ'}
for(let i in fruits){
    if(fruits.hasOwnProperty(i)){
        console.log(i, fruits[i]);
    }
}
```
- for ofにより、valueを取ってくることができる
- Object.keys(<オブジェクト>)により、キーを格納することができる
- Object.values(<オブジェクト>)により、バリューを格納することができる
- ES8から、Object.entries(<オブジェクト>)で、キーバリューの配列を取得することができる
  - entriesを使ったfor ofでのループは今後使われることになる
  
```
const fruits = {banana: 'バナナ', apple: 'リンゴ', orange: 'オレンジ'}
let keyFruits = Object.entries(fruits);
for(let [k, v] of keyFruits){
    console.log(k, v);
}
```

- forEach / mapで繰り返し処理
  - mapであれば、値を加工する際に使う
  - callback
```
const data = [1, 4, 2, 5];
// data.forEach((value, index, array) => {
//     console.log(value, index, array);
// });

const newData = data.map((value, index, array) => {
    return value * 2;
});
console.log(data);
console.log(newData);
```

- map/filter/reduce/sortなど高階関数を使うと、メソッドチェーンをして、処理を繋げることができ、便利。
  - mapなら新しい配列を作りたいのだということが分かるし、filterも特定条件に絞りたいこともわかる
    - 要は、何をしたいかが、その処理内容含め、端的でわかりやすくなる効果もある。
    - forやforEachは、なんでもできるがゆえに、同じ処理なら理解に少し時間を要することが多い
    - forEach使う前に、map/filter/reduce/sortなどでできないかを考えること
  - 関数を引数、戻り値として扱う関数
  - [JavaScript で forEach を使うのは最終手段](https://qiita.com/diescake/items/70d9b0cbd4e3d5cc6fce)
  
```
// map
const newData = data.map((value, index, array) => {
    return value * 2;
});
console.log(data); //Array(4) [1, 4, 2, 5]
console.log(newData); //Array(4) [2, 8, 4, 10]

// filter は、条件にマッチしたデータだけ、戻す。
const newData = data.filter((value, index, array) => {
    return value == 1;
});
console.log(data); // Array(4) [1, 4, 2, 5]
console.log(newData); // Array(1) [1]


// reduceは、returnの値をaccuに戻す場合に使う。
// 文字列を結合するときとかに使う。それ以外に使い様。
const newData = data.reduce((accu, curr) => {
    console.log(accu, curr);
    return accu + curr;
});
console.log(data); // Array(4) [1, 4, 2, 5]
console.log(newData); // 12

// ソートする。元の配列の順序も変わることに注意。
const newData = data.sort((a, b) => {
    console.log(a, b);
    return a - b;// 昇順
    // return b - a;// 降順
});
console.log(data); // Array(4) [1, 4, 2, 5]
console.log(newData); // Array(1) [1]
```


```
const newData = data
.map(v => v+1)
.sort((a, b) => {
    return a - b;
});
console.log(data); // Array(4) [1, 2, 4, 5]
console.log(newData); // Array(4) [2, 3, 5, 6]
```

### 非同期処理
#### callback
- 見づらい
#### Promise
- thenメソッドでPromiseを繋げる場合は、return でPromiseを返す必要がある

```
// Promise
function wait2(num){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            console.log(num);
            if (num ==1002){
                reject(num);
            }else{
                resolve(num);
            }
        }, num);
    });
}

wait2(1000).then((num) =>{
    return wait2(num);
}).then((num) =>{
    return wait2(num);
}).then((num) =>{
    return wait2(num);
})
```

```
// Promise.allメソッドで、すべてのPromiseメソッドが終わった後に、実行される
// 下記Promiseメソッド(wait2)は、非同期に並列で処理される
Promise.all([wait2(100), wait2(1500), wait2(2000)]).then((nums) => {
    console.log(nums);
});

// Promise.raceメソッドは、実行するどれか一つのPromise処理が終わったら実行される
// けっかとして返ってくるnumsは、処理が終わった結果であり、以下だとnums==100となる。
Promise.race([wait2(100), wait2(1500), wait2(2000)]).then((nums) => {
    console.log(nums+1); // 101
});
```


#### 
