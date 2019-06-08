import requests
import json

payload={'Amount': '100.10','Counterpart': '2C3MSBV5RL8I9EgKaXfhu7hvbjYpcdl5BLmDqqbb', 'Desc': 'Pagamento de honorários'}

r = requests.post('https://www.btgpactual.com/btgcode/api/money-movement', headers={'x-api-key':'ZtPtIH0U8JUUYTul1VTCBt768u0dez2kUKOOICVh'}, data=json.dumps(payload) )

print(r.text)

"""print(r)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())"""