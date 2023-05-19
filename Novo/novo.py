from customCTk import CustomTkinter as CTK

def exibir_imagem():
    janela = CTK()
    janela.title("Exemplo de Imagem como Plano de Fundo")
    janela.geometry("400x300")

    # Cria um canvas ocupando toda a janela
    canvas = CTK.Canvas(janela, width=400, height=300)
    canvas.pack()

    # Carrega a imagem
    imagem = CTK.load_image("")  

    # Define a imagem como plano de fundo do canvas
    canvas.create_image(0, 0, anchor="nw", image=imagem)

    # Cria uma coluna dentro do canvas
    coluna = CTK.Column(canvas, width=300, height=200, bg_color="white")
    canvas.create_window(50, 50, anchor="nw", window=coluna)

    # Adicione os widgets desejados à coluna
    label = CTK.Label(coluna, text="Texto de Exemplo", font=("Arial", 14))
    label.pack()

    # Configurações de rolagem (opcional)
    scrollbar = CTK.Scrollbar(janela, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.config(yscrollcommand=scrollbar.set)

    janela.mainloop()

exibir_imagem()
