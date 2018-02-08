from flask import request
from flask.views import MethodView



class MainRoute(MethodView):
    def get(self):
        return 'am suprascris'

    def post(self):
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        return_value = name + ' ' + age + ' ' + address
        return return_value