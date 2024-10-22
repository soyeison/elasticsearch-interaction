from pprint import pprint
from elasticsearch import Elasticsearch


class Search:
    def __init__(self) -> None:
        self.es = Elasticsearch("http://localhost:9200")
        client_info = self.es.info()
        print("Connected to Elasticsearch!")
        pprint(client_info.body)

    def create_index(self):
        self.es.indices.delete(index="my_documents", ignore_unavailable=True)
        self.es.indices.create(index="my_documents")

    def insert_document(self, document):
        return self.es.index(index="my_documents", body=document)

    def search(self, **query_args):
        return self.es.search(index="my_documents", **query_args)
