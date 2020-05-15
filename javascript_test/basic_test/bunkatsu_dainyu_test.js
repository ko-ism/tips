// let a, b, rest;
// [a, b] = [10, 20];
// console.log(a);
// console.log(b);

// [a, b, ...rest] = [10, 20, 30, 40, 50];
// console.log(a); // 10
// console.log(b); // 20
// console.log(rest); //Array(3) [30, 40, 50]

// [a] = [10, 20, 30, 40, 50];
// console.log(a); // 10

// [a, b] = [10, 20, 30, 40, 50];
// console.log(a); // 10
// console.log(b); // 20

// [a,,b ] = [10, 20, 30, 40, 50];
// console.log(a); // 10
// console.log(b); // 30


// [a ,, b, c=1] = [10, 20, 30];
// console.log(a); // 10
// console.log(b); // 30
// console.log(c); // 1 四番目の配列はないが、初期値を1と設定しているため1となる


// // 辞書形式も同様
// const {b, a:aa, ...rest} = {a: 10, b: 20, c: 30, d: 40};
// console.log(aa); // 10
// console.log(b); // 20
// console.log(rest); // Object {c: 30, d: 40}


// 関数を引数に取ると効果的
function drawES2015Chart({size = 'big', coords = {x:0, y:0}, radius = 25} = {}){
    console.log(size, coords, radius);
}

drawES2015Chart(); // 上記、初期値{}で実行される

drawES2015Chart({
    coords: {x: 18, y: 30},
    radius: 30
}); // big, Object {x: 18, y: 30}, 30



