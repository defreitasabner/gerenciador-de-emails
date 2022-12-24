import tkinter
import customtkinter

from config import APARENCIA_PRINCIPAL, TEMA_PRINCIPAL, LARGURA_JANELA_PRINCIPAL, ALTURA_JANELA_PRINCIPAL
from constantes import OPCOES_APARENCIA, OPCOES_TEMA

customtkinter.set_appearance_mode(APARENCIA_PRINCIPAL)
customtkinter.set_default_color_theme(TEMA_PRINCIPAL)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("MinervaBots - Gerenciador de Emails")
        #self.geometry(f"{LARGURA_JANELA_PRINCIPAL}x{ALTURA_JANELA_PRINCIPAL}")

        # Criando elementos do Menu Principal
        self.menu_principal = customtkinter.CTkFrame(
            self, 
            width=200, 
            corner_radius=0
        )
        self.email_label = customtkinter.CTkLabel(
            self.menu_principal, 
            text="E-mail", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.botao_login = customtkinter.CTkButton(
            self.menu_principal, 
            text = 'Login\n(remetente)',
            command=self.login_email_remetente
        )
        self.planilhas_label = customtkinter.CTkLabel(
            self.menu_principal, 
            text="Planilhas", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.botao_carregar_planilha_ps = customtkinter.CTkButton(
            self.menu_principal, 
            text = 'Carregar Planilha PS', 
            command=self.abrir_planilha_ps
        )
        self.botao_carregar_planilha_180 = customtkinter.CTkButton(
            self.menu_principal, 
            text = 'Carregar Planilha 180', 
            command=self.sidebar_button_event
        )

        # Posicionando elementos no Menu Principal
        self.menu_principal.grid(row=0, column=0)
        self.email_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.botao_login.grid(row=1, column=0, padx=20, pady=10)
        self.planilhas_label.grid(row=2, column=0, padx=20, pady=(20, 10))
        self.botao_carregar_planilha_ps.grid(row=3, column=0, padx=20, pady=10)
        self.botao_carregar_planilha_180.grid(row=4, column=0, padx=20, pady=10)

        # Criando elementos na Seção Principal
        self.principal = customtkinter.CTkFrame(
            self,
            width=200
        )
        self.output_sistema = customtkinter.CTkTextbox(
            self.principal,
            state="disabled"
        )
        self.container_input = customtkinter.CTkFrame(
            self.principal
        )
        self.input_usuario = customtkinter.CTkEntry(
            self.container_input,
            placeholder_text="Digite seus comandos aqui"
        )
        self.botao_input_usuario = customtkinter.CTkButton(
            self.container_input,
            text='Enviar'
        )
        # Posicionando elementos na Principal
        self.principal.grid(row=0, column=1)
        self.output_sistema.grid(row=0, column=1)
        self.container_input.grid(row=1, column=1)
        self.input_usuario.grid(row=0, column=0)
        self.botao_input_usuario.grid(row=0, column=1)

        # Criando elementos do Menu de configuração
        self.menu_configuracoes = customtkinter.CTkFrame(self, width=200)
        self.menu_configuracoes_label = customtkinter.CTkLabel(
            self.menu_configuracoes, 
            text="Configurações Gerais",
             font=customtkinter.CTkFont(size=20, weight='bold')
        )
        self.modo_aparecencia_label = customtkinter.CTkLabel(self.menu_configuracoes, 
            text="Aparência:",
            anchor="w"
        )
        self.modo_aparencia_opcoes = customtkinter.CTkOptionMenu(self.menu_configuracoes, 
            values= OPCOES_APARENCIA,
            command=self.evento_alterar_aparencia
        )
        self.tema_label = customtkinter.CTkLabel(self.menu_configuracoes, 
            text="Tema:",
            anchor="w"
        )
        self.tema_opcoes = customtkinter.CTkOptionMenu(self.menu_configuracoes, 
            values= OPCOES_TEMA,
            command=self.evento_alterar_tema
        )

        # Posicionando elementos no Menu de Configuração
        self.menu_configuracoes.grid(row=0, column=2)
        self.menu_configuracoes_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))
        self.modo_aparecencia_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.modo_aparencia_opcoes.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.tema_label.grid(row=2, column=0, padx=10, pady=(10, 0))
        self.tema_opcoes.grid(row=2, column=1, padx=10, pady=(10, 10))

    # Janela de configuração que abre quando clica no botão de configuração
    def login_email_remetente(self):
        janela_login = customtkinter.CTkToplevel(self)
        janela_login.geometry("400x200")
        janela_login.wm_transient(self)

        janela_login.title('Configuração')

        label = customtkinter.CTkLabel(janela_login, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    # Comando responsável pro passar a planilha do processo seletivo
    def abrir_planilha_ps(self):
        caminho_arquivo_csv = tkinter.filedialog.askopenfilename(
            initialdir = './data/planilhas/',
            title = 'Selecione a Planilha de Processo Seletivo (.csv)',
            filetypes = (('CSV Files', '*.csv'),)
        )
        print(caminho_arquivo_csv)

    def sidebar_button_event(self):
        print("Cliquei num botão da sidebar")

    def evento_alterar_aparencia(self, nova_aparencia: str) -> None:
        customtkinter.set_appearance_mode(nova_aparencia)

    def evento_alterar_tema(self, novo_tema: str) -> None:
        customtkinter.set_default_color_theme(novo_tema)

if __name__ == "__main__":
    app = App()
    app.mainloop()