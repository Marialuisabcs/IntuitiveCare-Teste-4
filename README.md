# IntuitiveCare - Processo seletivo - Teste-4

### Maria Luísa Barros C. Silva

Esse repositório tem por objetivo hospedar o código que que da a solução aos
problemas referentes os testes:

- Teste 4 - API

(Os **Testes 1 a 3 ** estão hospedados nesse [repositório](https://github.com/Marialuisabcs/IntuitiveCare-Testes-1-3.git) )

Para que seja possível executar o código siga os seguintes passos:

Foi utilizada a linguagem Python em sua versão 3.9, portanto se faz
necessário a instalação de um interpretador corente.

1. Clone o repositório:
   ```
   git clone https://github.com/Marialuisabcs/Teste-01_02.git
   ```

**BACKEND**

2. Se faz necessário possuir um banco postgres local e atulizar suas credenciais em service/backend/database/database.py

   ```
   db = peewee.PostgresqlDatabase("nome", user="user", password="pass", host="127.0.0.1", port=5432)
   ```

3. Abra o cmd e vá para o caminho services/backend e rode o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

4. Após a instalação de todas as dependências, execute o seguinte comando estando no caminho services/backend/src:

   ```
   uvicorn main:app --reload
   ```

   Dessa forma o backend estará sendo executado

**FRONTEND**

5. Agora no caminho services/frontend, execute:

   ```
   npm install
   ```

6. PAra rodar a aplicação rode o seguinte comando:
   ```
   npm run serve
   ```

Tenha acesso ao front em: http://localhost:8080/ (ou na porta que for apresentada)
