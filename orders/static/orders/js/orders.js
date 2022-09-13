var order = document.querySelector('#order');
var ordertotal = document.querySelector('#ordertotal');

function addItem(id) {
    name = '#name' + id;
    var name = document.querySelector(name).innerHTML;

    price = '#price' + id;
    var price = document.querySelector(price).innerHTML;

    order.innerHTML += '<li>'+ name + ' ' + price +'</li>';
}