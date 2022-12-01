import json
from quart import Blueprint, Response, request
from .models.rental_model import RentalModel


delete_current_rental_blueprint = Blueprint('delete_current_rental', __name__,)


@delete_current_rental_blueprint.route('/api/v1/rental/<string:rental_uid>', methods=['DELETE'])
async def delete_current_rental(rental_uid: str) -> Response:
    if 'X-User-Name' not in request.headers.keys():
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Request has not X-User-Name header!']
            })
        )

    user = request.headers['X-User-Name']

    try:
        rental = RentalModel.select().where(
            RentalModel.username == user and RentalModel.rental_uid == rental_uid
        ).get().delete_instance()

        return Response(
            status=204,
            content_type='application/json',
        )
    except Exception as e:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Uid not found in base.']
            })
        )