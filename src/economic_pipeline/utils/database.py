"""Utilitários para conexão com banco de dados."""

from sqlalchemy import create_engine
from .config import DATABASE_URL

def get_connection():
    """Criar conexão com o banco de dados."""
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL não configurada")
    
    engine = create_engine(DATABASE_URL)
    return engine.connect()
