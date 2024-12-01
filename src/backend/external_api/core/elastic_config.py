

from elasticsearch import Elasticsearch

_es = None
_es = Elasticsearch('https://elastic.labofdev.ru:443')
if _es.ping():
    print('Yay Connect')
else:
    print('Awww it could not connect!')
# _es.indices.delete(index="nyc-restaurants")
# print(_es.__dict__)

# print(os.popen("ping elastic.labofdev.ru").read())
# def create_index(es_object, index_name='recipes'):
#     created = False
#     # index settings
#     settings = {
#         "settings": {
#             "number_of_shards": 1,
#             "number_of_replicas": 0
#         },
#         "mappings": {
#             "members": {
#                 "dynamic": "strict",
#                 "properties": {
#                     "title": {
#                         "type": "text"
#                     },
#                     "submitter": {
#                         "type": "text"
#                     },
#                     "description": {
#                         "type": "text"
#                     },
#                     "calories": {
#                         "type": "integer"
#                     },
#                 }
#             }
#         }
#     }
#     try:
#         if not es_object.indices.exists(index_name):
#             # Ignore 400 means to ignore "Index Already Exist" error.
#             es_object.indices.create(index=index_name, ignore=400, body=settings)
#             print('Created Index')
#         created = True
#     except Exception as ex:
#         print(str(ex))
#     finally:
#         return created

# create_index(_es)
def create_index(client):
    """Creates an index in Elasticsearch if one isn't already there."""
    result = client.index(
        index="restaurant",
        document={
            "settings": {"number_of_shards": 2},
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "borough": {"type": "integer"},
                    "cuisine": {"type": "integer"},
                    "grade": {"type": "integer"},
                    "location": {"type": "text"},
                }
            },
        },
        id=2,
        ignore=400,
    )
    return result
print(create_index(_es))
import json

print(_es.get(index="restaurant", id=2))
# print(_es.create(index="restaurant", id=1, document={"name": "test","borough": 12,
#                     "cuisine": 20,
#                     "grade": 19,
#                     "location": "penis"}))
print(_es.search(index="restaurant", body=json.dumps({"query":{"match": {"name": "test"}}})))
# doc = {
#     "author": "kimchy",
#     "text": "Elasticsearch: cool. bonsai cool.",
#     "timestamp": datetime.now(),
# }
# resp = _es.index(index="test-index", id=1, document=doc)
# print(resp["result"])

# resp = _es.get(index="test-index", id=1)
# print(resp["_source"])