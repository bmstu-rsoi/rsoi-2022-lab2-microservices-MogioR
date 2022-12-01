import os
import json
import requests
from quart import Blueprint, Response, request
from .models.cars_model import CarsModel

get_cars_blueprint = Blueprint('get_cars', __name__, )


def validate_args(args):
    errors = []
    if 'page' in args.keys():
        try:
            page = int(args['page'])
            if page <= 0:
                errors.append('Page must be positive.')
        except ValueError:
            errors.append('Page is not a number')
            page = None
    else:
        errors.append('Page must be define')
        page = None

    if 'size' in args.keys():
        try:
            size = int(args['size'])
            if size <= 0:
                errors.append('Size must be positive.')
        except ValueError:
            size = None
            errors.append('Size is not a number')
    else:
        errors.append('Size must be define')
        size = None

    if 'showAll' in args.keys():
        if args['showAll'].lower() == 'true':
            show_all = True
        elif args['showAll'].lower() == 'false':
            show_all = False
        else:
            errors.append('showAll must be true or false')
            show_all = None
    else:
        show_all = False

    return page, size, show_all, errors


@get_cars_blueprint.route('/api/v1/cars/', methods=['GET'])
async def get_cars() -> Response:
    page, size, show_all, errors = validate_args(request.args)

    if len(errors) > 0:
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps({
                'errors': errors
            })
        )

    if not show_all:
        count_total = CarsModel.select().count()
        rentals = [rental.to_dict() for rental in CarsModel.select(CarsModel.availability == True).paginate(page, size)]
    else:
        count_total = CarsModel.select().count()
        rentals = [rental.to_dict() for rental in CarsModel.select().paginate(page, size)]

    return Response(
        status=200,
        content_type='application/json',
        response=json.dumps({
          "page": page,
          "pageSize": size,
          "totalElements": count_total,
          "items": rentals
        })
    )
