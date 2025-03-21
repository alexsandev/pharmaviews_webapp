# Gestão de Verbas

O projeto Gestão de Verbas consiste em uma aplicação web destinada controlar (criar, listar, editar, excluir) campanhas/ações de marketing e o orçamento destinados a elas.

![pharmaviewswebapp](https://github.com/user-attachments/assets/4b83af75-d924-4b8c-989a-b0c95e7ac734)

***
### Preparando o ambiente

Para que o programa execute localmente em sua maquina, é necessario ter o interpretador do Python (versão 3.13.2) instalado. Também são necessarias algumas bibliotecas Python, 
estas podem ser instaladas atráves do gerenciador de pacotes padrão "pip". Outro requisito importante é ter um banco de dados local configurado conforme detalharemos abaixo.

***
#### Instalando Python

Você pode baixar o interpretador do Python 3.13.2 no [site oficial](https://www.python.org/downloads/) da linguagem.

***
#### Clonando repositório

Os arquivos do projeto podem ser baixados no diretório do projeto no Github.
```
git clone https://github.com/alexsandev/pharmaviews_webapp.git
```
***
#### Criando ambiente virtual

Com os arquivos do projeto baixados, é recomendado configurar um ambiente virtual do python na pasta raiz do projeto para que não ocorram conflitos com outros pacotes globais. 
O comando a seguir cria o ambiente virtual:
```
pip venv /.venv
```
Ao executar o comando será criado o diretório \.venv\ na pasta raiz do projeto. Para ativar o ambiente virtual no console é necessario executar o script 'activate' contido na pasta:

###### Windows
```
.\.venv\Scripts\activate
```

###### Linux
```
source ./.venv/Scripts/activate
```

***
#### Instalando dependencias
Com ao ambiente virtual ativo e dentro da pasta raiz do projeto, você devera executar o comando abaixo para instalação das dependencias.
```
python -m pip install -r ./requirements.txt
```
***
#### Banco de dados
Para que o programa funcione corretamente é necessario configurar um servidor de banco de dados MySQL localmente
funcionando na porta 3306 contendo um database com o nome "pharmaviewsdb". Outra opção é modificar o campo DATABASES do arquivo ".\pharmaviews\settings.py", inserindo as informações do
banco de dados com o qual você deseja se conectar.

***
#### Executando o programa
Com todo o ambiente configurado podemos executar o programa atráves de um console no diretório raiz do projeto.
```
python .\manage.py migrate
python .\manage.py collectstatic
python .\manage.py runserver
```
Pronto! Se tudo correu bem você deve ver uma tela parecida com essa:

![runserver](https://github.com/user-attachments/assets/bbe5e9d6-4bae-4dfb-85ac-b47f3b205548)


