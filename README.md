# Kira
Kira is a python class for interacting with the smspool.net api.
I am not sure all of this works but I will remove this part from the readme when I am sure.

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
