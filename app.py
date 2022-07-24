from flask import Flask

from controller.grafana.a_base_api import a_base_api
from controller.grafana.a_daily_api import a_daily_api
from controller.grafana.base_api import base_api
import controller.grafana.base_api

app = Flask(__name__)
app.register_blueprint(base_api)
app.register_blueprint(a_base_api)
app.register_blueprint(a_daily_api)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
