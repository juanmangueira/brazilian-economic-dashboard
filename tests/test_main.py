"""Testes básicos do projeto."""

def test_import():
    """Testar se conseguimos importar o módulo principal."""
    try:
        import economic_pipeline
        assert True
    except ImportError:
        assert False, "Não foi possível importar economic_pipeline"
