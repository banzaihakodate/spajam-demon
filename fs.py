import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def firestore_init():
    cred = credentials.Certificate(os.environ['FIREBASE_AUTH_KEY'])
    firebase_admin.initialize_app(cred)
    return firestore.client()

def get_firestore_time():
    return firestore.SERVER_TIMESTAMP


# Usage
# Initialize firestore
# db = firestore_init()

# Insert data to table
# db.collection('messages').add({})

# Get data from table
# docs = db.collection('messages').where('name', '==', "aaaa").get()
# for doc in docs:
#    print(doc.to_dict()['text'])
