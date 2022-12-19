from .config import *


def upload_image(name, certif):
    storage.child(f"{name} {certif}.jpg").put("result.jpg")
    return f"{name} {certif}.jpg"
