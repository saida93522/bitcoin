
import requests 
import pyinputplus as pyip

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    bitcoin = get_bitcoin_value()
    dollars = get_bitcoin_rate(bitcoin)
    display_result(bitcoin, dollars)
    
    
def get_bitcoin_value():
    bitcoin = pyip.inputFloat('Enter the number of bitcoin: ')
    return bitcoin

def get_bitcoin_rate(bitcoin):
    req_rate = request_coin_data()
    res = extract_data(req_rate)
    if res: 
        dollar = convert_rate(bitcoin,res)
    else:
        res.raise_for_status()

    return dollar

def request_coin_data():
    return requests.get(url).json()
    
def extract_data(res):
    return res['bpi']['USD']['rate_float']

def convert_rate(bitcoin,dollar):
    return bitcoin * dollar
    

def display_result(bitcoin,dollars):
    print(f'{bitcoin} Bitcoin is equivalent to ${dollars}')
    

if __name__ == '__main__':
    main()
    