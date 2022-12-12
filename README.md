## Estrutura do Projeto

### data
Arquivos de entrada e saída de dados. Dentro desse diretório temos os sub-diretórios:
- `planilhas/`: onde ficaram os arquivos `.csv` para extrairmos as informações necessárias (nome, email, categorias, etc...).
- `mensagens/`: arquivos `.txt` com as mensagens de e-mail que queremos enviar.
- `logs/`: arquivos `.txt` com as informações do que foi feito em cada sessão (quais e-mails foram enviados e os possíveis erros que ocorreram).

### src
É o diretório principal, que irá conter todo nosso código python. Pode ser divido em diversos módulos, que por sua vez podem ser divididos em sub-módulos. Além disso, dentro do diretório src, também teremos o sub-diretório `tests/`.

### bin
É o diretório que irá conter os executáveis do projeto.