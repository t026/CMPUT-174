import requests, pprint

def main():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    print(response.status_code)
    
    if response.status_code == 200:
        data = response.json() # json() method is same as loads()
        #pprint.pprint(data)
        rates = data["rates"]
        pprint.pprint(rates)
        print(f'1 Euro = {rates["PKR"]} PKR')

main()