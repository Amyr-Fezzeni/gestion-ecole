# from rest_framework.response import Response
# from rest_framework.decorator import api_view
from django.http import JsonResponse, HttpResponse
from .image_processing.image_processing_service import *


def index(request):
    return HttpResponse("Certifications")


def microblading(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(microblading_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def brow(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(brow_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def extension_cils(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(extension_cils_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def keratine(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(keratine_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def microneedling(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(microneedling_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def massage(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(massage_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def coiffure_dames(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(coiffure_dames_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def coiffure_homme(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(coiffure_homme_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def esthetique(request, name, day, month, year):
    if None not in [name, day, month, year]:
        return JsonResponse(esthetique_service(name, day, month, year), safe=False)
    return JsonResponse({"Wrong data"})


def onglerie(request, name, day, month, year, day2, month2, year2):
    if None not in [name, day, month, year, day2, month2, year2]:
        return JsonResponse(onglerie_service(name, day, month, year, day2, month2, year2), safe=False)
    return JsonResponse({"Wrong data"})


def maquilliage(request, name, day, month, year, day2, month2, year2):
    if None not in [name, day, month, year, day2, month2, year2]:
        return JsonResponse(maquilliage_service(name, day, month, year, day2, month2, year2), safe=False)
    return JsonResponse({"Wrong data"})

