from search import Search
from integration import ElasticSearchApi


def main(es: Search, elastic_api: ElasticSearchApi):
    # Crear el indice
    # es.create_index()

    # Agregar documentos a un indice
    # document = {
    #     "title": "Work From Home Policy",
    #    "contents": "The purpose of this full-time work-from-home policy is...",
    #    "created_on": "2023-11-02",
    # }
    # response = es.insert_document(document)
    # print("Document inserted:", response)

    # Obtener los documentos haciendo una consulta a la api de elastic search
    # response = elastic_api.get_all_documents("my_documents")
    # print("Response:", response)

    # Obtener un documento consultado por id
    response = elastic_api.sear_document_by_Id("my_documents", "8kYatZIBFZ1ks_bYb_A_")
    print("Response:", response)


if __name__ == "__main__":
    es = Search()
    elastic_api = ElasticSearchApi()
    main(es, elastic_api)
