'''
Created on Oct 8, 2016

@author: mumta
'''
from flask import Flask

from handlers import site
from cem import cem

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    # blueprints
    app.register_blueprint(site)
    app.register_blueprint(cem)
    
    return app

def main():
    app = create_app()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()