from flask import Flask, request
from flask_basicauth import BasicAuth
import os
from pymongo import MongoClient
from bson.json_util import dumps
import datetime
import re


mongo_user = os.environ['CONFIG_MONGODB_ADMINUSERNAME']
mongo_password = os.environ['CONFIG_MONGODB_ADMINPASSWORD']
basic_user = os.environ['FLASK_BASIC_AUTH_USERNAME']
basic_password = os.environ['FLASK_BASIC_AUTH_PASSWORD']

client = MongoClient('db', username=mongo_user, password=mongo_password)
db = client.universalbackend
db.api.create_index("uid", unique=True)

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = basic_user
app.config['BASIC_AUTH_PASSWORD'] = basic_password

basic_auth = BasicAuth(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'DELETE'])
@basic_auth.required
def universal_api(path):
    path = remove_leading_trailing_slash(path)
    if request.method == 'POST':
        return post_data(path, request.json)
    elif request.method == 'DELETE':
        return delete_data(path)
    else:
        if path == '/':
            return query_all_documents(request.json)
        return get_data(path)


def remove_leading_trailing_slash(string: str) -> str:
    string = '/' + string
    if string.endswith('/') and len(string) > 1:
        string = string[:-1]

    return string


def post_data(uid: str, data: dict) -> str:
    db_doc = {
        'uid': uid,
        'data': data,
        'date': datetime.datetime.utcnow()
    }
    db.api.replace_one({'uid': uid}, replacement=db_doc, upsert=True)
    return dumps(db_doc)


def delete_data(uid: str) -> str:
    db.api.delete_one({'uid': uid})
    return dumps({'uid': uid})


def get_data(uid: str) -> str:
    found = db.api.find_one({'uid': uid})
    if not found:
        regx = re.compile('^' + uid + '/+.')
        found = db.api.find({'uid': regx})
    return dumps(found)


def query_all_documents(query_string: str) -> str:
    return dumps(db.api.find(query_string))


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
