def currency_rates(currency_code):
    from requests import get, utils
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    split_currencies = content.split("</Valute")
    exchange_rate_string = []
    for item in split_currencies:
        if item.count(currency_code) == 1:
            exchange_rate_string = item
        else:
            pass

    exchange_rate = exchange_rate_string[
                    exchange_rate_string.index("<Value>") + 7:exchange_rate_string.index("</Value")]
    print(f'Текущий курс валюты {currency_code} к рублю составляет: {float(exchange_rate.replace(",", "."))}')


currency_rates("USD")
currency_rates("EUR")
