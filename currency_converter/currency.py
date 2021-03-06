import requests
import json
import pandas as pd

connection=True
test_url = "https://www.google.com"
timeout = 5
ap = 'https://api.exchangerate-api.com/v4/latest/USD'
try:
    request = requests.get(test_url, timeout=timeout)
    connection=True
    with open('rates.txt', 'w') as outfile:
        json.dump(CurrencyConverter_online(ap).data, outfile)

except (requests.ConnectionError, requests.Timeout) as exception:
    connection=False
    print("No internet connection.")

with open('rates.txt') as json_file:
    data = json.load(json_file)


class CurrencyConverter_online():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
        self.time = self.data['date']

class CurrencyConverter():
    if connection==True:
        def __init__(self,url,rates):
            self.data= requests.get(url).json()
            self.currencies = self.data['rates']
            self.time = self.data['date']
        def convert(self, from_currency, to_currency, amount): 
            initial_amount = amount 
            #first convert it into USD if it is not in USD.
            # because our base currency is USD
            if from_currency != 'USD' : 
                amount = amount / self.currencies[from_currency] 
  
            # limiting the precision to 4 decimal places 
            amount = round(amount * self.currencies[to_currency], 4) 
            return amount

    else:
        def __init__(self,url,rates):
            self.currencies = rates['rates']
            self.time = rates['date']
        def convert(self, from_currency, to_currency, amount): 
            initial_amount = amount 
            #first convert it into USD if it is not in USD.
            # because our base currency is USD
            if from_currency != 'USD' : 
                amount = amount / self.currencies[from_currency] 
  
            # limiting the precision to 4 decimal places 
            amount = round(amount * self.currencies[to_currency], 4) 
            return amount




converter=CurrencyConverter(ap,data)
print("Here is the list of currency codes, please select the ones you want")
#with open('codes-all.json') as json_file:
#    codes = json.load(json_file)
#df=(pd.read_json('codes-all.json')[["AlphabeticCode","Currency"]])
#print(df.drop_duplicates())
print(converter.currencies.keys())
fromcurr = input("Please enter the currency you want to convert from in caps: ")
tocurr = input ("Please enter the currency you want to convert to in caps: ")
amountcurr = input ("Please enter the amount of money you want to convert: ")
print(converter.time)
print(amountcurr +fromcurr + " is equal to " +str(converter.convert(fromcurr,tocurr,float(amountcurr)))+tocurr+", using exchange rate of the date: " +str(converter.time))
