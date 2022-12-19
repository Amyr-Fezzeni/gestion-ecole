from django.http import JsonResponse, HttpResponse

import certifs.firebase.config as config
import json

from students.models import Student


def index(request):
    return HttpResponse("Students")


def get_students(request):
    docs = {"status": None, "body": []}
    try:
        for doc in config.students.get():
            docs['body'].append(doc.to_dict())
        docs['status'] = True
        return JsonResponse(docs)
    except Exception as e:
        docs['status']= False
        docs['error'] = f"{e}"
        return JsonResponse(docs)


def get_student_by_id(request, id):
    docs = {"status": None, "body": None}
    try:

        docs['body'] = config.students.where('Id', '==', id).get()[0].to_dict()
        docs['status'] = True
        return JsonResponse(docs)
    except:
        docs['status'] = False
        docs['error'] = f"Student not found"
        return JsonResponse(docs)


def get_students_by_name(request, name):

    docs = {"status": None, "body": None}
    try:
        students = []
        for doc in config.students.get():
            if name.lower() in f"{doc.to_dict()['Prenom']} {doc.to_dict()['Nom']}".lower():
                students.append(doc.to_dict())
        docs['body'] = students
        docs['status'] = True
        return JsonResponse(docs)
    except Exception as e:
        docs['status'] = False
        docs['error'] = f"{e}"
        return JsonResponse(docs)


def add_student(request):
    response = {"status": None, "body": None}
    try:
        print(request.method)
        data = json.loads(request.body)
        student = Student()
        student.from_json(data)
        if list(data.keys()).count('Id') == 1:
            response['status'] = False
            response['error'] = f"Student exist"
            return JsonResponse(response)
        config.students.document(str(student.id)).set(student.to_map())
        response['status'] = True
        response['body'] = student.to_map()
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)


def update_student(request):
    response = {"status": None, "body": None}
    try:
        data = json.loads(request.body)
        student = Student()
        student.from_json(data)
        config.students.document(str(student.id)).set(student.to_map())
        response['status'] = True
        response['body'] = student.to_map()
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)


def delete_student(request, id):
    response = {"status": None, "body": None}
    try:
        config.students.document(str(id)).delete()
        response['status'] = True
        return JsonResponse(response)
    except Exception as e:
        response['status'] = False
        response['error'] = f"{e}"
        return JsonResponse(response)