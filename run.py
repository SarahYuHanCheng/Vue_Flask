from flask import Flask, render_template, jsonify
# from random import *
# from flask_cors import CORS
# import requests

from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
# app.config['SQLAlCHEMY_DATABASE_URI']='postgresql://0618patrick:0618@localhost/even_more_awesome_application'
POSTGRES = {
    'user': '0618patrick',
    'password': '0618',
    'db': 'even_more_awesome_application',
    'host': 'localhost',
    'port': '5432',
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['DEBUG'] = True
db = SQLAlchemy(app)
from models import User
db.init_app(app)

@app.route('/')
def index():
		return "<h1> hello my flaskkk</h1>"	
if __name__ == '__main__':
	app.run()


# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# @app.route('/api/random')
# def random_number():
# 	response = {
# 		'randomNumber': randint(1,100)
# 	}
# 	return jsonify(response)

# @app.route('/', defaults={'path':''})
# @app.route('/<path:path>')
# def catch_all(path):
# 	if app.debug:
# 		return requests.get('http://localhost:8080/{}'.format(path)).text
# 	return render_template("index.html")