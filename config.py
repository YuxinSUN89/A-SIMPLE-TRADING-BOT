import alpaca_trade_api as tradeapi
API_KEY = "<Your API here>"
SECRET_KEY = "<Your secret key here>"

#---------------- API INFO ----------------#
api = tradeapi.REST(Yuxin_config.API_KEY,
                    Yuxin_config.SECRET_KEY,
                    'https://paper-api.alpaca.markets')


#-------- Here basket of stocks ------------#
symbols = ['AA', 'AAL', 'UAL', 'NIO', 'AMD', 'NCLH', 'BYND', 'DAL', 'ATVI', 'WORK', 'VIRT', 'AAPL', 'AMC', 'TSLA']


#---- NUMBER OF SHARES FOR EACH PURCHASE -----#
loading = {
    'AA': 100,
    'AAL': 100,
    'UAL': 100,
    'NIO': 100,
    'AMD': 100,
    'NCLH': 100,
    'BYND': 100,
    'DAL': 100,
    'ATVI': 100,
    'WORK': 100,
    'VIRT': 100,
    'AAPL': 10,
    'AMC': 200,
    'TSLA': 40}

#---- SET SLOW AND FAST MOVING AVERAGE -----#
slow = 20
fast = 1

#------- FREQUENCY for you time interval -----------#
freq = '1Min'