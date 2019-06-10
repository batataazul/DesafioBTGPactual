from tkinter import *
import json
import requests
"""
def click():
    entered_text=textentry.get()
    output.delete(0.0,END)

#cria janela
root = Tk()
root.title("Saques BTG pactual")

#cria label
label = Label(root, text = "Enter something").grid(row=1,column=0,sticky=W)

#cria entrada de texto
textentry = Entry(root, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#cria botão
Button(root, text="sacar", width=6,command=click()).grid(row=3,column=0,sticky=W)

#cria outra label
label = Label(root, text = "Enter another thing").grid(row=4,column=0,sticky=W)

#cria caixa de texto
output = Text(root, width=75, height=6, wrap=WORD)
output.grid(row=5, column=0, columnspan=2, sticky=W)

root.mainloop()
"""
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



"""print(r)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())"""