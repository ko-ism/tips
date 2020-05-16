// // callback

// function wait(callback, num){
//     setTimeout(() => {
//         console.log(num);
//         callback(num);
//     }, num)
// }

// wait(() => {
//     console.log('callback function is called');
// }, 1000)

// // Promise
// function wait2(num){
//     return new Promise((resolve, reject) =>{
//         setTimeout(() => {
//             console.log(num);
//             if (num ==1002){
//                 reject(num);
//             }else{
//                 resolve(num);
//             }
//         }, num);
//     });
// }

// wait2(1000).then((num) =>{
//     num++;
//     console.log('promise function is called');
//     return wait2(num);
// }).then((num) =>{
//     num++;
//     console.log('promise function is called');
//     return wait2(num);
// }).then((num) =>{
//     num++;
//     console.log('promise function is called');
//     return wait2(num);
// })


// Promise.all([wait2(100), wait2(1500), wait2(2000)]).then((nums) => {
//     console.log(nums);
// });

// Promise.race([wait2(100), wait2(1500), wait2(2000)]).then((nums) => {
//     console.log(nums+1);
// });


// await-async

function wait3(num){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            console.log(num);
            if (num ==2){
                reject(num);
            }else{
                resolve(num);
            }
        }, num);
    });
}

async function init(){
    let num = 0;
    try {
        num = await wait3(num);
        num++;
        num = await wait3(num);
        num++;
        // num = await wait3(num);
        // num++;
    }catch(e){
        throw new Error('Error is occured', e);
    }

    return num
}

init().then(() => {
    console.log('End');
});