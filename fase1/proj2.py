import json
import requests

extrato = []
while(True):
    valor = input("Digite o valor a ser sacado ou digite sair para encerrar as operações e imprimir o extrato\n")

    if valor == 'sair':
        print("Muito obrigado, volte sempre")
        extrato = str(extrato)
        print("Extrato: " + extrato)
        break

    try:    
        extrato.append( float(valor))
    except:
        print("Erro na operação")
        continue

    payload={'Amount': valor,'Counterpart': '2C3MSBV5RL8I9EgKaXfhu7hvbjYpcdl5BLmDqqbb', 'Desc': 'Pagamento de honorários'}

    r = requests.post('https://www.btgpactual.com/btgcode/api/money-movement', headers={'x-api-key':'ZtPtIH0U8JUUYTul1VTCBt768u0dez2kUKOOICVh'}, data=json.dumps(payload) )

    print(r.text)