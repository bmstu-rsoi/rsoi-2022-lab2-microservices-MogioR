from quart import Quart
from blueprints.get_rental import get_rental_blueprint
from blueprints.get_current_rental import get_current_rental_blueprint
from blueprints.post_rental import post_rental_blueprint
from blueprints.delete_rental import delete_current_rental_blueprint
from blueprints.models.rental_model import RentalModel


app = Quart(__name__)
app.register_blueprint(get_rental_blueprint)
app.register_blueprint(get_current_rental_blueprint)
app.register_blueprint(post_rental_blueprint)
app.register_blueprint(delete_current_rental_blueprint)


def create_tables():
    # RentalModel.drop_table()
    RentalModel.create_table()


if __name__ == '__main__':
    create_tables()
    app.run(port=8003)
