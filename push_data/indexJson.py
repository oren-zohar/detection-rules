import requests, json, os
from elasticsearch import Elasticsearch
from datetime import datetime
from os import path
INDEX_NAME = "osquery-index"
DOC_TYPE = "_doc"
DIRECTORY = "data"
FILENAME = "sample.json"
directory = 'data'
HOST = "my_host"
PASS = "pass"

es = Elasticsearch([{'host': HOST, 'port': '9243'}], http_auth=("elastic",PASS),scheme="https",)
for filename in os.listdir(directory):
    if filename.endswith(FILENAME):
        f = open(path.join(DIRECTORY, FILENAME))
        data = json.load(f)
        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        data["@timestamp"][0] = date_time
        print("load file: ", filename)
        print("@datetimne: ", data["@timestamp"])
        docket_content = f.read()   
        response = es.index(index = INDEX_NAME, doc_type = DOC_TYPE, body = data)
        print(response)