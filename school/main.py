from flask import Flask

from routes.main_route import MainRoute

app = Flask(__name__)

app.add_url_rule('/', view_func=MainRoute.as_view('/'))

app.run(host='0.0.0.0')
