# Projeto_MVC

Esse projeto é voltado para uma prova de Framework FullStack. 
- O projeto é uma ideia de inserir informações de diversos jogos, aonde agora o usuario consegue realizar o seu cadastro com CPF, Nome e Senha.
- O cadastro e os jogos são armazenados no banco de dados MySQL. O arquivo jogoteca.db é aonde esta os scripts que usei para criação de tabelas e database dentro do MySQL.
- Atraves das rotas o usuario consegue:
    - Cadastrar o seu perfil.
    - Fazer o login. Se a senha e o CPF estiver errado, não sera possivel entrar.
    - Inserir jogos na jogoteca
    - Consultar os jogos por categoria(Tiro, futebol, Corrida, etc...)
  
 Rotas por acesso local:
  - http://127.0.0.1:5000/ = Realizar cadastro
  - http://127.0.0.1:5000/login = Realizar o Login
  - http://127.0.0.1:5000/criarconsulta = Realizar consulta das categorias
  - http://127.0.0.1:5000/novoJogo = Inserir jogo na Jogoteca
  - http://127.0.0.1:5000/jogos = Todos os jogos da jogoteca
 
