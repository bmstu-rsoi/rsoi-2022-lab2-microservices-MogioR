import os
import json
from quart import Blueprint, Response, request


get_cars_blueprint = Blueprint('get_cars', __name__,)


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
    try:
        response = requests.get(
            os.environ['CARS_SERVICE_HOST'] + ':' + os.environ['CARS_SERVICE_PORT'] + '/' + 'api/v1/cars',
            timeout=5)

        return Response(
            status=response.status_code,
            content_type='application/json',
            response=response.text
        )
    except:
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Cars service is dead.']
            })
        )

