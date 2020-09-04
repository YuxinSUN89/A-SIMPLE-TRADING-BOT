
import pandas as pd
import Yuxin_config
from StockInfo import *
from get_data import *

def time_to_open(current_time):
    if current_time.weekday() <= 4:
        d = (current_time + timedelta(days=1)).date()
    else:
        days_to_mon = 0 - current_time.weekday() + 7
        d = (current_time + timedelta(days=days_to_mon)).date()
    next_day = datetime.datetime.combine(d, datetime.time(8, 30, tzinfo=tz))
    seconds = (next_day - current_time).total_seconds()
    return seconds


def run_checker():
    print('run_checker started')
    while True:
        # Check if Monday-Friday
        if datetime.datetime.now(tz).weekday() >= 0 and datetime.datetime.now(tz).weekday() <= 4:
            # Checks market is open
            print('Trading in process '+ datetime.datetime.now().strftime("%x %X"))
            if datetime.datetime.now(tz).time() > datetime.time(8, 30) and datetime.datetime.now(tz).time() <= datetime.time(15, 00):
                dataframe = StockInfo(Yuxin_config.symbols, Yuxin_config.freq, Yuxin_config.slow, Yuxin_config.fast)
                signals = dataframe.get_signals()
                for signal in signals:
                    if signals[signal] > 0:
                        # [x.symbol for x in api.list_positions()] collect all stock tickers
                        try:
                            api.submit_order(signal, signals[signal], 'buy', 'market', 'day')
                            logging.warning('{} bought {}  {} shares, portfolio value {} 🤑💵'.format(datetime.datetime.now(tz).strftime("%x %X"),
                                                                                                            signal, signals[signal], api.get_account().equity))
                        except:
                            logging.warning('{} Insufficient buying power'.format(datetime.datetime.now(tz).strftime("%x %X")))
                            print('Trading in process '+ datetime.datetime.now().strftime("%x %X") + ' Insufficient fund')
                            pass

                            # print(datetime.datetime.now(tz).strftime("%x %X"), 'buying', signals[signal], signal)
                    elif signals[signal] < 0:
                        try:
                            api.submit_order(signal, -signals[signal], 'sell', 'market', 'day')
                            logging.warning('{} sold   {} {} shares, portfolio value {} 🤖💵'.format(datetime.datetime.now(tz).strftime("%x %X"), signal, signals[signal], api.get_account().equity))
                        except Exception as e:
                            # print('No sell', signal, e)
                            pass

                time.sleep(60)

            else:
                # Get time amount until open, sleep that amount
                print('Market closed ({})'.format(datetime.datetime.now(tz)))
                print('Sleeping', round(time_to_open(datetime.datetime.now(tz))/60/60, 2), 'hours')
                time.sleep(time_to_open(datetime.datetime.now(tz)))
        else:
            # If not trading day, find out how much until open, sleep that amount
            print('Market closed ({})'.format(datetime.datetime.now(tz)))
            print('Sleeping', round(time_to_open(datetime.datetime.now(tz))/60/60, 2), 'hours')
            time.sleep(time_to_open(datetime.datetime.now(tz)))

if __name__ == "__main__":
    run_checker()


