import alpaca_trade_api as tradeapi

#API_KEY = "<Your API here>"
#SECRET_KEY = "<Your secret key here>"
API_KEY = "PK4G3XX1Y9R5DBQ7QVDI"
SECRET_KEY = "fdqmnZ8xImi2KhCzaUU9pZFohvORdwa8WmOMYcms"

#---------------- API INFO ----------------#
api = tradeapi.REST(API_KEY,
                    SECRET_KEY,
                    'https://paper-api.alpaca.markets')

#-------- Here basket of stocks ------------#
symbols = ['AA', 'AAL', 'UAL', 'NIO', 'AMD', 'TSLA', 'BYND', 'NKLA', 'XPEV']


#---- NUMBER OF SHARES FOR EACH PURCHASE -----#
loading = {'AA': 50,
           'AAL': 50,
           'UAL': 50,
           'NIO': 50,
           'AMD': 50,
           'TSLA': 10,
           'BYND': 20,
           'NKLA': 30,
           'XPEV': 30}

#---- SET SLOW AND FAST MOVING AVERAGE -----#
slow = 20
fast = 1

#------- FREQUENCY for you time interval -----------#
freq = '1Min'