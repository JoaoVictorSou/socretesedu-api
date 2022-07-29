# socretesedu-api
API para uma escola fictícia utilizando o framework, de Python, Django Rest. Inspirado no primeiro curso de Django Rest da Alura.

## Para prosseguir utilizando a aplicação
É necessário que tenha instalado em sua máquina alguns pacotes, juntamente com o interpretador do Python
[Instale o interpretador do Python](https://www.python.org/downloads/).
### instale as dependências do projeto
```
pip install -r requirements.txt
```
*A ação pode ser feita utilizando um terminal, com tal permissão, aberto na pasta socretesedu-api* 
### Conexão com o banco de dados
É muito simples utilizar as tecnologias de persistência de dados deste projeto. Basta ter o banco de dados utilizado, MySQL, corretamente instalado em sua máquina.
Portanto, [instale o MySQL](https://www.mysql.com/downloads/).
#### Crie um banco de dados para o projeto
Após a instalação, use o seu cliente MySQL para criar um banco de dados que será utilizado pelo Django. Pode ser feito da seguinte forma:
```
mysql -u (nome do usuário) -p (senha)

create database socretesedu;
```
#### Corrija o nome de usuário e a senha
Dentro da pasta setup do projeto existe o arquivo de configurações, o settings.py, procure por ele e substitua o nome de usuário e o password para o referentes de seu MySQL.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'socretesedu',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': '127.0.0.1',
    }
}
```
*O 'USER' condiz ao nome de usuário e o 'PASSWORD' a senha.*
#### Crie as tabelas do projeto
As tabelas do projeto podem facilmente serem criadas utilizando uma funcionalidade do Django. Execute o seguinte comando.
```
python manage.py migrate
```