from app.storage.temp.inmemory import InMemoryDocumentStore

doc_store = InMemoryDocumentStore()

def get_doc_store() -> InMemoryDocumentStore:
    return doc_store