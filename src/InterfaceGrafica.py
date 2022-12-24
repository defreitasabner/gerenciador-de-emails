import tkinter
import customtkinter

from config import APARENCIA_PRINCIPAL, TEMA_PRINCIPAL, LARGURA_JANELA_PRINCIPAL, ALTURA_JANELA_PRINCIPAL
from constantes import OPCOES_APARENCIA

customtkinter.set_appearance_mode(APARENCIA_PRINCIPAL)
customtkinter.set_default_color_theme(TEMA_PRINCIPAL)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("MinervaBots - Gerenciador de Emails")
        #self.geometry(f"{LARGURA_JANELA_PRINCIPAL}x{ALTURA_JANELA_PRINCIPAL}")

        # Criando elementos do Menu Lateral
        self.menu_lateral = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.logo_label = customtkinter.CTkLabel(self.menu_lateral, text="Tipo de Rotina", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sidebar_button_1 = customtkinter.CTkButton(self.menu_lateral, text = 'Login do e-mail',command=self.janela_configuracao)
        self.sidebar_button_2 = customtkinter.CTkButton(self.menu_lateral, text = 'Abrir PlanilhaPS', command=self.abrir_planilha_ps)
        self.sidebar_button_3 = customtkinter.CTkButton(self.menu_lateral, text = 'Abri Planilha180', command=self.sidebar_button_event)


        # Posicionando elementos no Menu Lateral
        self.menu_lateral.grid(row=0, column=0)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)


        # Criando elementos do Menu de configuração
        self.menu_configuracoes = customtkinter.CTkFrame(self, width=140)
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

        # Posicionando elementos no Menu de Configuração
        self.menu_configuracoes.grid(row=0, column=1)
        self.menu_configuracoes_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.modo_aparecencia_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.modo_aparencia_opcoes.grid(row=6, column=0, padx=20, pady=(10, 10))

    # Janela de configuração que abre quando clica no botão de configuração
    def janela_configuracao(self):
        janela_config = customtkinter.CTkToplevel(self)
        janela_config.geometry("400x200")
        janela_config.wm_transient(self)

        janela_config.title('Configuração')

        label = customtkinter.CTkLabel(janela_config, text="CTkToplevel window")
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

    def evento_alterar_aparencia(self, nova_aparencia: str):
        customtkinter.set_appearance_mode(nova_aparencia)

if __name__ == "__main__":
    app = App()
    app.mainloop()