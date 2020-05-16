class Person {
    constructor(first, last){
        this.first = first;
        this.last = last;
    }
    introduce(){
        console.log('My name is ' + this.first + this.last);
    };
}

class Japanese extends Person{
    constructor(first, last){
        super(first, last);
        this.lang = 'ja';
        this._age = 0;
    }

    sayJapanese(){
        console.log('こんにちは ' + this.first + this.last);
    };

    static sayHello(value){
        console.log('こんにちは ' + value);
    }

    set age(value){
        this._age = value;
    }

    get age(){
        return this._age;
    }
}

let me = new Person('First', 'Last');
me.introduce();

// 継承
let me2 = new Japanese('Japanese', 'Name');
me2.introduce();
me2.sayJapanese();

// static呼び出し
Japanese.sayHello("TEST");

// get/set
console.log(me2.age);
me2.age = 10;
console.log(me2.age);


// // ES2019におけるクラスの書き方
// // 以下のように、プライベート変数を#を使って定義可能。
// // これまでは_versionなどアンダースコアを入れて、明示的にプライベート変数であることをアピールしていたが、制限がかかっていたわけではない。
// class ES2019{
//     #version = '1.0.0'

//     printVersion(){
//         console.log('this version is ' + this.#version);
//     }
// };

// cl = new ES2019();
// cl.printVersion();