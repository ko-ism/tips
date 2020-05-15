console.log('%c [JavaScript]アロー関数について学ぼう', 'color:red; font-size:1.5em');
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Functions/Arrow_functions

// function timesTwo(i){
//     return i*2;
// }

// const timesTwo = (i) => {
//     return i*2;
// }

// 1行のコードであれば、｛｝も不要。returnも記載不要。
const timesTwo = (i) => i*2;

const res = timesTwo(2);
console.log(res);

/**
 * 書き方（シンタックス）について
 */

 let arrowFn;
 arrowFn = () => 42;
 arrowFn = x => 42;
 arrowFn = (x) => 42;
 arrowFn = (x, y) => 42;
 arrowFn = (x, y) => {
     console.log(x, y);
     return x + y;
 };
 


 /** 
  * アロー関数内の、thisのバインドについて
  */

//   let normalFn;
//   normalFn = {
//       id: 43,
//       counter: function(){
//           console.log(this);
//           setTimeout(() => {
//               console.log(this);
//           }, 1000)
//       }
//   }
//   normalFn.counter();


// me = 'global'
// const outer = function(){
//     let me = 'outer'; // lexical scope
//     return {
//         me: 'inner',
//         say: () => {
//             // 出力はglobalになる
//             console.log(this.me);
//         }
//     }
// }
// outer().say();


me = 'global'
const outer = function(){
    let me = 'outer'; // lexical scope

    return {
        me: 'inner',
        say: function() {
            // 出力はinnerになる
            console.log(this.me);
        }
    }
}

outer().say();