import requests
from config import scanner_id


def send_barcode(barcode):
    print('before', barcode)
    try:
        barcode = barcode.strip().replace('^[[B', '')
        barcode = ''.join(c for c in barcode if c.isprintable())
        barcode = barcode.replace('[B', '')
        print('after', barcode)
        print(len(barcode))
    except AttributeError:
        pass

    r = requests.post(
        'https://scancash.herokuapp.com/scanners/record',
        json={
            'scanner_id': scanner_id,
            'record': barcode,
        })
