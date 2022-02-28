# Description: 
#   Money conversor using a 3rd party data rate provider
# Author: 
#   Elio Garcia
# Author GitHub profile: 
#   https://github.com/etigersoft/

from urllib.request import urlopen
import json

def convert(from_currency,currency_rate):
        convertion_results = from_currency * float(currency_rate)
        return str(round(convertion_results,2))


def run():
    welcome = """ 
    Welcome to the Real Time Convertion program, you will be able to convert your Bolivares to Dollars in real time. 
    The exchange rate data is being provided by DolarToday.com\n
    """ 

    # Bolivares rate data is provided by DolarToday.com
    json_data_url = "https://s3.amazonaws.com/dolartoday/data.json"

    # Read URL JSON object and decode it in latin because there are special characters such as Sábado
    bs_today_rate = json.loads(urlopen(json_data_url).read().decode("latin1"))
    bs_avg_rate = bs_today_rate["USD"]["promedio"]

    print(welcome + "Today's exchange rate for 1 dollar is " + str(bs_avg_rate) + " Bolivares\n")

    # Ask the user amount of dollars to convert
    dollars = float(input("Please enter dollar's amount that you'd like to convert $"))

    # Invoke the the convertion function
    results = convert(dollars,bs_avg_rate)

    print(str(dollars) + " dollars are " + results + " bolivares")

    
if __name__ == '__main__':
    run()