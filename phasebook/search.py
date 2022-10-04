from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    
    results = []

    if('id' in args):
        for user in USERS:
            if(args['id'] == user['id'] and user not in results):
                results.append(user)

    if('name' in args):
        param = args['name'].lower()
        for user in USERS:
            attribute = user['name'].lower()
            if(param in attribute and user not in results):
                results.append(user)

    if('age' in args):
        ages = int(args['age'])
        ages = [ages-1, ages, ages+1]
        for user in USERS:
            if(int(user['age']) in ages and user not in results):
                results.append(user)

    if('occupation' in args):
        param = args['occupation'].lower()
        for user in USERS:
            attribute = user['occupation'].lower()
            if(param in attribute and user not in results):
                results.append(user)


    if(len(results) == 0):
        return USERS            
    return results
