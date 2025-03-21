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

***
### Capturas de tela

![Screenshot_1](https://github.com/user-attachments/assets/656bd0d9-294b-4722-a950-68bab777686a)
***
![Screenshot_2](https://github.com/user-attachments/assets/f004dac2-6adb-4d7c-9cf9-5a74b7c58665)
***
![Screenshot_3](https://github.com/user-attachments/assets/06401be4-7441-4eae-aaf9-b54014edf1ee)
***
![Screenshot_4](https://github.com/user-attachments/assets/d3bf336f-3838-437e-b873-49b1be403eb4)
***
![Screenshot_5](https://github.com/user-attachments/assets/8aff5db7-a46e-491e-975d-cb6c5d26c5d6)
***
![Screenshot_6](https://github.com/user-attachments/assets/b327b4a9-d7ae-4b77-a19a-d30f7a78e1b1)
***
![Screenshot_7](https://github.com/user-attachments/assets/0b52da05-5b14-4a56-86da-ba972b247286)
***
![Screenshot_8](https://github.com/user-attachments/assets/8e47ad00-6da7-490c-b97a-6f58c6ca19d8)
***
![Screenshot_9](https://github.com/user-attachments/assets/4fc9bac9-7aab-42b2-b06d-dcab1cc2f94d)
***




