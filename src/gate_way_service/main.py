from quart import Quart
from blueprints.get_cars_blueprint import get_cars_blueprint
from blueprints.get_rentals_blueprint import get_rentals_blueprint
from blueprints.get_rental_blueprint import get_rental_blueprint
from blueprints.post_rental import post_rentals_blueprint
from blueprints.delete_rental import delete_rental_blueprint
from blueprints.post_rental_finish import post_rental_finish_blueprint

app = Quart(__name__)
app.register_blueprint(get_cars_blueprint)
app.register_blueprint(get_rentals_blueprint)
app.register_blueprint(post_rentals_blueprint)
app.register_blueprint(delete_rental_blueprint)
app.register_blueprint(post_rental_finish_blueprint)
app.register_blueprint(get_rental_blueprint)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
