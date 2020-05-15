/**
 * クロージャ
 */

// // globalで定義する場合は、値を直接修正できてしまう
// counter = 0;
// function increment(){
//     counter++;
//     console.log(counter);
// }
// increment(); // 1
// counter = 0
// increment(); // 2
// increment(); // 3

// こうすることで、外部からcounterへアクセスできない
let increment = (function() {
    let counter = 0; // Lexical Scope

    return function () {
        counter += 1;
        console.log(counter)
    }
})();

increment(); // 1
increment(); // 2
increment(); // 3

// 上記とは別物が定義された、という扱い
increment.counter = 10;

increment(); // 4





// function addStringFactory(tail){
//     function concat(str){
//         return str + tail;
//     }
//     return concat;
// }

// もしくは

function addStringFactory(tail){
    return function concat(str){
        return str + tail;
    }
}

let addAs = addStringFactory('AAAAA');
let addBs = addStringFactory('BBBBB');

let str = 'Tom'
str = addAs(str);
console.log(str);