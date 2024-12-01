from elasticsearch import Elasticsearch

from .settings import ELASTICSEARCH_URL


class TypeEnum:
    FLOAT = "float"
    INT = "integer"
    STR = "text"
    DATE = "date"
    BOOL = "boolean"
    UUID = "keyword"


_es = Elasticsearch(ELASTICSEARCH_URL)
