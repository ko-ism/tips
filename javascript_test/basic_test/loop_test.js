console.log('%c [JavaScript]ループを使いこなそう', 'color:red; font-size:1.5em');

const data = [1, 4, 2, 5];
const fruits = {banana: 'バナナ', apple: 'リンゴ', orange: 'オレンジ'}

Object.prototype.additionalFn = function(){};

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

// 回避としては一般的に以下のように書く
for(let i in fruits){
    if(fruits.hasOwnProperty(i)){
        console.log(i, fruits[i]);
    }
}
