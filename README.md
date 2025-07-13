# Dashboard da Economia Brasileira
## 🎯 Visão Geral
Pipeline ELT completo de dados econômicos do Brasil com Flask, dbt, Supabase (PostgreSQL) e dashboard interativo


## 🛠️ Stack Técnico
- **Simulação de cliente e assistente de IA**: Perplexity com modelo Claude 4
- **Backend**: Python, Flask
- **Transformação**: dbt Core
- **Banco**: PostgreSQL (Supabase)
- **Qualidade**: Great Expectations
- **Deploy**: Railway

## 📊 Funcionalidades
- Extração automatizada de dados do IBGE
- Transformações com dbt
- Dashboard responsivo
- Testes de qualidade automatizados

## Pipeline
| Fase ELT | Tecnologia |
| -------- | ---------- |
| Extract | Python (requests) |
| Load | Python + Supabase (PostgreSQL) |
| Transform | dbt (SQL) |

## Cronograma de Execução
| Semana | Foco | Entregável |
| ------ | ---- | ---------- |
| 1 | Setup, Infraestrutura | Ambiente configurado |
| 2 | Pipeline de dados | dbt models funcionando |
| 3 | Prototipagem Dashboard Flask | Protótipo de alta fidelidade |
| 4 | Dashboard Flask | Interface básica |
| 5 | Deploy + Refinamento | Projeto online |

## 🚀 Como Executar
[em breve, instruções aqui]

## 📈 Resultados
[em breve, screenshots aqui]

## Arquitetura inicial
````
brazilian-economic-data-pipeline/
├── pyproject.toml              # Poetry config (substitui requirements.txt)
├── poetry.lock                 # Lock file automático do Poetry
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── src/
│   └── economic_pipeline/      # Pacote Python principal
│       ├── __init__.py
│       ├── main.py            # Entry point principal
│       ├── app/               # Flask application
│       │   ├── __init__.py
│       │   ├── main.py        # Flask app principal
│       │   ├── routes/        # Rotas organizadas
│       │   │   ├── __init__.py
│       │   │   └── dashboard.py
│       │   ├── templates/     # HTML templates
│       │   │   ├── base.html
│       │   │   ├── dashboard.html
│       │   │   └── components/
│       │   └── static/        # CSS/JS/Assets
│       │       ├── css/
│       │       ├── js/
│       │       └── img/
│       ├── extractors/        # Scripts de extração (ex-scripts/)
│       │   ├── __init__.py
│       │   ├── main.py
│       │   ├── ibge.py       # Extrator do IBGE
│       │   └── bcb.py        # Extrator do Banco Central
│       ├── loaders/          # Scripts de carregamento
│       │   ├── __init__.py
│       │   ├── main.py
│       │   └── database.py
│       └── utils/            # Utilitários compartilhados
│           ├── __init__.py
│           ├── database.py   # Conexões de banco
│           ├── config.py     # Configurações
│           └── validators.py # Validações
├── dbt_project/              # Projeto dbt (mantido separado)
│   ├── dbt_project.yml
│   ├── profiles.yml
│   ├── models/
│   │   ├── staging/
│   │   │   ├── _staging.yml
│   │   │   ├── stg_pib.sql
│   │   │   └── stg_inflacao.sql
│   │   ├── intermediate/
│   │   │   ├── _intermediate.yml
│   │   │   └── int_indicadores_economicos.sql
│   │   └── marts/
│   │       ├── _marts.yml
│   │       ├── dim_regioes.sql
│   │       └── fct_indicadores_mensais.sql
│   ├── macros/              # Macros dbt customizadas
│   ├── tests/               # Testes específicos do dbt
│   └── docs/                # Documentação do dbt
├── data/                    # Dados de exemplo/desenvolvimento
│   ├── raw/                 # Dados brutos
│   │   └── .gitkeep
│   ├── processed/           # Dados processados
│   │   └── .gitkeep
│   └── sample/              # Dados de exemplo para testes
├── tests/                   # Testes Python
│   ├── __init__.py
│   ├── conftest.py         # Configuração pytest
│   ├── test_extractors/
│   ├── test_loaders/
│   ├── test_app/
│   └── test_utils/
├── docs/                    # Documentação do projeto
│   ├── setup.md
│   ├── architecture.md
│   └── deployment.md
└── deployment/              # Configurações de deploy
    ├── docker-compose.yml
    ├── Dockerfile
    └── railway.toml
````
