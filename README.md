
# IntuitiveCare - Processo seletivo - Teste-4

### Maria Luísa Barros C. Silva

Esse repositório tem por objetivo hospedar o código que que da a solução aos problemas referentes os testes:

- Teste 4 - API

Os  **Testes 1 a 3**  estão hospedados nesse [repositório](https://github.com/Marialuisabcs/IntuitiveCare-Testes-1-3.git).

### ACESSO À APLICAÇÃO NA NUVEM:
Para ter acesso a aplicação por inteiro basta acessar os links abaixo:

 - [API (backend)](https://intuitive-care-back.herokuapp.com/)
 - [Documentação da API (Swagger)](https://intuitive-care-back.herokuapp.com/docs)
 - [APP (frontend)](https://intuitive-care-front.vercel.app)

> O app apresentará as informações apenas quando requisitado pelos donos dos dados. A API está temporariamente fora do ar para não ocorrer vazamento de dados sensíveis.

### EXECUTANDO O CÓDIGO LOCALMENTE:
Foi utilizada a linguagem Python em sua versão 3.9, portanto se faz necessária a instalação de um interpretador coerente. Ao executar localmente é indicado a utilização de um ambiente virtual para rodar o backend (mais informações em [Venv](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.)). 

Para que seja possível executar o código localmente siga os seguintes passos:

 1. Clone o repositório - abra o terminal na pasta que desejar e execute o comando:
```
git clone https://github.com/Marialuisabcs/IntuitiveCare-Teste-4.git
```
**BACKEND**

 2. Se faz necessário possuir um banco PostgreSQL. Para criar a conexão do banco crie um arquivo .env e insira a url do banco como:
```
DATABASE_ULR = 'postgres://[user[:password]@][netloc][:port][/dbname]'
```
3. Crie dentro do caminho '~/services/backend' uma pasta nomeada 'static' e insira o csv (Relatorio_cadop.csv). (O arquivo não foi publicado nesse repositório por medidas de segurança).

4. Abra o terminal e vá para o caminho '~/services/backend' e rode o seguinte comando (caso esteja utilizando um ambiente virtual ative-o previamente):
```
pip install -r requirements.txt
```
5. Após a instalação de todas as dependências, execute o seguinte comando estando no caminho '~/services/backend/src' :
```
uvicorn main:app --reload
```
Dessa forma o backend estará sendo executado, na porta indicada em seu terminal (http://127.0.0.1:8000).
  

**FRONTEND**

6. No caminho '~/services/frontend', execute:
```
npm install
```
7. Como o back está sendo executado localmente é necessário alterar a url base da api em [CadOpService.js](https://github.com/Marialuisabcs/IntuitiveCare-Teste-4/blob/main/services/frontend/src/service/CadOpService.js)
```
const  base_url  =  "http://127.0.0.1:8000/" (ou a porta indicada no terminal);
```
8. Para rodar a aplicação rode o seguinte comando:
```
npm run serve
```
Tenha acesso ao front em: http://localhost:8080/ (ou na porta que for apresentada).

---

###  Tecnologias utilizadas:

|Tecnologia| Versão |Descrição| Licença|
|--|--|--|--|
| FastAPI |  0.68|Framework para desenvolvimento de RESTful APIs|[MIT license](https://github.com/tiangolo/fastapi/blob/master/LICENSE)
| PostgreSQL|  14.3| Sistema de gerenciamento de banco de dados relacional (ORDBMS) |[MIT license](https://www.postgresql.org/about/licence/)
| Vue.js|  2.6.14|Framework para criação de interfaces de usuário|[MIT license](https://github.com/vuejs/core/blob/main/LICENSE)
| Vuetify |  2.6|Biblioteca de componentes UI|[MIT license](https://github.com/vuetifyjs/vuetify/blob/master/LICENSE.md)
| Heroku| -- |Ferramenta que permite hospedagem de projetos virtuais em nuvem|[License](https://www.heroku.com/policy/heroku-elements-licensing)
| Vercel|  --|Ferramenta que permite hospedagem de sites estáticos em nuvem|[Apache-2.0 license](https://github.com/vercel/vercel/blob/main/LICENSE)