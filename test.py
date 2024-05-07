import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '8129936791',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())