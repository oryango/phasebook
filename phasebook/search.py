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
    priority = []
    arg = ['id','name','age','occupation']

    for user in USERS:
        for index in range(4):
            if(arg[index] in args):
                if(check_arg(arg[index], args, user)):
                    results.append(user)
                    priority.append(index)
                    break


    ordered_results = []
    for index in range(4):
        for iindex in range(len(results)):
            if(priority[iindex] == index):
                ordered_results.append(results[iindex])

    """
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
   
    """
    if(len(ordered_results) == 0):
        return USERS            
    return ordered_results

def check_arg(arg, args, user):
    if(arg == 'id'):
        return (args['id'] == user['id'])
    elif(arg == 'age'):
        ages = int(args['age'])
        ages = [ages-1, ages, ages+1]
        return (int(user['age']) in ages)
    else:
        val1 = args[arg].lower()
        val2 = user[arg].lower()
        return (val1 in val2)

