import tkinter
import customtkinter

from config import APARENCIA_PRINCIPAL, TEMA_PRINCIPAL
from constantes import OPCOES_APARENCIA, OPCOES_TEMA, ETAPAS_PS

customtkinter.set_appearance_mode(APARENCIA_PRINCIPAL)
customtkinter.set_default_color_theme(TEMA_PRINCIPAL)

class InterfaceGrafica(customtkinter.CTk):
    """
    Classe responsável pela estruturação da interface gráfica do programa. Aqui são configuradas todas as widgets, bem como os comandos que elas irão disparar. Entretanto, a lógica por trás do funcionamento dessas widgets deve ser implementada em `App`, sobrescrevendo as funções herdadas por `InterfaceGrafica`.
    """
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("MinervaBots - Gerenciador de Emails")
        #self.geometry(f"{LARGURA_JANELA_PRINCIPAL}x{ALTURA_JANELA_PRINCIPAL}")

        # Criando elementos do Menu Principal
        self.container_menu_principal = customtkinter.CTkFrame(
            self, 
            width=200, 
            corner_radius=0
        )
        self.container_email = customtkinter.CTkFrame(
            self.container_menu_principal
        )
        self.container_planilhas = customtkinter.CTkFrame(
            self.container_menu_principal
        )
        self.email_label = customtkinter.CTkLabel(
            self.container_email, 
            text="E-mail", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.input_email = customtkinter.CTkEntry(
            self.container_email,
            placeholder_text='Digite o e-mail (remetente)'
        )
        self.input_senha = customtkinter.CTkEntry(
            self.container_email,
            placeholder_text='Digite a senha'
        )
        self.botao_login = customtkinter.CTkButton(
            self.container_email,
            text='Salvar dados',
            command=self.salvar_dados_email
        )
        self.planilhas_label = customtkinter.CTkLabel(
            self.container_planilhas, 
            text="Planilhas", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.botao_carregar_planilha_ps = customtkinter.CTkButton(
            self.container_planilhas, 
            text = 'Carregar Planilha PS', 
            command=self.carregar_planilha_ps
        )
        self.botao_carregar_planilha_180 = customtkinter.CTkButton(
            self.container_planilhas, 
            text = 'Carregar Planilha 180', 
            command=self.carregar_planilha_180
        )

        # Posicionando elementos no Menu Principal
        self.container_menu_principal.grid(row=0, column=0, padx=(10,0)) # Container menu principal
        self.container_email.grid(row=0, column=0) # Container email (inputs e botão de login)
        self.container_planilhas.grid(row=1, column=0) # Container dos botões de carregar planilha
        self.email_label.grid(row=0, column=0, padx=20, pady=(10, 10)) # Título do container email
        self.input_email.grid(row=1, column=0, padx=20, pady=(0,10)) # Input de email
        self.input_senha.grid(row=2, column=0, padx=20, pady=(0, 10)) # Input da senha do email
        self.botao_login.grid(row=3, column=0, padx=20, pady=(0, 10)) # Botão de login
        self.planilhas_label.grid(row=4, column=0, padx=20, pady=(10, 10)) # Título do container Planilhas
        self.botao_carregar_planilha_ps.grid(row=5, column=0, padx=20, pady=(0, 5)) # Botão Planilha PS
        self.botao_carregar_planilha_180.grid(row=6, column=0, padx=20, pady=(5, 10)) # Botão Planilha 180

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
        """
        Exibe uma mensagem padrão (branca) no console de saída do sistema. Pode ser modificada mudando o valor da propriedade `tag` de `padrao` para `aviso`, `erro` ou `sucesso`. Evite usar outros valores para `tag`, opte por usar as funções específicas: `sistema_msg_erro()`, `sistema_msg_alerta()` e `sistema_msg_sucesso()`. Por padrão, irá pular linha após exibir a mensagem, mas pode ser aterado através da propriedade `pula_linha`.
        """
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
        """
        Exibe uma mensagem de sucesso (verde) no console de saída do sistema. Use esse tipo de mensagem para deixar o usuário ciente de que o procedimento foi concluído com sucesso.
        """
        self.sistema_msg_padrao(mensagem, 'sucesso')

    def sistema_msg_alerta(self, mensagem: str) -> None:
        """
        Exibe uma mensagem de alerta (amarela) no console de saída do sistema. Use esse tipo de mensagem para chamar a atenção do usuário.
        """
        self.sistema_msg_padrao(mensagem, tag='aviso')

    def sistema_msg_erro(self, erro: Exception, procedimento: str) -> None:
        """
        Exibe uma mensagem de erro (vermelha) no console de saída do sistema. O parâmetro `erro` recebe o tipo de erro, vindo de um bloco `except` e trata para a mensagem ser exibida. O parâmetro `procedimento` deve receber uma indicação de que procedimento o usuário estava tentando fazer quando ocorreu o erro.
        """
        msg_erro = str(erro)
        self.sistema_msg_padrao(f'Ocorreu um erro ao tentar {procedimento}:', tag='erro')
        self.sistema_msg_padrao(msg_erro, tag='erro')
    
    # Comando responsável pro passar a planilha do processo seletivo
    def carregar_planilha_ps(self):
        self.sistema_msg_padrao('Abrindo Planilha de PS...')

    def carregar_planilha_180(self):
        self.sistema_msg_padrao('Abrindo Planilha de 180...')

    def salvar_dados_email(self):
        self.sistema_msg_padrao(f'Enviando dados do email: {self.input_email.get()} ...')

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