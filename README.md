# ALPACA-TRADING-BOT
This a trading bot based on Alpaca API.
Use the package manager pip to install.
## Installation
```bash
pip -r requirements
```

## Usage
To get data from the API, simply import the library and call the object with your API key. Your API key may also be stored in the environment variable in config file.
```bash
API_KEY = "<Your API here>"
SECRET_KEY = "<Your secret key here>"

api = tradeapi.REST(API_KEY,
                    SECRET_KEY,
                    'https://paper-api.alpaca.markets')
```
Also you can list the stocks you want to trade in 
```bash
symbols = ['AA', 'AAL', 'UAL', 'NIO', 'AMD', 'NCLH', 'BYND', 'DAL', 'ATVI', 'WORK', 'VIRT', 'AAPL', 'AMC', 'TSLA']
```
and number of shares you want to purchase each time (buy more shares for small-cap stock and less shares for large-cap stocks)
```bash
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
```
Last, set the slow and fast moving average and time frequency data for your dataframe.
```bash
slow = 20
fast = 1
freq = '1Min'
```

## Data frame structure.



```python
import 

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
