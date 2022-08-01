import logging

from flask import Flask

from controller.grafana.a_base_api import a_base_api
from controller.grafana.a_daily_index_api import a_daily_index_api
from controller.grafana.us_daily_k_api import us_daily_k_api
from controller.grafana.base_api import base_api
from utils.scheduler_utils import scheduler_start

app = Flask(__name__)
app.register_blueprint(base_api)
app.register_blueprint(a_base_api)
app.register_blueprint(a_daily_index_api)
app.register_blueprint(us_daily_k_api)

logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
    scheduler_start()
