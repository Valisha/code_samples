#!/usr/bin/env python3
## Trying to import the unbossed_EEG project into a flask app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    if test_config is None:
        ## using the unbossed EEG file, need to change the input function
        app.config.from_pyfile('/Users/valishashah/codes/code_samples/unbossed_spectral_analysis_on_EEG/unbossed_spectral_analysis_on_EEG.py', silent=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/hello')
    def hello():
        return 'Hello, World! Trying to run the unbossed project'
    return app
