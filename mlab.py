import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds049486.mlab.com:49486/moviedb

host = "ds049486.mlab.com"
port = 49486
db_name = "moviedb"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())