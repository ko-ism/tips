# tips
## 基礎
### this (basic_test/this_test.js)
- thisを呼び出す際の、呼び出す場所によってwindowオブジェクトか、自身のオブジェクトを指すかが分かれる

### アロー関数
- https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Functions/Arrow_functions
- 関数内でアロー関数を定義し、そのなかでthisを呼び出すと、自身のオブジェクトを指す

```
  let normalFn;
  normalFn = {
      id: 43,
      counter: function(){
          console.log(this);
          setTimeout(() => {
              // この場合のthisは、normalFn objを指す
              console.log(this);
          }, 1000)
      }
  }
  normalFn.counter();
```


```
  let normalFn;
  normalFn = {
      id: 43,
      counter: function(){
          console.log(this);
          setTimeout( function() {
              // この場合のthisは、window obj
              console.log(this);
          }, 1000)
      }
  }
  normalFn.counter();
```
