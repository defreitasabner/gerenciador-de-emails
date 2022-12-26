import tkinter
import customtkinter

from config import APARENCIA_PRINCIPAL, TEMA_PRINCIPAL, LARGURA_JANELA_PRINCIPAL, ALTURA_JANELA_PRINCIPAL
from constantes import OPCOES_APARENCIA, OPCOES_TEMA, ETAPAS_PS, COLUNAS_ESPERADAS_PLANILHA_PS

customtkinter.set_appearance_mode(APARENCIA_PRINCIPAL)
customtkinter.set_default_color_theme(TEMA_PRINCIPAL)

class InterfaceGrafica(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("MinervaBots - Gerenciador de Emails")
        #self.geometry(f"{LARGURA_JANELA_PRINCIPAL}x{ALTURA_JANELA_PRINCIPAL}")

        # Criando elementos do Menu Principal
        self.menu = customtkinter.CTkFrame(
            self, 
            width=200, 
            corner_radius=0
        )
        self.email_label = customtkinter.CTkLabel(
            self.menu, 
            text="E-mail", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.botao_login = customtkinter.CTkButton(
            self.menu, 
            text = 'Login\n(remetente)',
            command=self.login_email_remetente
        )
        self.planilhas_label = customtkinter.CTkLabel(
            self.menu, 
            text="Planilhas", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.botao_carregar_planilha_ps = customtkinter.CTkButton(
            self.menu, 
            text = 'Carregar Planilha PS', 
            command=self.carregar_planilha_ps
        )
        self.botao_carregar_planilha_180 = customtkinter.CTkButton(
            self.menu, 
            text = 'Carregar Planilha 180', 
            command=self.carregar_planilha_180
        )

        # Posicionando elementos no Menu Principal
        self.menu.grid(row=0, column=0, padx=(10,0))
        self.email_label.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.botao_login.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.planilhas_label.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.botao_carregar_planilha_ps.grid(row=3, column=0, padx=20, pady=(0, 5))
        self.botao_carregar_planilha_180.grid(row=4, column=0, padx=20, pady=(5, 10))

        # Criando elementos na Seção Principal
        self.principal = customtkinter.CTkFrame(
            self,
            width=800
        )
        self.output_sistema = customtkinter.CTkTextbox(
            self.principal,
            width= 500,
            state='disabled',
            font=("Helvetica", 12)
        )
        self.container_ps = customtkinter.CTkFrame(
            self.principal
        )
        self.container_msg_email = customtkinter.CTkFrame(
            self.principal,
            fg_color='transparent'
        )
        self.etapas_ps_label = customtkinter.CTkLabel(
            self.container_ps, 
            text="Etapas do PS", 
            font=customtkinter.CTkFont(size=12, weight="bold")
        )
        self.selecao_etapa = customtkinter.CTkSegmentedButton(
            self.container_ps,
            values = ETAPAS_PS,
            command= self.evento_selecao_etapa
        )
        self.botao_verificar_msg = customtkinter.CTkButton(
            self.container_msg_email,
            text='Verificar Mensagens',
            command=self.evento_verificar_mensagens
        )
        self.botao_enviar_emails = customtkinter.CTkButton(
            self.container_msg_email,
            text='Enviar E-mails',
            fg_color='green',
            command=self.evento_enviar_emails
        )
        # Posicionando Containers na Principal
        self.principal.grid(row=0, column=1, padx=10, pady=10)
        self.output_sistema.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.container_ps.grid(row=1, column=1, padx=10, pady=10)
        self.container_msg_email.grid(row=2, column=1, pady=(0, 10))
        # Posicionando Elementos dentro do Container de PS
        self.etapas_ps_label.grid(row=0, column=0)
        self.selecao_etapa.grid(row=1, column=0, padx=10, pady=(0, 10))
        # Posicionando Elementos dentro do Container de msg e email
        self.botao_verificar_msg.grid(row=0, column=0, padx=5)
        self.botao_enviar_emails.grid(row=0, column=1, padx=5)

        # Criando elementos do Menu de configuração
        self.configuracoes = customtkinter.CTkFrame(self, width=200)
        self.configuracoes_label = customtkinter.CTkLabel(
            self.configuracoes, 
            text="Configurações Visuais",
             font=customtkinter.CTkFont(size=20, weight='bold')
        )
        self.modo_aparecencia_label = customtkinter.CTkLabel(self.configuracoes, 
            text="Aparência:",
            anchor="n"
        )
        self.modo_aparencia_opcoes = customtkinter.CTkOptionMenu(self.configuracoes, 
            values= OPCOES_APARENCIA,
            command=self.evento_alterar_aparencia
        )
        self.tema_label = customtkinter.CTkLabel(self.configuracoes, 
            text="Tema:",
            anchor="n"
        )
        self.tema_opcoes = customtkinter.CTkOptionMenu(self.configuracoes, 
            values= OPCOES_TEMA,
            command=self.evento_alterar_tema
        )

        # Posicionando elementos no Menu de Configuração
        self.configuracoes.grid(row=0, column=2, padx=(0, 10))
        self.configuracoes_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))
        self.modo_aparecencia_label.grid(row=1, column=0, padx=5, pady=(10, 0))
        self.modo_aparencia_opcoes.grid(row=1, column=1, padx=5, pady=(10, 10))
        self.tema_label.grid(row=2, column=0, padx=5, pady=(10, 0))
        self.tema_opcoes.grid(row=2, column=1, padx=5, pady=(10, 10))

        # Criando tags para os tipos de mensagem que o sistema pode exibir
        self.output_sistema.tag_config('erro', foreground='red')
        self.output_sistema.tag_config('sucesso', foreground='green')
        self.output_sistema.tag_config('aviso', foreground='yellow')

    def sistema_msg_padrao(self, mensagem: str, tag: str = 'padrao', pula_linha: bool = True) -> None:
        self.output_sistema.configure(state='normal')
        if pula_linha:
            caracter_especial = '\n'
        else:
            caracter_especial = ''
        if tag == 'padrao':
            self.output_sistema.insert('end', f"{mensagem}{caracter_especial}")
        else:
            self.output_sistema.insert('end', f"{mensagem}{caracter_especial}", tag)
        self.output_sistema.see(tkinter.END) # Auto Scroll da Caixa de texto
        self.output_sistema.configure(state='disabled')

    def sistema_msg_sucesso(self, mensagem: str) -> None:
        self.sistema_msg_padrao(mensagem, 'sucesso')

    def sistema_msg_alerta(self, mensagem: str) -> None:
        self.sistema_msg_padrao(mensagem, tag='aviso')

    def sistema_msg_erro(self, erro: Exception, procedimento: str) -> None:
        msg_erro = str(erro)
        self.sistema_msg_padrao(f'Ocorreu um erro ao tentar {procedimento}:', tag='erro')
        self.sistema_msg_padrao(msg_erro, tag='erro')
    
    # Janela de configuração que abre quando clica no botão de configuração
    def login_email_remetente(self):
        janela_login = customtkinter.CTkToplevel(self)
        janela_login.geometry("400x200")
        janela_login.wm_transient(self)

        janela_login.title('Configuração')

        label = customtkinter.CTkLabel(janela_login, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    # Comando responsável pro passar a planilha do processo seletivo
    def carregar_planilha_ps(self):
        self.sistema_msg_padrao('Abrindo Planilha de PS...')

    def carregar_planilha_180(self):
        self.sistema_msg_padrao('Abrindo Planilha de 180...')

    def evento_alterar_aparencia(self, nova_aparencia: str) -> None:
        customtkinter.set_appearance_mode(nova_aparencia)

    def evento_alterar_tema(self, novo_tema: str) -> None:
        customtkinter.set_default_color_theme(novo_tema)

    def evento_selecao_etapa(self, botao_clicado: str):
        print(botao_clicado)

    def evento_verificar_mensagens(self):
        self.sistema_msg_padrao('Verificando Mensagens...')

    def evento_enviar_emails(self):
        self.sistema_msg_padrao('Enviando emails...')

if __name__ == "__main__":
    app = InterfaceGrafica()
    app.mainloop()