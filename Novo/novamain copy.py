import psycopg2
from Controle.classControle import Conexao
from Modelo.classCliente import Cliente
from customtkinter import *
from functools import partial

conexao = Conexao("ABC", "localhost", "5432", "postgres", "postgres")
def CriarTabelas(aux):

    while aux<2:
        try: 
            conexao.manipularBanco(Cliente. criarTabelaCliente())
           # conexaoLivraria.manipularBanco(Livro. criarTabelaLivro())
           # conexaoLivraria.manipularBanco(Aluguel. criarTabelaAluguel())
            print("Tabelas Criadas com sucesso!")
        except(Exception,psycopg2.Error) as error:
            print("Algo deu Errado! ",error)

        aux += 1

# CriarTabelas(1)

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gerenciamento")
        self.geometry("600x500")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)


        #Menu de navegação
        self.menuNavegacao = CTkFrame(self, fg_color="transparent")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)
    
        self.botaoTelaInicial = CTkButton(self.menuNavegacao, text="Tela Inicial", command=partial(self.abrirTela,"Tela Inicial"))
        self.botaoTelaInicial.grid(column=0,row=0, padx= 20, pady= 25)

        self.botaoInserirCliente = CTkButton(self.menuNavegacao, text="Inserir Cliente", command=partial(self.abrirTela,"Inserir Cliente"))
        self.botaoInserirCliente.grid(column=0, row=1, padx= 20, pady= 25)

        self.botaoVisualizarClientes = CTkButton(self.menuNavegacao, text="Visualizar Clientes", command=partial(self.abrirTela,"Visualizar Clientes"))
        self.botaoVisualizarClientes.grid(column=0, row=2, padx= 20, pady= 25)


        #Tela Inicial
        self.telaInicial = CTkFrame(self, fg_color="gray")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

        self.telaInicial.columnconfigure(0, weight=1)
        self.telaInicial.rowconfigure(0,weight=1)

        self.mensagemBoasVindas = CTkLabel(self.telaInicial, text="Bem vindo ao Sistema de Gerenciamento de livros",text_color="black",font=CTkFont(size=16,weight="bold"), compound="top", wraplength=500)
        self.mensagemBoasVindas.grid(column=0,row=0, sticky="nsew")

        #Tela Inserir Cliente

        self.telaInserirCliente = CTkFrame(self, fg_color="transparent")

        self.tituloInserirCliente = CTkLabel(self.telaInserirCliente, text= "Inserir Cliente", font=CTkFont(size=32))
        self.tituloInserirCliente.grid(column=0, row=0)

        self.rotuloNome = CTkLabel(self.telaInserirCliente, text= "Nome: ", font=CTkFont(size=32))
        self.rotuloNome.grid(column=0, row=1, padx=30, pady=30) 

        self.campoNome = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o nome do Livro"))
        self.campoNome.grid(column=1, row=1, padx= 10, pady = 30)

        self.rotuloCPF = CTkLabel(self.telaInserirCliente, text= "CPF: ", font=CTkFont(size=32))
        self.rotuloCPF.grid(column=0, row=2, padx=30, pady=30) 

        self.campoCPF = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o CPF do Livro"))
        self.campoCPF.grid(column=1, row=2, padx= 10, pady = 30)

        self.botaoInserirCliente = CTkButton(self.telaInserirCliente, text="Enviar", command=self.inserirClienteBanco)
        self.botaoInserirCliente.grid(column=0, row=3)
    


    
    def menu__init__(self):
        super().__init__()

        self.title("Sistema de Gerenciamento")
        self.geometry("600x500")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.menuNavegacao = CTkFrame(self, fg_color="transparent")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)

        self.botaoTelaInicial = CTkButton(self.menuNavegacao, text="Tela Inicial", command=partial(self.abrirTela,"Tela Inicial"))
        self.botaoTelaInicial.grid(column=0,row=0, padx= 20, pady= 25)
        self.telaInicial = CTkFrame(self, fg_color="gray")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

        self.telaInicial.columnconfigure(0, weight=1)
        self.telaInicial.rowconfigure(0,weight=1)
        

    def abrir_menu_secundario():
        menu.destroy()  
        menu_secundario()

        btn_secundario = CTkButton(menu, text="Abrir Menu Secundário", command=abrir_menu_secundario)
        btn_secundario.pack(pady=50)

       

    def menu_secundario():
        menu = Tk()
        menu.geometry("300x200")
        menu.title("Menu Secundário")

    def voltar_menu_principal():
        menu.destroy()  
        menu_principal()

        btn_voltar = CTkButton(menu, text="Voltar ao Menu Principal", command=voltar_menu_principal)
        btn_voltar.pack(pady=50)

        menu.mainloop()




    def inserirClienteBanco(self):

        
        nome = self.campoNome.get()

        autor = self.campoCPF.get()

        print("=====INICIALIZANDO CADASTRO=======")

        cliente = Cliente(None, nome,autor)
        conexao.manipularBanco(cliente.inserirCliente())

        print("=======CADASTRO REALIZADO=========")

       
        

    def abrirTela(self,nomeDaTela):

        if nomeDaTela == "Tela Inicial":
            self.telaInicial.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInicial.grid_forget()

        if nomeDaTela == "Inserir Cliente":
            self.telaInserirCliente.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInserirCliente.grid_forget()
        '''

        if nomeDaTela == "Visualizar Clientes":
            self.telaVisualizarClientes.grid(column=1,row=0, sticky="nsew")
            conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")
        
           Clientes = conexaoBanco.consultarBanco('''
            # Select * From "Clientes"
            # Order BY "Nome" ASC ''')
        '''
           # textoExibicao = "ID | Nome | Autor "

            for Cliente in Clientes:

                textoExibicao += f"{Cliente[0]} | {Cliente[1]} | {Cliente[2]}"

            self.listaDeClientes.insert("end", textoExibicao)

        else:
            self.telaVisualizarClientes.grid_forget()
            self.listaDeClientes.delete("0.0","end")'''



if __name__ == "__main__":
    app = App()
    app.mainloop()