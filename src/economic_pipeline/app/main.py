"""Aplicação Flask principal."""

from flask import Flask

def create_app():
    """Factory function para criar a aplicação Flask."""
    app = Flask(__name__)
    
    @app.route('/')
    def dashboard():
        return "<h1>Brazilian Economic Data Pipeline</h1><p>Dashboard em desenvolvimento...</p>"
    
    return app

def run():
    """Executar a aplicação Flask."""
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    run()
