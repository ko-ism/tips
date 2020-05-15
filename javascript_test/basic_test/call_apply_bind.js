// let myObj = {
//     id: 42,
//     print() {
//         // このthisはobjを指す
//         console.log(this);
//         // windows.setTimeoutがwindowから呼び出しているから
//         setTimeout(function() {
//             // このthisは、window objとなる
//             console.log(this)
//         }, 1000)
//     }
// }

// myObj.print();


// // もし、setTimeout内でthisをwindow objにしない方法
// let myObj = {
//     id: 42,
//     print() {
//         // このthisはobjを指す
//         console.log(this);
//         // bindするとthisが、objをさせるようにできる
//         setTimeout(function() {
//             // このthisは、myObjとなる
//             console.log(this)
//         }.bind(this), 1000)
//     }
// }

// myObj.print();




// // もし、setTimeout内でthisをwindow objにしない方法2
// let myObj = {
//     id: 42,
//     print() {
//         // このthisはobjを指す
//         console.log(this);
//         // アロー関数にすると
//         setTimeout(() => {
//             // このthisは、myObjとなる
//             console.log(this)
//         }, 1000)
//     }
// }

// myObj.print();




// もし、setTimeout内でthisをwindow objにしない方法3
// よく使う手法
let myObj = {
    id: 42,
    print() {
        // このthisはobjを指す
        console.log(this);
        let _that = this;
        // アロー関数にすると
        setTimeout( function() {
            // この_thatはthisと同じで、myObjとなる
            console.log(_that)
        }, 1000)
    }
}

myObj.print();