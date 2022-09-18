var cart = document.querySelector('#cart');
var total = document.querySelector('#ordertotal');

function addItem(id) {
    name = '#name' + id;
    var name = document.querySelector(name).innerHTML;

    price = '#price' + id;
    var price = document.querySelector(price).innerHTML;

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    orders[cartSize] = [name, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    remove = '<button class="del" onclick="removeItem(' + cartSize + ')">x</button>';
    ordertotal.innerHTML = 'Total: €' + total;
    cart.innerHTML += '<li>'+ remove + name + ': €' + price + '</li>';
}

function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    cart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<button class="del" onclick="removeItem(' + i + ')">x</button>';
        cart.innerHTML += '<li>'+ remove + orders[i][0] + ': €' + orders[i][1] + '</li>';
    }
    ordertotal.innerHTML = 'Total: €' + total;
}

shoppingCart()

function removeItem(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][1]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingCart();
}