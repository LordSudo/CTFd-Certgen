from .routes import certificates

def load(app):
    app.register_blueprint(certificates)
