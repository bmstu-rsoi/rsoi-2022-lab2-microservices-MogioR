import json
from quart import Blueprint, Response, request
from .models.rental_model import RentalModel


get_rental_blueprint = Blueprint('get_rental', __name__,)


@get_rental_blueprint.route('/api/v1/rental/<string:rental_uid>', methods=['GET'])
async def get_rental(rental_uid: str) -> Response:
    try:
        rental = RentalModel.select().where(
            RentalModel.rental_uid == rental_uid
        ).get().to_dict()

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(rental)
        )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Uid not found in base.']
            })
        )