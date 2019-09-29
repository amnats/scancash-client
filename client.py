import requests
from config import scanner_id


def send_barcode(barcode):
    print(barcode)
    barcode.replace('^[[B', '')
    r = requests.post(
        'https://scancash.herokuapp.com/scanners/record',
        data={
            'scanner_id': scanner_id,
            'record': barcode,
        })
