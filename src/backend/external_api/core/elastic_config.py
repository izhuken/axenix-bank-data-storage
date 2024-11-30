from elasticsearch import Elasticsearch

_es = None
_es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
if _es.ping():
    print('Yay Connect')
else:
    print('Awww it could not connect!')
