from flask import Flask
from flasgger import Swagger
from models import db, migrate
# from config import Development

def create_app():

    app= Flask(__name__)
    swagger = Swagger(app)
    app.config.from_pyfile('config.py')
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
