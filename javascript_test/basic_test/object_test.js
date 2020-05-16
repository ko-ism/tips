// // {}で作られたものをオブジェクト。辞書型配列。
// let obj = {}
// obj.name = 'Tom'
// console.log(obj);
// obj.arry = ['1', 100]; 
// console.log(obj);
// let array = new Array();

// // コンストラクタ関数
// function Person(fist, last){
//     this.first = first;
//     this.last = last;
// }
// let me = new Person('First', 'Last');

// // Personコンストラクタを作る
// function Person(first, last){
//     this.first = first;
//     this.last = last;
//     this.introduce = function(){
//         console.log('My name is '+ first + last);
//     }
// }
// let me = new Person('First', 'Last');
// me.introduce();


function Person(first, last){
    this.first = first;
    this.last = last;
};

let me = new Person('First', 'Last');
// プロトタイプを利用してコンストラクタ定義をすることが多い
Person.prototype.introduce = function(){
    console.log('My name is ' + this.first + this.last);
};
me.introduce();


// 継承
function Japanese(first, last){
    // Personをcallしてbindする
    Person.call(this, first, last);
    this.lang = 'ja'
}
Object.setPrototypeOf(Japanese.prototype, Person.prototype);
Japanese.prototype.say_japanese = function(){
    console.log('こんにちは ' + this.first + this.last);
};

let me2 = new Japanese('Japanese', 'Name');
me2.introduce();
me2.say_japanese();