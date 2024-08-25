## **Sistema de Gerenciamento de Banco de Dados SQL Web (SGBD)**

### **Visão Geral**

O Sistema de Gerenciamento de Banco de Dados SQL Web (SGBD) é uma aplicação web robusta e intuitiva, projetada para fornecer aos usuários uma interface poderosa e direta para executar comandos SQL e gerenciar interações com o banco de dados. Utiliza tecnologias web modernas para oferecer uma experiência fluida para interação com bancos de dados MySQL diretamente do navegador.

### **Principais Recursos**

1. **Execução Interativa de SQL**:
   - **Entrada de Comandos**: Usuários podem inserir e executar comandos SQL através de uma interface fácil de usar.
   - **Feedback em Tempo Real**: Os resultados das consultas SQL são exibidos imediatamente no lado direito da tela, permitindo a visualização e análise dos dados sem atraso.

2. **Interface Amigável**:
   - **Layout em Duas Painéis**: A aplicação possui um layout limpo e dividido, onde o painel esquerdo é dedicado à entrada de comandos SQL e o painel direito exibe os resultados das consultas.
   - **Design Responsivo**: A interface é projetada para ser responsiva, garantindo usabilidade em diferentes dispositivos e tamanhos de tela.

3. **Conexão Segura com o Banco de Dados**:
   - **Variáveis de Ambiente**: Detalhes sensíveis de conexão, como host do banco de dados, usuário, senha e nome do banco de dados, são gerenciados através de variáveis de ambiente para aumentar a segurança.
   - **Gerenciamento de Conexões**: Gerencia de forma segura as conexões com o banco de dados para garantir interações confiáveis e eficientes com o MySQL.

4. **Escalabilidade e Desempenho**:
   - **Gunicorn**: Utiliza Gunicorn, um servidor WSGI pronto para produção, para lidar com múltiplas solicitações simultâneas de forma eficiente.
   - **Nginx**: Emprega Nginx como um proxy reverso para gerenciar o tráfego de entrada e garantir alta disponibilidade e desempenho.

5. **Implantação com Docker**:
   - **Containerização**: A aplicação é totalmente containerizada usando Docker, facilitando a implantação, escalabilidade e gerenciamento em diferentes ambientes.
   - **Configuração Fácil**: Um `docker-compose` simplifica a configuração e a orquestração dos serviços de aplicação e banco de dados.

### **Detalhes Técnicos**

- **Backend**:
  - **Flask**: O backend é construído com Flask, um framework web Python leve e flexível.
  - **Gunicorn**: Serve como o servidor WSGI para gerenciar a aplicação Flask.
  - **MySQL**: A aplicação interage com um banco de dados MySQL para executar comandos SQL e buscar resultados.

- **Frontend**:
  - **React**: O frontend é desenvolvido com React, garantindo uma experiência de usuário dinâmica e responsiva.
  - **Layout em Duas Painéis**: Fornece uma separação clara entre a entrada de SQL e a exibição dos resultados.

- **Implantação**:
  - **Docker**: A aplicação é containerizada usando Docker para uma implantação consistente em diferentes ambientes.
  - **Nginx**: Atua como um proxy reverso para gerenciar solicitações HTTP e roteá-las para a aplicação Flask.

### **Casos de Uso**

- **Administradores de Banco de Dados**: Execute e teste consultas SQL em bancos de dados MySQL de forma eficiente.
- **Desenvolvedores**: Interaja rapidamente com bancos de dados durante as fases de desenvolvimento e depuração.
- **Analistas de Dados**: Analise e recupere dados diretamente do banco de dados sem a necessidade de ferramentas complexas.

### **Como Começar**

1. **Configuração**: Clone o repositório e configure seu ambiente. Certifique-se de ter o Docker e o Docker Compose instalados.
2. **Configuração**: Edite o arquivo `.env` para incluir as credenciais do seu banco de dados MySQL.
3. **Implantação**: Use `docker-compose up --build` para iniciar a aplicação e acessá-la através do navegador.

### **Conclusão**

O Sistema de Gerenciamento de Banco de Dados SQL Web (SGBD) é projetado para simplificar tarefas de gerenciamento de banco de dados, oferecendo uma solução eficiente e amigável para executar consultas SQL e gerenciar dados. Com sua arquitetura moderna e implantação segura, é ideal para ambientes de desenvolvimento e produção.