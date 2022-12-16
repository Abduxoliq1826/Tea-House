let order = document.querySelector('#order_tab')
let delivery = document.querySelector('#delivery_tab')
let orders = document.getElementById('orders')
let delivers = document.getElementById('delivers')

orders.addEventListener('click', (e) => {
    e.preventDefault()
    order.style.display = 'block'
    delivery.style.display = 'none'
    console.log('something went wrong')
})

delivers.addEventListener('click', (e) => {
    e.preventDefault()
    delivery.style.display = 'block'
    order.style.display = 'none'
    console.log('something went wrong')
})

