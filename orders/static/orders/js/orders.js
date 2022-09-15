var cart = document.querySelector('#cart');
var total = document.querySelector('#ordertotal');

function addItem(id) {
    name = '#name' + id;
    var name = document.querySelector(name).innerHTML;

    price = '#price' + id;
    var price = document.querySelector(price).innerHTML;

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');

    orders = [name,price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    ordertotal.innerHTML = 'Total: ' + total + '';
    cart.innerHTML += '<li>'+ name + ' ' + price +'</li>';
}