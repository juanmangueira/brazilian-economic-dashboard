"""Configuração do pytest."""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path para importações
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
