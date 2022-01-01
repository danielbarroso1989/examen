import requests
from company.forms import Companyform
from company.models import Company
#Todo: Use polygon library for validate  symbol bursatil
def search_symbol(symbol):
    
    try:
        symbol = symbol.upper()
        print(symbol)
        url= "https://api.polygon.io/v3/reference/tickers?ticker="+symbol+"&active=true&sort=ticker&order=asc&limit=10&apiKey=5BMSKHMUnbd7xp2H4cSwD0ga7V56gpG5"
        result = requests.get(url)
        result_json_ticker = result.json()["results"][0]
        return result_json_ticker
    
    except Exception as e:
        print("Error validate symbol:",e)
       
    return False


#todo: function for validate, clean data and create company
def validatedata(data):

    try:

        form = Companyform(data)

        if form.is_valid():

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            symbol = form.cleaned_data['symbol']
            values = form.cleaned_data['values']
            result_symbol = search_symbol(symbol)

            if result_symbol:

             
                Company_create = Company.objects.create(name=name,description=description,symbol=symbol,values=values)

                return "OK"

           

            return " symbol bursatil incorrect"
    
    except Exception as e:
        
        print("Error validate symbol:",e)   
 
    return "Validate data complete"
