"""Configurações do projeto."""

import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv('DATABASE_URL')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Flask
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')

# APIs
IBGE_API_BASE_URL = os.getenv('IBGE_API_BASE_URL', 'https://servicodados.ibge.gov.br/api/v3')
BCB_API_BASE_URL = os.getenv('BCB_API_BASE_URL', 'https://api.bcb.gov.br/dados/serie/bcdata.sgs')
