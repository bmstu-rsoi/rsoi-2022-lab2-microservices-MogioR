from quart import Quart
from blueprints.get_cars_blueprint import get_cars_blueprint


app = Quart(__name__)
app.register_blueprint(get_cars_blueprint)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
