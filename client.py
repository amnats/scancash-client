import requests
from config import scanner_id


def send_barcode(barcode):
    barcode = barcode.replace('^[[B', '')
    print(barcode)
    r = requests.post(
        'https://scancash.herokuapp.com/scanners/record',
        json={
            'scanner_id': scanner_id,
            'record': barcode,
        })
