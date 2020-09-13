import alpaca_trade_api as tradeapi

API_KEY = "<Your API here>"
SECRET_KEY = "<Your secret key here>"

#---------------- API INFO ----------------#
api = tradeapi.REST(API_KEY,
                    SECRET_KEY,
                    'https://paper-api.alpaca.markets')

#-------- Here basket of stocks ------------#
symbols = ['AA', 'AAL', 'UAL', 'NIO', 'AMD', 'TSLA']


#---- NUMBER OF SHARES FOR EACH PURCHASE -----#
loading = {'AA': 50,
           'AAL': 50,
           'UAL': 50,
           'NIO': 50,
           'AMD': 50,
           'TSLA': 10}

#---- SET SLOW AND FAST MOVING AVERAGE -----#
slow = 20
fast = 1

#------- FREQUENCY for you time interval -----------#
freq = '1Min'