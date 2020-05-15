/** 
 * スプレッド構文を使いこなす
 * Pythonの*argと同じかな
 */

// function sum(x, y, z){
//     return x + y + z;
// }
// console.log(sum(1, 2, 3));
// const numbers = [1, 2, 3];
// console.log(sum(...numbers));
// // 一昔前は、applyを使って書いていた
// console.log(sum.apply(null, numbers));


// // 様々なスプレッド構文のメリット(結合)
// let arr1 = [0, 1, 2];
// let arr2 = [3, 4, 5];
// arr3 = arr1.concat(arr2);
// // 配列の結合もconcatせずにできる
// arr4 = [...arr1, ...arr2];
// // 配列の結合時、追加も簡単にできる
// arr5 = [...arr1, 10, ...arr2];
// console.log(arr5);


// // 辞書での利用
// let obj1 = { foo: 'bar', x:42};
// let obj2 = { foo: 'baz', y:13};
// let clonedObj = { ...obj1 };
// let mergedObj = { ...obj1, ...obj2 };
// console.log(clonedObj); // Object {foo: "bar", x: 42}
// console.log(mergedObj); // Object {foo: "baz", x: 42, y: 13}


// // 参照のコピー
// let a = [[1], [2], [3]];
// let b = [...a];
// // shift()は、最初の配列を削除する
// console.log(b.shift().shift()); // 1
// console.log(b); // Array(2) [Array(1), Array(1)]
// console.log(a); // Array(3) [Array(0), Array(1), Array(1)]


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