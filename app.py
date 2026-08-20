from flask import Flask
from flasgger import Swagger
from models import db, migrate
# from config import Development
# from flask_jwt_extended import JWTManager
from config import jwt

def create_app():

    app= Flask(__name__)

    app.config.from_pyfile('config.py')
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Secure API Documentation",
            "description": "API using JWT Bearer token authentication.",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        }
    }
    swagger = Swagger(app, template=swagger_template)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from routes import main
    app.register_blueprint(main)
    with app.app_context():
        # from models import db
        db.create_all()
        print("Tables created successfully")
    return app
# if __name__ == '__main__':
#     app.run(debug=True)
