# Sistema-Aluguel-Carros-db-mongo
Sistema em Python para gerenciar aluguel de carros, com CRUD e relatórios usando MongoDB e Oracle XE.

# 🚗 Sistema de Aluguel de Carros

Aplicação acadêmica em **Python 3.8+** que gerencia **clientes, categorias, carros e alocações** de veículos, utilizando simultaneamente **MongoDB** (NoSQL) e **Oracle XE** (SQL).

---

## 📁 Organização do Repositório

```
.
├── sql/                     # Scripts de criação de tabelas e inserts Oracle    ← opcional
│   ├── create_tables.sql
│   └── inserting_sample_data.sql
├── conexion/                # Camada de acesso a dados
│   ├── mongo_queries.py
│   ├── oracle_queries.py
│   └── passphrase/
│       ├── authentication.mongo
│       └── authentication.oracle
├── controller/              # Regras de negócio (CRUD/relatórios)
├── model/                   # Entidades de domínio (Cliente, Carro, etc.)
├── reports/                 # Relatórios prontos em Pandas
├── utils/                   # Menu, splash-screen e helpers
├── principal.py             # Ponto de entrada (menu interativo)
├── test.py                  # Testes rápidos da conexão Oracle
├── requirements.txt         # Dependências Python
└── README.md
```

*O diretório `sql/` é opcional — crie-o se for disponibilizar scripts DDL/DML.*

---

## 🗄️ Tecnologias & Bibliotecas

| Tecnologia          | Função no Projeto                      |
|---------------------|----------------------------------------|
| **Python 3.8+**     | Lógica de negócio / CLI                |
| **MongoDB 4.0+**    | Coleções `clientes`, `carro`, `categoria`, `alocacao` |
| **Oracle XE 18c/21c** | Consultas tabulares e relatórios      |
| **PyMongo**         | Driver MongoDB                         |
| **cx_Oracle**       | Driver Oracle                          |
| **Pandas**          | Exibição / manipulação de dados        |

Instalação rápida:

```bash
pip install -r requirements.txt
```
Requirements.txt contém as versões exatas utilizadas. 

---

## 🔑 Configurando Credenciais

1. **Crie**, se necessário, a pasta `conexion/passphrase/`.  
2. Adicione dois arquivos de texto simples:

| Arquivo                     | Formato                                            |
|-----------------------------|----------------------------------------------------|
| `authentication.mongo`      | `usuario_mongo,senha_mongo`                        |
| `authentication.oracle`     | `usuario_oracle,senha_oracle`                      |

As classes `MongoQueries` e `OracleQueries` fazem a leitura automática desses arquivos.

---

## 🖥️ Instalando o Oracle Instant Client (Linux)

Caso ainda não possua o *Instant Client*:

1. Baixe o pacote RPM adequado em <https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html/>.  
2. Se usar Debian/Ubuntu, converta para `.deb`:

   ```bash
   sudo alien --scripts oracle-instantclient18.5-basic-18.5.0.0.0-3.x86_64.rpm
   sudo dpkg -i oracle-instantclient18.5-basic_18.5*.deb
   ```

3. Adicione variáveis ao `~/.bash_profile`:

   ```bash
    export ORACLE_HOME=/usr/local/oracle/instantclient_18_5/lib/oracle/18.5/client64
    export LD_LIBRARY_PATH=$ORACLE_HOME/lib
    export PATH=$PATH:$ORACLE_HOME/bin
    export PATH
   ```

---

## ⚙️ Execução Passo a Passo

1. **(Opcional)** crie as tabelas Oracle e/ou coleções Mongo vazias, executando — conforme existam — os scripts em `sql/` ou um script de seed de sua preferência (por exemplo, `create_tables.sql`, `inserting_sample_data.sql`).  
2. Inicie os serviços:

   ```bash
   # MongoDB
   sudo systemctl start mongod

   # Oracle XE (pode variar conforme instalação)
   sudo systemctl start oracle-xe
   ```

3. Rode a aplicação principal:

   ```bash
   python principal.py
   ```

   - A *splash-screen* exibirá a contagem de documentos em cada coleção Mongo e os créditos do autor.
     
   - O menu interativo permite:
  
      Relatórios – listagens de carros, clientes, categorias e alocações.

      Inserir – novos registros (clientes, carros, categorias, alocações).

      Atualizar – alteração de dados existentes.

      Excluir – remoção de registros (com verificações de integridade).

      Sair – encerra o programa.

---

## 💡 Exemplos de Uso da Classe de Conexão

### Consulta simples (DataFrame)

```python
def listar_clientes(self, oracle: OracleQueries, need_connect: bool = False):
    query = """
        SELECT cpf
             , nome 
        FROM clientes
        ORDER BY nome
    """
    if need_connect:
        oracle.connect()
    print(oracle.sqlToDataFrame(query))
```

### Inserção com commit (Oracle)

```python
from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()

oracle.write("""
    INSERT INTO clientes (cpf, nome)
      VALUES ('12345678901', 'Maria Teste')
""")
```

---

## ✨ Funcionalidades Principais

- **Categorias:** código, descrição e valor da diária.  
- **Carros:** chassi, cor, modelo, marca, placa, ano e categoria.  
- **Clientes:** CPF, RG, CNH, nome e endereço.  
- **Alocações:** código de alocação, datas de saída/entrega, vínculo carro ⇄ cliente.  
- **Relatórios:** listagens tabulares via `pandas`.  

---

### Contato

- [Kayo145v@gmail.com]

---
