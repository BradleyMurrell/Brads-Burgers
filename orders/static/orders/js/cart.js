var item = document.querySelector("#item");
var subtotal = document.querySelector("#subtotal");
var grandtotal = document.querySelector("#grandtotal");

function fshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    item.innerHTML = 'Item';
    subtotal.innerHTML = 'Subtotal';

    for (let i = 0; i < cartSize; i++) {
        item.innerHTML += '<h4>' + orders[i][0] + '</h4>';
        subtotal.innerHTML += '<h4>' + '€ ' + orders[i][1] + '</h4>';
    }
    grandtotal.innerHTML = 'Total: € ' + total;
}

fshoppingCart()

function confirmation() {
    var orders = localStorage.getItem('orders');

    var ur = '/confirmation/';
    var orderData = {};
    orderData['orders'] = orders;
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        success: function(data){
            window.location.replace('/confirmation/success')
            localStorage.setItem('orders', JSON.stringify([]));
            localStorage.setItem('total', 0);
        }
    })
}