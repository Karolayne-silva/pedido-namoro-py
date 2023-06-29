from tkinter import *


def nao():
    global img2
    mensagem = "Que isso? APERTE NO SIM"
    label_mensagem.config(text=mensagem)
   
    

def sim():
    global img
    mensagem = "te amoo momo feliz 5 anos e alguns meses"
    label_mensagem.config(text=mensagem)
    



janela = Tk()
janela.title('Aceitas?')
janela.geometry("500x500")
janela.configure(background='#6959CD')

texto = Label(janela, text='Quer namorar comigo de novo?', fg='#fff', bg='#6959CD', font='40')
texto.pack(pady=20)

buttom = Button(janela, text='Sim', width=15, height=1, bg='#DA70D6', fg='#fff', font='5', command=sim)
buttom.pack(pady=25)

buttom2 = Button(janela, text='Não', width=15, height=1, bg='#DA70D6', fg='#fff', font='5', command=nao)
buttom2.pack(pady=5)

label_mensagem = Label(janela, text="", bg='#6959CD', fg='#fff', font='1')
label_mensagem.pack(pady=20)


label_imagem = Label(janela, bg='#6959CD')
label_imagem.pack()
label_imagem2 = Label(janela, bg='#6959CD')
label_imagem2.pack()

janela.mainloop()

