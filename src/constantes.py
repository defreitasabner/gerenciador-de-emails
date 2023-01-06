# Colunas esperadas pelas planilhas
COLUNAS_ESPERADAS_PLANILHA_PS = [
    'id',
    'nome',
    'email',
    'formulario',
    'dinamica',
    'entrevista',
    'capacitacao',
    'trainee'
]

COLUNAS_ESPERADAS_PLANILHA_180 = [
    'Carimbo de data/hora',
    'Endereço de e-mail',
    'Quem é você?',
    'Pra quem quer dar Feedback?',
    'Feedback:'
]

# Constantes relativas ao Processo Seletivo
ETAPAS_PS = {
    'Formulário': 'formulario',
    'Dinâmica': 'dinamica',
    'Entrevista': 'entrevista',
    'Capacitação': 'capacitacao',
    'Trainee': 'trainee'
} # Optei por um dicionário para apresentarmos as chaves no terminal (com caracteres especiais) e dentro do código usamos os valores (sem carecteres especiais)

# Constantes da Classe InterfaceGrafica
OPCOES_APARENCIA = [
    "Dark",
    "Light",
    "System"
]
OPCOES_TEMA = [
    "dark-blue"
]