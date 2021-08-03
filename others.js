function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

	var amount = "{{ grand_total }}"
	var url = "{% url 'payments' %}"
	var csrftoken = getCookie('csrftoken');
	var orderID = "{{order.order_number}}"
	var payment_method = 'PayPal' 


paypal.Buttons({

		style: {
			color: 'blue',
			shape: 'rect',
			label: 'pay',
			height: 40
		},

		// Set up the transaction
		createOrder: function(data, actions) {
			return actions.order.create({
				purchase_units: [{
					amount: {
						value: amount,
					}
				}]
			});
		},

		// Finalize the transaction
	onApprove: function(data, actions) {
			return actions.order.capture().then(function(details) {
				// Show a success message to the buyer
				console.log(details);
          console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                    var transaction = orderData.purchase_units[0].payments.captures[0];
                    alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details')
				sendData();
				function sendData(){
					fetch(url, {
						method : "POST",
						headers: {
							"Content-type": "application/json",
							"X-CSRFToken": csrftoken,
						},
						body: JSON.stringify({
							orderID: orderID,
							transID: details.id,
							payment_method: payment_method,
							status: details.status,
						}),
					})
				  .then((response) => response.json())
				  .then((data) => {
						window.location.href = redirect_url + '?order_number='+data.order_number+'&payment_id='+data.transID;
					});
				}
			});
		}


	}).render('#paypal-button-container');