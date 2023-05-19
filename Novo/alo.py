from customtkinter import *

def menu_principal():
    menu = CTK()
    menu.geometry("300x200")
    menu.title("Menu Principal")

    # Função para abrir o menu secundário
    def abrir_menu_secundario():
        menu.destroy()  # Fecha o menu principal
        menu_secundario()

    # Botão para abrir o menu secundário
    btn_secundario = menu.button("Abrir Menu Secundário", command=abrir_menu_secundario)
    btn_secundario.pack(pady=50)

    menu.mainloop()

def menu_secundario():
    menu = CTK()
    menu.geometry("300x200")
    menu.title("Menu Secundário")

    # Função para voltar ao menu principal
    def voltar_menu_principal():
        menu.destroy()  # Fecha o menu secundário
        menu_principal()

    # Botão para voltar ao menu principal
    btn_voltar = menu.button("Voltar ao Menu Principal", command=voltar_menu_principal)
    btn_voltar.pack(pady=50)

    menu.mainloop()

# Inicia o programa pelo menu principal
menu_principal()