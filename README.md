# FastApi


### **GIF de Demonstração**

Veja o **GIF** abaixo para entender o fluxo de interação com o aplicativo:

![Demonstração do aplicativo](app/images/app_example.gif)


## Visão Geral

Este projeto é um **Fast API**.


## Estrutura do Projeto

## **Instalar pyenv**
Referência: **https://pyenv-win.github.io/pyenv-win/**

## **Instalar Python**
Vá até dentro da pasta de seu projeto e instale a versão de python que deseja utilizar nele.

**Terminal**
C:\Users\klaus\FastApi> pyenv update

C:\Users\klaus\FastApi> pyenv install --list

C:\Users\klaus\FastApi> pyenv install 3.11.6

C:\Users\klaus\FastApi> pyenv global 3.11.6

## **Instalar o pipx**
Dentro da pasta de seu projeto instale o pipx

**Terminal**
C:\Users\klaus\FastApi> pip install pipx

C:\Users\klaus\FastApi> pipx --version

C:\Users\klaus\FastApi> pipx ensurepath

## **Instalar Poetry**
Dentro da pasta de seu projeto instale e atualize o Poetry

**Terminal**
C:\Users\klaus\FastApi> pipx install poetry
C:\Users\klaus\FastApi\app> pipx upgrade poetry


## **Criação projeto FastApi**
Agora que temos instalado e configurado o Python e Poetry vamos dar inicio a criação do projeto

**Criar projeto python utilizando Poetry**
C:\Users\klaus\FastApi> poetry new app

C:\Users\klaus\FastApi> cd .\app\

C:\Users\klaus\FastApi\app> dir
Diretório: C:\Users\klaus\FastApi\app


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26/11/2024     09:06                app
d-----        26/11/2024     09:06                tests
-a----        26/11/2024     09:06            311 pyproject.toml
-a----        26/11/2024     09:06              0 README.rst

**Devemos dizer ao pyenv qual versão do python será usada nesse diretório será criado um arquivo ".python-version" **
C:\Users\klaus\FastApi\app> pyenv local 3.11.6

C:\Users\klaus\FastApi\app> dir


    Diretório: C:\Users\klaus\FastApi\app


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26/11/2024     09:06                app
d-----        26/11/2024     09:06                tests
-a----        26/11/2024     09:08              8 .python-version
-a----        26/11/2024     09:06            311 pyproject.toml
-a----        26/11/2024     09:06              0 README.rst

**Alterar a linha de configuração "pyproject.toml" para que utlize a versão exata do python**
[tool.poetry.dependencies]
python = "3.10.*"

**inicialize o ambiente virtual com Poetry e instalaremos o FastAPI**
C:\Users\klaus\FastApi\app> poetry install

C:\Users\klaus\FastApi\app> poetry add 'fastapi[standard]'

**Habilitar ambiente virtual com Poetry para que resolva dependencias do projeto**
C:\Users\klaus\FastApi\app> poetry shell

**Executar o main.py para subir aplicação FastAPI**
 C:\Users\klaus\FastApi\app> fastapi dev .\main.py

**Acessar via browser a roda "/"**
Veja que agora conseguimos consumir ApiFast que esta servido HTTP na rota "/" e podemos ver o resultado que é o dicionário "menssage: "Hello World".

http://127.0.0.1:8000/ 

## ** Uvicorn ** 
O FastAPI é ótimo para criar APIs, mas não pode disponibilizá-las na rede sozinho, Para podermos acessar essas APIs por um navegador ou de outras aplicações clientes, é necessário um servidor. Uvicorn atua como esse servidor, disponibilizando a API do FastAPI em rede. Isso permite que a API seja acessada de outros dispositivos ou programas. que podemos ver no trecho do log da FastAPI.

**Trecho do log**
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17940] using WatchFiles
INFO:     Started server process [24828]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


## **Ferramentas de testes para o desenvolvedor**

**taskipy**
Ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.

**pytest**
Ferramenta para escrever e executar testes

**ruff**
Um analisador estático de código (um linter), para dizer se não estamos infringido alguma boa prática de programação;
Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.

**--group dev**
Para instalar essas ferramentas que usaremos em desenvolvimento, podemos usar um grupo (--group dev) do poetry focado nelas, para não serem instaladas quando nossa aplicação estiver em produção.

**terminal**
C:\Users\klaus\FastApi\app> poetry add --group dev pytest pytest-cov taskipy ruff

**[tool ruff]**
Na configuração global do Ruff queremos alterar somente duas coisas. O comprimento de linha para 79 caracteres (conforme sugerido na PEP-8) e em seguida, informaremos que o diretório de migrações de banco de dados será ignorado na checagem e na formatação

**Adicione no arquivo "pyproject.toml" o trecho abaixo**
[tool.ruff]
line-length = 79
extend-exclude = ['migrations']

**Linter**
Durante a análise estática do código, queremos buscar por coisas específicas. No Ruff, precisamos dizer exatamente o que ele deve analisar. Isso é feito por códigos. Usaremos estes:

I (Isort): Checagem de ordenação de imports em ordem alfabética
F (Pyflakes): Procura por alguns erros em relação a boas práticas de código
E (Erros pycodestyle): Erros de estilo de código
W (Avisos pycodestyle): Avisos de coisas não recomendadas no estilo de código
PL (Pylint): Como o F, também procura por erros em relação a boas práticas de código
PT (flake8-pytest): Checagem de boas práticas do Pytest

**[tool ruff lint]**

**Adicione no arquivo "pyproject.toml" o trecho abaixo**

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

**Formatter**
A formatação do Ruff praticamente não precisa ser alterada. Pois ele vai seguir as boas práticas e usar a configuração global de 79 caracteres por linha. A única alteração que farei é o uso de aspas simples ' no lugar de aspas duplas ".

**Adicione no arquivo "pyproject.toml" o trecho abaixo**
[tool.ruff.format]
preview = true
quote-style = 'single'

**pytest**
O Pytest é uma framework de testes, que usaremos para escrever e executar nossos testes. O configuraremos para reconhecer o caminho base para execução dos testes na raiz do projeto 

**Adicione no arquivo "pyproject.toml" o trecho abaixo**
[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'

**Taskipy**
A ideia do Taskipy é ser um executor de tarefas (task runner) complementar em nossa aplicação. No lugar de ter que lembrar comandos como o do fastapi, que vimos na execução da aplicação, que tal substituir ele simplesmente por task run?

Isso funcionaria para qualquer comando complicado em nossa aplicação. Simplificando as chamadas e também para não termos que lembrar de como executar todos os comandos de cabeça.

Alguns comandos que criaremos agora no início:

**Adicione no arquivo "pyproject.toml" o trecho abaixo**
[tool.taskipy.tasks]
lint = 'ruff check .; ruff check . --diff'
format = 'ruff check . --fix && ruff format .'
run = 'fastapi dev app/app/main.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=app -vv'
post_test = 'coverage html'

## **Utilização dos comandos de testes**
Os comandos definidos fazem o seguinte:

lint: Executa duas variações da checagem:

ruff check --diff: Mostra o que precisa ser alterado no código para que as boas práticas sejam seguidas

ruff check: Mostra os códigos de infrações de boas práticas

&&: O duplo & faz com que a segunda parte do comando só seja executada se a primeira não der erro. Sendo assim, enquanto o --diff apresentar erros, ele não executará o check

format: Executa duas variações da formatação:

ruff check --fix: Faz algumas correções de boas práticas automaticamente

ruff format: Executa a formatação do código em relação as convenções de estilo de código

run: executa o servidor de desenvolvimento do FastAPI

pre_test: executa a camada de lint antes de executar os testes

test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura

post_test: gera um report de cobertura após os testes

Para executar um comando, é bem mais simples, precisando somente passar a palavra task <comando>.

## **Estrutura de teste**
Está parte é muito importante para mais detalhes veja o script em **app/app/tests/test_app.py** Com ele podemos consumir a nossa FastApi que está servindo um dicionário Hello Wolrd.

**Terminal**
C:\Users\klaus\FastApi\app> task test