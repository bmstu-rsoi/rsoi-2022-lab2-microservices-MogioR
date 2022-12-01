from quart import Quart
from blueprints.get_cars import get_cars_blueprint
from blueprints.models.cars_model import CarsModel

app = Quart(__name__)
app.register_blueprint(get_cars_blueprint)


def create_tables():
    # CarsModel.drop_table()
    CarsModel.create_table()

    CarsModel.get_or_create(
        id=1,
        car_uid="109b42f3-198d-4c89-9276-a7520a7120ab",
        brand="Mercedes Benz",
        model="GLA 250",
        registration_number="ЛО777Х799",
        power=249,
        type="SEDAN",
        price=3500,
        availability=True
    )


if __name__ == '__main__':
    create_tables()
    app.run(port=8001)
