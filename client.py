import requests

scanner_id = 1

def send(barcode):
  r = requests.post('https://scancash.herokuapp.com/scanners/record', data = {
    'scanner_id': scanner_id,
    'record': barcode,
  })