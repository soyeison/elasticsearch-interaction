import requests


class ElasticSearchApi:
    def get_all_documents(self, index: str):
        # Autenticarse
        # Hacer la consulta
        request = requests.get(f"http://localhost:9200/{index}/_search")
        return request.json()["hits"]["hits"]

    def sear_document_by_Id(self, index: str, id: str):
        # Autenticar
        # Hacer consulta
        query = {"query": {"match": {"_id": {"query": id}}}}
        request = requests.get(f"http://localhost:9200/{index}/_search", json=query)
        return request.json()["hits"]["hits"]
