from core.settings.elastic import TypeEnum
from elasticsearch import Elasticsearch


class ElasticSearchService:
    def __init__(self, client: Elasticsearch, index_name: str, index_id: str):
        self.client = client
        self.index_name = index_name
        self.index_id = index_id

    def create_index(self, properties):
        result = self.client.index(
            index=self.index_name,
            document={
                "settings": {"number_of_shards": 2},
                "mappings": {"properties": self.__model_cast(properties)},
            },
            id=self.index_id,
            ignore=400,
        )
        return result

    def insert_data(self, properties: dict):
        self.client.index(
            index=self.index_name,
            doc_type="_doc",
            id=properties.get("id_fact"),
            document=properties,
        )

    def update_data(self, properties: dict):
        self.client.index(
            index=self.index_name,
            id=properties.get("id_fact"),
            doc_type="_doc",
            document=properties,
        )

    def __model_cast(_, data: dict):
        result = {}

        for key, value in data.items():
            result[key] = {"type": TypeEnum.__dict__[type(value).__name__.upper()]}

        return result
