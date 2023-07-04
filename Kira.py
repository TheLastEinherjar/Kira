import requests
import time

class Kira :
    def get_balance(self) :
        url = 'https://api.smspool.net/request/balance'
        params = {
            'key': self.api_key,
        }
        response = requests.get(url, params=params)
        json_response = response.json()
        return float(json_response['balance'])
    
    def get_order_price(self, country_code, service_name) :
        url = 'https://api.smspool.net/request/price'
        params = {
            'key': self.api_key,
            'country' : country_code,
            'service' : service_name
        }
        response = requests.get(url, params=params)
        json_response = response.json()
        if 'price' in json_response :
            return json_response['price']
        else :
            return None
    
    def get_countries(self) :
        url = 'https://api.smspool.net/country/retrieve_all'
        response = requests.get(url)
        json_response = response.json()
        return json_response
    
    def get_country_id_by_country_code(self, country_code : str) :
        json_response = self.get_countries()
        for diction in json_response :
            if diction['short_name'] == country_code.upper() :
                return diction['ID']
        return None
    
    def get_services(self) :
        url = 'https://api.smspool.net/service/retrieve_all'
        response = requests.get(url)
        json_response = response.json()
        return json_response
    
    def get_service_id_by_name(self, service_name) :
        json_response = self.get_services()
        for diction in json_response :
            if diction['name'] == service_name :
                return diction['ID']

    def order_phone_number(self, country_code, service_name):
        url = 'https://api.smspool.net/purchase/sms'
        data = {
            'key': self.api_key,
            'service': service_name,
            'country': country_code
        }
        response = requests.post(url, data=data)
        json_response = response.json()
        if 'number' in json_response:
            return str(json_response['number']), str(json_response['order_id'])
        else:
            print(json_response)
            return None, None

    def check_sms(self, order_id, get_response_on_fail=False):
        url = 'https://api.smspool.net/sms/check'
        params = {
            'key': self.api_key,
            'orderid': order_id
        }
        response = requests.get(url, params=params)
        json_response = response.json()
        if 'sms' in json_response :
            return json_response['sms']
        else:
            print(json_response['message'])

            if get_response_on_fail :
                return json_response
            else :
                return None
        
    def wait_for_sms(self, order_id, cycle_time:int=10, max_wait_time:int = -1) :
        current_wait_time = 0
        done_looping = False
        while not done_looping  :
            time.sleep(cycle_time)
            current_wait_time += cycle_time
            response = self.check_sms(order_id, True)
            if 'message' in response :
                #we did not get the sms
                if 'status' in response and response['status'] == 1:
                    #if it is pending
                    if not max_wait_time == -1 :
                        done_looping = (current_wait_time >= max_wait_time)
                    continue
                else :
                    #else return the message
                    return False, response['message']
            else :
                return True, response
        return False, 'wait time up'


    def __init__(self, api_key) :
        self.api_key = api_key
