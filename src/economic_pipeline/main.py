"""Entry point principal do projeto brazilian-economic-data-pipeline."""

def main():
    """Função principal do pipeline."""
    print("Brazilian Economic Data Pipeline")
    print("Para executar o extrator: python -m economic_pipeline.extractors.main")
    print("Para executar o app: python -m economic_pipeline.app.main")

if __name__ == "__main__":
    main()
