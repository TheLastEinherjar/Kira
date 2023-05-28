# Kira
Kira is a python class for interacting with the smspool.net api. 

I am not sure all of this works but I will remove this part from the readme when I am sure.

# Example

```py
# Create a Kira object with your API key
kira = Kira(api_key)

# Check your balance
balance = kira.get_balance()
print(f"Your current balance is {balance}")

# Get the price for a specific service in a country
price = kira.get_order_price("US", "Google")
print(f"The price for the Google service in the US is {price}")

# Order a phone number for a specific service in a country
number, order_id = kira.order_phone_number("US", "Google")
print(f"Your new phone number for the Google service in the US is {number}")

# Wait for an SMS message to be received for the specified order ID
success, message = kira.wait_for_sms(order_id, 5)
if success:
    print(f"Received SMS message: {message}")
else:
    print(f"Failed to receive SMS message: {message}")
```
# Methods

get_balance() to retrieve the account balance.

get_order_price(country_code, service_name) to retrieve the price of an SMS for a specific country and service.

get_countries() to retrieve a list of countries available for ordering phone numbers.

get_country_id_by_country_code(country_code) to get the ID of the country based on its country code.

get_services() to retrieve a list of services available when ordering phone numbers.

get_service_id_by_name(service_name) to get the ID of the service based on its name.

order_phone_number(country_code, service_name) to order a phone number for a specific country and service.

check_sms(order_id, get_response_on_fail=False) to check if an SMS has been received for a specific order ID.

wait_for_sms(order_id, cycle_time) to wait for an SMS to be received for a specific order ID.
