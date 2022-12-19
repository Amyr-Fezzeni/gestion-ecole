import bson


class User:
    def __init__(self):
        self.id = str(bson.objectid.ObjectId())
        self.name = None
        self.email = None
        self.password = None
        self.birthday = None
        self.photo = None
        self.sexe = None

    def to_string(self):
        return f"Id: {self.id}\nName: {self.name}\nemail: {self.email}\nPassword: {self.password}\nBirthday: {self.birthday}\nPhoto: {self.photo}\nSexe: {self.sexe}\n"

    def from_json(self, json):
        if list(json.keys()).count('Id') == 1:
            self.id = json['id']
        self.name = json['name']
        self.email = json['email']
        self.password = json['password']
        self.birthday = json['birthday']
        self.photo = json['photo']
        self.sexe = json['sexe']

    def to_map(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "photo": self.photo,
            "sexe": self.sexe,
        }

