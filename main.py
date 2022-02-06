from pycbrf import ExchangeRates
from datetime import datetime

time = datetime.now().strftime("%Y-%m-%d")
rates = ExchangeRates(time, locale_en=True)

int_item = 10
comp_item = 18
mult_int = int_item * 2
item_2 = True
item_3 = False
item_4 = 0
item_5 = 1

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
usd_eur_rate = rates['USD'].value / rates['EUR'].value

uah_item = "uah"
# why usd_uah_rate = 26.23 ???
usd_uah_rate = rates['USD'].value / rates['UAH'].value

chf_item = "chf"
usd_chf_rate = rates['USD'].value / rates['CHF'].value

rub_item = "rub"
usd_rub_rate = rates['USD'].value

byn_item = "byn"
usd_byn_rate = rates['USD'].value / rates['BYN'].value

if mult_int > comp_item:
    print(f"Переменная mult_int ({mult_int}) больше" +
          f" чем переменная comp_item ({comp_item})")

div_int = int_item / 2
if div_int < comp_item:
    print(f"Переменная div_int ({div_int}) меньше" +
          f" чем переменная comp_item ({comp_item})")

item_1 = int_item + 10
if item_1 < comp_item:
    print(f"Переменная item_1 ({item_1}) меньше" +
          f" чем переменная comp_item ({comp_item})")
else:
    print(f"Переменная item_1 ({item_1}) больше или равна" +
          f" чем переменная comp_item ({comp_item})")

if item_2:
    print(f"Переменная item_2 = {item_2}")
else:
    print(f"Переменная item_2 = {item_3}")
if item_3:
    print(f"Переменная item_3 = {item_2}")
else:
    print(f"Переменная item_3 = {item_3}")
if item_5:
    print(f"Переменная item_5 = {item_5}")
else:
    print(f"Переменная item_5 = {item_4}")
if item_4:
    print(f"Переменная item_4 = {item_5}")
else:
    print(f"Переменная item_4 = {item_4}")

currency_convertor = item_2
if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == "eur":
        currency_result = target_currency_amount / usd_eur_rate
        print(f"{target_currency_amount} {eur_item} = {currency_result:.{3}f} {usd_item}")
    elif target_currency == "uah":
        currency_result = target_currency_amount / usd_uah_rate
        print(f"{target_currency_amount} {uah_item} = {currency_result:.{3}f} {usd_item}")
    elif target_currency == "usd":
        currency_result = target_currency_amount
        print(f"{target_currency_amount} {usd_item} = {currency_result:.{3}f} {usd_item}")
    elif target_currency == "chf":
        currency_result = target_currency_amount / usd_chf_rate
        print(f"{target_currency_amount} {chf_item} = {currency_result:.{3}f} {usd_item}")
    elif target_currency == "rub":
        currency_result = target_currency_amount / usd_rub_rate
        print(f"{target_currency_amount} {rub_item} = {currency_result:.{3}f} {usd_item}")
    elif target_currency == "byn":
        currency_result = target_currency_amount / usd_byn_rate
        print(f"{target_currency_amount} {byn_item} = {currency_result:.{3}f} {usd_item}")
    else:
        print("Unknow currency")
else:
    print(f"Переменная currency_convertor = {item_3}")