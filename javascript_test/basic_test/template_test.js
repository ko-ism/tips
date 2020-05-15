console.log('%c [JavaScript]タグ付きテンプレートリテラルを使ってみよう', 'color:red; font-size:1.5em');

// ダブルクォートやシングルクォート（""や''）ではなく、変数を組み込める
// let name = 'Tom'
// let str = `Hello\n${name}`;
// console.log(str); // Hello<改行>Tom

// let name = 'Tom'
// let str = `Hello\
//     ${name}`;
// console.log(str); //Hello    Tom

// 文字列の整形をしてreturnするのに使う
function b(strings, ...values){
    console.log(strings);
    console.log(values);
    return strings.reduce((accu, str, i) => {
        let val = values[i] ? `<b>${values[i]}</b>` : "";
        return `${accu}${str}${val}`;
    }, '');
}

const str1 = "Bob";
const str2 = "Tom";
let result = b`${str1} and ${str2}`;
console.log(result);
result = `${str1} and ${str2}`;
console.log(result);