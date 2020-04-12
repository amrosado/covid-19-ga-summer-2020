from flask import Flask

from flask_back_end.api.ApiEndpoints import api_blueprint

app = Flask(__name__)

prod = False

app.register_blueprint(api_blueprint)

@app.route('/')
def home():
	return "Hello, World!"

if __name__ == '__main__':
	# This is used when running locally. Gunicorn is used to run the
	# application on Google App Engine. See entrypoint in app.yaml.
	if prod:
		app.run(host='127.0.0.1', port=5000, debug=False)
	else:
		app.run(host='127.0.0.1', port=5000, debug=True)