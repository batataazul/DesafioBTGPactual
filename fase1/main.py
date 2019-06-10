from tkinter import *
import json
import requests

def close_window():
    root.destroy()
    exit()

def clickSaque():
    val=textentry.get()
    output.delete(0.0,END)
    payload={'Amount': val,'Counterpart': '2C3MSBV5RL8I9EgKaXfhu7hvbjYpcdl5BLmDqqbb', 'Desc': 'Pagamento de honorários'}
    r = requests.post('https://www.btgpactual.com/btgcode/api/money-movement', headers={'x-api-key':'ZtPtIH0U8JUUYTul1VTCBt768u0dez2kUKOOICVh'}, data=json.dumps(payload) )
    try:
        val2 = "%.2f" %float(val)
        extrato.append(val2)
    except:
        print("Algo deu errado")
    output.insert(END, r.text)

def clickExtrato():
    output.delete(0.0,END)
    string  = "Extrato:"
    for i in extrato:
        string = string+"\n"+"saque: R$"+str(i)
    output.insert(END, string)

extrato = []

#cria janela
root = Tk()
root.title("BTG")

#cria label
label = Label(root, text = "Entre o valor a ser sacado").grid(row=1,column=0,sticky=W)

#cria entrada de texto
textentry = Entry(root, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#cria botão
Button(root, text="Sacar", width=20,command=clickSaque).grid(row=3,column=0,sticky=W)

#botão de extrato
Button(root, text="Extrato", width=20,command=clickExtrato).grid(row=5,column=0,sticky=W)

#cria caixa de texto
output = Text(root, width=20, height=6, wrap=WORD)
output.grid(row=4, column=0, columnspan=1, sticky=W)


#botão de saida
Button(root, text="Sair", width=20,command=close_window).grid(row=7,column=0,sticky=W)
root.mainloop()
