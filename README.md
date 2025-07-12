# Dashboard da Economia Brasileira
## 🎯 Visão Geral
Pipeline ELT completo de dados econômicos do Brasil com Flask, dbt, Supabase (PostgreSQL) e dashboard interativo

## Arquitetura inicial
````
projeto-dashboard/
├── data/
│   ├── raw/              # Dados brutos
│   └── processed/        # Dados processados
├── dbt_project/
│   ├── models/
│   │   ├── staging/      # Modelos de staging
│   │   ├── intermediate/ # Transformações intermediárias
│   │   └── marts/        # Modelos finais
│   └── dbt_project.yml
├── app/
│   ├── app.py           # Flask application
│   ├── templates/       # HTML templates
│   └── static/          # CSS/JS
├── scripts/
│   ├── extract.py       # Scripts de extração
│   └── load.py          # Scripts de carregamento
└── requirements.txt
````

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