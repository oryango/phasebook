from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
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

