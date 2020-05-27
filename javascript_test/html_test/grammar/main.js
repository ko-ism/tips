/**  array test */

// let hello = 'Hello World'
// console.log(hello.substr(0,5));

// let arry = [1, 2, 3, 4, 5, 'moji', false];
// // 先頭へ値格納
// // Array(8) ["new item", 1, 2, 3, 4, 5, "moji", false]
// arry.unshift('new item');
// console.log(arry);

// // 最後の値取り出し、削除
// let val = arry.pop();
// // Array(7) ["new item", 1, 2, 3, 4, 5, "moji"]
// console.log(arry);
// // false
// console.log(val);

// // 最初の値取り出し、削除
// val = arry.shift();
// // Array(6) [1, 2, 3, 4, 5, "moji"]
// console.log(arry);
// // "new item"
// console.log(val);


/** callback test */
// // 関数を変数として定義することができるのがjavascriptならでは

// const hello = (callback) => {
//     console.log('hello ' + callback());
// }

// const getName = () => {
//     return 'shinya koizumi'
// }

// // getName()としてしまうとgetName()の実行結果である'shinya koizumi' が代入されてしまいエラーとなる
// // getNameとすることで関数を代入することができる
// hello(getName);



/** forEach test */
// let arry = [1, 2, 3, 4, 5];

// // for文よりforEachの方が使われる。簡単にかけるため。
// // 第一引数には値、第二引数はindex番号、第三引数にはarrayすべてが入ってくる
// arry.forEach((val, index, arr) => {
//     console.log(val, index, arr)
// });



/** reduce test */
// reduceメソッドは、arrayを一つずつ処理して結果をaccuに格納、それを繰り返す
const str = 'animation';
const strArray = str.split('');
function tag(accu, curr) {
    // console.log(accu, curr);
    return `${accu}<${curr}>`
}

function reduce(arry, callback, defaultValue) {
    let accu = defaultValue;
    for (let i = 0; i < arry.length; i++){
        let curr = arry[i];
        accu = callback(accu, curr);
    }
    return accu;
}

const result = reduce(strArray, tag, "");
console.log(result);