import bson


class Student:
    def __init__(self):
        self.id = str(bson.objectid.ObjectId())
        self.email = None
        self.birthday = None
        self.photo = None
        self.address = None
        self.cin = None
        self.date_debut = None
        self.date_inscrit = None
        self.date_naissence = None
        self.nom = None
        self.phoneNumber = None
        self.prenom = None
        self.cils_africane = None
        self.coiffure_homme = None
        self.coiffure_dames = None
        self.coloration = None
        self.coupe = None
        self.esthetique = None
        self.extension_cils = None
        self.maquilliage = None
        self.microblading = None
        self.microneedling = None
        self.onglerie = None
        self.paid = None
        self.price = None
        self.reste = None
        self.soin_visage = None
        self.tatouage = None

    def to_string(self):
        return f"Id: {self.id}\nPrenom: {self.prenom}\nemail: {self.email}"

    def from_json(self, json):

        if list(json.keys()).count('Id') == 1:
            self.id = json['Id']

        self.email = json['Mail']
        self.address = json['Adresse']
        self.cin = json['Cin']
        self.phoneNumber = json['NumTel']
        self.date_debut = json['DateDebut']
        self.date_inscrit = json['DateInscrit']
        self.date_naissence = json['DateNaissence']
        self.nom = json['Nom']
        self.prenom = json['Prenom']
        self.cils_africane = json['cilsAfricaine']
        self.coiffure_homme = json['coiffure_homme']
        self.coiffure_dames = json['coiffure_damme']
        self.coloration = json['coloration']
        self.coupe = json['coupe']
        self.esthetique = json['esthetique']
        self.extension_cils = json['extensionCils']
        self.maquilliage = json['maquilliage']
        self.microblading = json['microblading']
        self.microneedling = json['microneedling']
        self.onglerie = json['onglerie']
        self.paid = json['paid']
        self.price = json['price']
        self.reste = json['reste']
        self.soin_visage = json['soin_visage']
        self.tatouage = json['tatouage']

    def to_map(self):
        return {
            "Id": self.id,
            "Mail": self.email,
            'Adresse': self.address,
            'Cin': self.cin,
            'NumTel': self.phoneNumber,
            'DateDebut': self.date_debut,
            'DateInscrit': self.date_inscrit,
            'DateNaissence': self.date_naissence,
            'Nom': self.nom,
            'Prenom': self.prenom,
            'cilsAfricaine': self.cils_africane,
            'coiffure_homme': self.coiffure_homme,
            'coiffure_damme': self.coiffure_dames,
            'coloration': self.coloration,
            'coupe': self.coupe,
            'esthetique': self.esthetique,
            'extensionCils': self.extension_cils,
            'maquilliage': self.maquilliage,
            'microblading': self.microblading,
            'microneedling': self.microneedling,
            'onglerie': self.onglerie,
            'paid': self.paid,
            'price': self.price,
            'reste': self.reste,
            'soin_visage': self.soin_visage,
            'tatouage': self.tatouage,
        }
