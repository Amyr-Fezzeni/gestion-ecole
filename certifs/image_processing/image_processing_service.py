from PIL import Image, ImageFont, ImageDraw
from ..firebase.upload_file import upload_image
from ..firebase.config import base_dir


def microblading_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/microblading.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'microblading')
    except Exception as e:
        return f"{e}"


def brow_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/brow.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'brow')
    except Exception as e:
        return f"{e}"


def extension_cils_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/extension_cils.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'extension_cils')
    except Exception as e:
        return f"{e}"


def keratine_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/keratine et proteine.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'keratine et proteine')
    except Exception as e:
        return f"{e}"


def microneedling_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/microneedling.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'microneedling')
    except Exception as e:
        return f"{e}"


def massage_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/massage.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((2100 - int(len(name) * 28.5), 1540), name, (0, 0, 0),
                            font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2356, 2212), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'massage')
    except Exception as e:
        return f"{e}"


def coiffure_dames_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/coiffure dames.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((1229, 1480), name, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((609, 2058), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'coiffure dames')
    except Exception as e:
        return f"{e}"


def coiffure_homme_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/coiffure homme.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((923, 967), name, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 90))
        image_editable.text((1010, 1407), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 45))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'coiffure homme')
    except Exception as e:
        return f"{e}"


def esthetique_service(name, day, month, year):
    try:
        date = f"{day}/{month}/{year}"
        my_image = Image.open(f"{base_dir}/assets/esthetique.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((1653, 1343), name, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 110))
        image_editable.text((1520, 1960), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 60))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'esthetique')
    except Exception as e:
        return f"{e}"


def onglerie_service(name, day, month, year, day2, month2, year2):
    try:
        date = f"{day}/{month}/{year}"
        date2 = f"{day2}/{month2}/{year2}"
        my_image = Image.open(f"{base_dir}/assets/onglerie.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((1149, 1585), name, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2166, 975), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 90))
        image_editable.text((900, 1770), date2, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 90))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'onglerie')
    except Exception as e:
        return f"{e}"


def maquilliage_service(name, day, month, year, day2, month2, year2):
    try:
        date = f"{day}/{month}/{year}"
        date2 = f"{day2}/{month2}/{year2}"
        my_image = Image.open(f"{base_dir}/assets/maquillage.jpg")
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((1149, 1505), name, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 120))
        image_editable.text((2166, 980), date, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 90))
        image_editable.text((800, 1716), date2, (0, 0, 0), font=ImageFont.truetype(f'{base_dir}/assets/arial.ttf', 90))
        my_image.save(f"{base_dir}/result.jpg")
        return upload_image(name, 'maquillage')
    except Exception as e:
        return f"{e}"
