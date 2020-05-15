console.log('%c [JavaScript]ループを使いこなそう', 'color:red; font-size:1.5em');

const data = [1, 4, 2, 5];
const fruits = {banana: 'バナナ', apple: 'リンゴ', orange: 'オレンジ'}

// Object.prototype.additionalFn = function(){};

// for(let i = 0; i < data.length; i++){
//     console.log(i, data[i]);
// }

// let keyFruits = Object.keys(fruits);
// console.log(keyFruits);

// for(let i = 0; i < keyFruits.length; i++){
//     console.log(i, fruits[keyFruits[i]]);
// }


// for(let i in data){
//     console.log(i, data[i]);
// }

// // この場合、additionalFn、function()などのプロパティもループしてしまう
// for(let i in fruits){
//     console.log(i, fruits[i]);
// }

// // 回避としては一般的に以下のように書く
// for(let i in fruits){
//     if(fruits.hasOwnProperty(i)){
//         console.log(i, fruits[i]);
//     }
// }

// // for inがkeyをiに格納していたが、
// // for ofはvalueをiに格納する
// 辞書オブジェクト
// let keyFruits = Object.keys(fruits);
// for(let i of keyFruits){
//     console.log(i, fruits[i]);
// }

// let keyFruits = Object.keys(fruits);
// for(let i of keyFruits){
//     console.log(i, fruits[i]);
// }

// let valueFruits = Object.values(fruits);
// for(let i of valueFruits){
//     console.log(i);
// }


// let keyFruits = Object.entries(fruits);
// for(let [k, v] of keyFruits){
//     console.log(k, v);
// }


// data.forEach((value, index, array) => {
//     console.log(value, index, array);
// });

// const newData = data.map((value, index, array) => {
//     return value * 2;
// });
// console.log(data);
// console.log(newData);

// // filter は、条件にマッチしたデータだけ、戻す。
// const newData = data.filter((value, index, array) => {
//     return value == 1;
// });
// console.log(data); // Array(4) [1, 4, 2, 5]
// console.log(newData); // Array(1) [1]


// reduceは、returnの値をaccuに戻す場合に使う。
// 文字列を結合するときとかに使う。それ以外に使い様。
// const newData = data.reduce((accu, curr) => {
//     console.log(accu, curr);
//     return accu + curr;
// });
// console.log(data); // Array(4) [1, 4, 2, 5]
// console.log(newData); // 12

// // ソートする。元の配列の順序も変わることに注意。
// const newData = data.sort((a, b) => {
//     console.log(a, b);
//     return a - b;// 昇順
//     // return b - a;// 降順
// });
// console.log(data); // Array(4) [1, 2, 4, 5]
// console.log(newData); // Array(4) [1, 2, 4, 5]

const newData = data
.map(v => v+1)
.sort((a, b) => {
    return a - b;
});
console.log(data); // Array(4) [1, 2, 4, 5]
console.log(newData); // Array(4) [2, 3, 5, 6]
