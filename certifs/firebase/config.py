import pyrebase
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase as fb

base_dir = os.path.dirname(os.path.abspath(__file__))
firebaseConfig = {
    "apiKey": "AIzaSyC9nfPfUqdP9gw4u1g1fpgH4VBT2Ew4W0E",
    "authDomain": "aphrodite-academy-f9520.firebaseapp.com",
    "projectId": "aphrodite-academy-f9520",
    "storageBucket": "aphrodite-academy-f9520.appspot.com",
    "messagingSenderId": "333477445878",
    "appId": "1:333477445878:web:6950c0c5852f958be5ecd7",
    "serviceAccount": {
                          "type": "service_account",
                          "project_id": "aphrodite-academy-f9520",
                          "private_key_id": "13ab5e953ef9b95971f9f9d42581b45759e33816",
                          "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCgNF+aCNW1Bmsi\nBhoZOtrCEfIC/zMBIwUX7FzPHQyK68ffF8svff1eUDn0lxH1LpyyVz0XJJG1OBH5\nwL50XuwzA8Po5yfiPg+WMMVmiuMHDTI6kedYXsynEwiwz3ptDThdYHyTTPeU79qQ\noarr3Db3irFErojgc9h+YoUt7SObT0BUye9F1swctAF8l4ElUSBxvkl3v0EvQCY9\ngN6U2my7TXMTsro6mgomGy+JBo0m0iZtFsyFuSe/zm5Q89YWeVCBViXhjNd/Bkw0\nFcu2Pmn4ZfrjwYQ6PYkjF72XMI69pmI9sGUr6wBJkfKua3hJioZkwaeueQRHhkFD\nJvYBdHaPAgMBAAECggEAGgJMD8C7Gqp3Q9epbrWAj30Er++I8yMhhWVGb1+VdOEG\nRYC3kuHJpoFa2gvutUIDMZb6iuJ71L0iJKHh/xhBZkozCQGs7CJMOy4hgN4v29S3\ndg0lpHyw4rezM6qzgwyK5+oCv5KsJ/NwJgar2PfwZUGQjwh7ngkLZFVlWXPu/HHg\nWTf5F/vXQYzYxTwomVXRQdHHJaTe5V/qr/4AQbuV4rVEsIOxMrKcNAIh5XGQKyIa\n99jq64APItqNuxeko22Bx2cIl9zmyvInXng4e6ydKqtV5O4+MoCZrb3gkjv2+qeb\nJnuUKKJVYIP9tk5K0UgXRN3Gf7UDrV5XtRsbTteALQKBgQDWwRA24ADXKFYPfSZI\n/RT5GwIb6RHME8jlr0yIAYKkD0NhqBWOw9GTB+qLmaNOpDZfQ3NJ27stV2BAZ64N\ny1uJ02DDFTjP5BHl7BMrXcs3UkUVVBDyRexChbhwDif9+TE9tr32j6FLQRzqnvbe\ntMr7QPQfpYV0I+3rPEl4AkrFSwKBgQC++T26mKtR4QH/kOTUhtS5J4LtPtQJnGkj\noP/LyOjRYP6ujo+J0/le5vR6tJ/0R1tciyeezgb6PuCW0MxMm8u4gIVO3tnYuyUb\nQ/992Wh3d56UUYrGpy4nt4Arh/QxcNREQ8zzTJd0WI7Nh66K8D2WXn9Yj1lk3GlZ\nF33SUnT9TQJ/Zy5bnAIEZVv7/XUj7+2pJgbT/JT++A6Jd9HB85bGLg0nUsRvlyh+\niSZEis5GqII9nYfK3LG2PRK+LDOkbPxH/vCQjSqlIT1zXAURMMTf3rSofJbnjYAL\nA+s7spsam+wevIgQvWZFGOMwAYpfEqHK5O1QXeQpOqQIq/1LT13KjwKBgFC+VrAX\nLpAu30Zrv6Rv4W7rWrruTn5FyFpNDvndVzp3lRa+pcezfQL4CTP8PIjuxp0JJNZK\n675QaWq6mzZkxKycgkCHjnnJHnY5uMM/8aBZTg4Nr+wv8R7PwfwlvkRNHSJDvFq9\n7mc9rhsOG+kYjCGQkK0j5rrzSgNmIEeVn2sdAoGBAI7Q22V3D3/qnolHmxbgjVoM\n76BqXjP/NhvJFhXKS3fqj9kb2yTDUlUUCYchivI0cfchtWoXTTU9/6bSYNdbc44F\n7ZaV0IBCylIqcul9N0UQK2D2ieRLvBarr1ElxuIe5o0BTE8kiQTu4rRa5hFlkNrc\nywUtm4Ebb9tRL3hi8aPx\n-----END PRIVATE KEY-----\n",
                          "client_email": "firebase-adminsdk-dx3at@aphrodite-academy-f9520.iam.gserviceaccount.com",
                          "client_id": "106122814161918650679",
                          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                          "token_uri": "https://oauth2.googleapis.com/token",
                          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                          "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dx3at%40aphrodite-academy-f9520.iam.gserviceaccount.com"
                        },
    "databaseURL":"aphrodite-academy-f9520.appspot.com"
  }

cred = credentials.Certificate(f"{base_dir}/aphrodite-academy-f9520-firebase-adminsdk-dx3at-82132d37a8.json")

firebase_admin.initialize_app(cred)

conf = pyrebase.initialize_app(firebaseConfig)

storage = conf.storage()

db = firestore.client()

users = db.collection('users')

students = db.collection('Etudiants')
