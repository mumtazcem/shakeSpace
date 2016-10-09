'''
Created on Oct 8, 2016

@author: mumta
'''
from flask import Flask
import os

from handlers import site
from cem import cem
from ipek import ipek
from batuhan import batuhan

def create_app():
    app = Flask(__name__)
    port = int(os.getenv("VCAP_APP_PORT"))
    app.config.from_object('settings')
    # blueprints
    app.register_blueprint(site)
    app.register_blueprint(cem)
    app.register_blueprint(ipek)
    app.register_blueprint(batuhan)
    
    return app

def main():
    app = create_app()
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
