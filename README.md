## **Requisitos**

Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente:
- [Python 3.10+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/)

---

## **Configuração do Ambiente**

### 1. Clone o Repositório

git clone https://github.com/seu-usuario/sua-api.git
cd sua-api

### 2. Crie um Ambiente Virtual

python -m venv venv


### 3. Ative o Ambiente Virtual
Windows:
venv\Scripts\activate

Linux/MacOS:
source venv/bin/activate


### 4. Instale as Dependências
pip install -r requirements.txt
Banco de Dados

### 5. Realize as Migrações
Certifique-se de que o banco de dados foi configurado e crie as tabelas:
python manage.py makemigrations
python manage.py migrate

## Criar um Superusuário
Para acessar a interface de administração do Django:

python manage.py createsuperuser
Siga as instruções para configurar um nome de usuário, email e senha.

Executar a Aplicação
Inicie o servidor de desenvolvimento:
python manage.py runserver
Acesse a aplicação em http://127.0.0.1:8000/.

Endpoints da API
Listar Produtos (GET):
GET /api/produtos/
Criar Produto (POST):
POST /api/produtos/
{
  "nome": "Produto X",
  "descricao": "Descrição do Produto X",
  "preco": 100.00,
  "estoque": 50
}
#### Nota: Para testar os endpoints, use ferramentas como Postman ou Insomnia.

## Acessar o Django Admin
A interface administrativa está disponível em: http://127.0.0.1:8000/admin/
Utilize o superusuário criado anteriormente para fazer login.

### Contribuindo
Faça um fork do projeto.
Crie uma branch para a sua feature ou correção:
git checkout -b minha-feature
Realize os commits:
git commit -m "Minha feature incrível"
Envie as alterações:
git push origin minha-feature
Abra um Pull Request.

Contato
Para dúvidas ou sugestões:

Email: and_bas7@hotmail.com
LinkedIn: [Seu Perfil](https://www.linkedin.com/in/andr%C3%A9-luiz-636468244/)








