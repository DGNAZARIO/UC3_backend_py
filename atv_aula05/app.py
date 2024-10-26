from flask import Flask
from configurations.aql_commands import create_table_bike
from configurations.database import db
from controllers.bike_controller import bike_blueprint
from repositories.bike_repository import BikeRepository
from urllib.parse import quote
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(bike_blueprint)


user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

if __name__ == '__main__':
    create_table_bike(app, db)
    app.run(debug=True)