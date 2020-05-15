// let myObj = {
//     id: 2,
//     printId(){
//         console.log(this.id)
//     }
// }

// myObj.printId()

// const sayFoo = function(){
//     console.log(this['foo'])
// }

// foo = 'foo'

// const mySecondObj = {
//     foo: "I'm in the obj",
//     sayFoo
// }

// // sayFoo()
// mySecondObj.sayFoo()

// function MyObj(id){
//     this.id = id
// }

// MyObj.prototype.printId = function(id){
//     console.log(this.id)
// }
// const newInstance = new MyObj(5)
// // console.log(newInstance.id)


// class MyClass {
//     constructor(id){
//         this.id = id
//     }
//     printId(id){
//         console.log(this.id)
//     }
// }

const outer = {
    func1: function(){
        console.log(this)

        const func2 = function(){
            console.log(this)

            const func3 = function(){
                console.log(this)
            }()
        }()
    }
}
