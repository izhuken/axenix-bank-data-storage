from elasticsearch import Elasticsearch

from .config import ELASTICSEARCH_URL


class TypeEnum():
    FLOAT = "float"
    INT = "integer"
    STR = "text"
    DATE = "date"
    BOOL = "boolean"
    UUID = "keyword"


_es = Elasticsearch(ELASTICSEARCH_URL)

# print(_es.search(index="penis", body=json.dumps({"query":{"match": {"id_fact" : str(uuid_field)}}})))
