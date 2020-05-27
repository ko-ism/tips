const btn = document.querySelector('#btn');
const h1 = document.querySelector('h1');

const hello = function() {
    alert('hello');
    this.style.color = 'red';
};

const changeColor = function() {
    h1.style.backgroundColor = 'yellow';
};

btn.addEventListener('click', hello);
btn.addEventListener('click', changeColor);