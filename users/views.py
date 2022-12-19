from django.http import JsonResponse, HttpResponse
import json
import certifs.firebase.config as config
from users.models import User


def index(request):
    return HttpResponse("Users")


def get_users(request):
    docs = {"status": None, "body": []}
    try:
        for doc in config.users.get():
            docs['body'].append(doc.to_dict())
        docs['status'] = True
        return JsonResponse(docs)
    except Exception as e:
        docs['status']= False
        docs['error'] = f"{e}"
        return JsonResponse(docs)


def get_user_by_id(request, id):
    docs = {"status": None, "body": None}
    try:

        docs['body'] = config.users.where('id', '==', id).get()[0].to_dict()
        docs['status'] = True
        return JsonResponse(docs)
    except:
        docs['status'] = False
        docs['error'] = f"User not found"
        return JsonResponse(docs)


def add_user(request):
    try:
        print(request.method)
        data = json.loads(request.body)
        response = {"status": None, "body": None}
        user = User()
        user.from_json(data)
        config.users.document(str(user.id)).set(user.to_map())
        response['status'] = True
        response['body'] = user.to_map()
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)


def update_user(request):
    try:
        print(request.method)
        data = json.loads(request.body)
        response = {"status": None, "body": None}
        user = User()
        user.from_json(data)
        config.users.document(str(user.id)).set(user.to_map())
        response['status'] = True
        response['body'] = user.to_map()
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)


def delete_user(request, id):
    try:
        print(request.method)
        response = {"status": None, "body": None}
        config.users.document(str(id)).delete()
        response['status'] = True
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)