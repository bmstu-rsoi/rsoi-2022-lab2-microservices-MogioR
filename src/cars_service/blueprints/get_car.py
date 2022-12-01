import json
from quart import Blueprint, Response, request
from .models.cars_model import CarsModel

get_car_blueprint = Blueprint('get_car', __name__, )


@get_car_blueprint.route('/api/v1/cars/<string:car_uid>', methods=['GET'])
async def get_car(car_uid: str) -> Response:
    try:
        payment = CarsModel.select().where(
            CarsModel.car_uid == car_uid
        ).get().to_dict()

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(payment)
        )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Uid not found in base.']
            })
        )