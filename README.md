## Introdução do projeto

Nesse projeto foi desenvolvido um sistema de vendas de produtos, usando a ferramenta de front-end Streamlit, a cada venda foi inserido os dados no banco de dados PostgreSQL. Para garantir a integridade e validação dos dados, foi utilizado o Pydantic, e além disso foi implementado o DBT para realizar a transformação dos dados entre as camadas silver e gold.

Também realizado teste usando inteligencia artificial, com as APIs da OpenAI e Groq, com base nos dados vendidos.

Um projeto simples, criado para testar e validar cada ferramenta.

## Tecnologias utilizadas

### Streamlit
Uma biblioteca em Python que permite criar aplicações web interativas para ciência de dados e machine learning de forma rápida e fácil.

### Pydantic
Uma biblioteca que valida e define configurações de dados em Python, utilizando anotações de tipo para garantir que os dados estejam corretos e completos.

### Psycopg2
Um adaptador para PostgreSQL em Python, permitindo a interação com bancos de dados PostgreSQL através de consultas SQL e manipulação de dados.

### PostgreSQL
Um sistema de gerenciamento de banco de dados relacional e objeto que é robusto, escalável e suporta extensões, transações e uma rica linguagem de consulta.

### MkDocs
Uma ferramenta para criar documentação estática, que utiliza Markdown e gera sites de documentação a partir de arquivos Markdown de maneira simples.

### Dbt
Uma ferramenta de transformação de dados que permite modelar, testar e documentar dados em um ambiente de data warehouse, facilitando o fluxo de trabalho de análise.

-----------------------------------------------------------------
## Comandos úteis:

#### Streanlit:
- streanlit run app.py - iniciar server

#### MkDocs
- Lib instaladas: poetry add mkdocs mkdocs-material mkdocstrings mkdocstrings-python
- mkdocs new .
- mkdocs serve
- fazer deploy
- mkdocs build
- mkdocs gh-deploy

#### dbt
- poetry add dbt-postgre
- dbt init dbt_vendas
- dbt debug
- dbt docs generate - gerar documentacao
- dbt docs serve --port 8080 - iniciar server
