import requests


def get_patients():
    url = "http://127.0.0.1:8000/api/v1/p/patients"
    r = requests.get(url)
    r.raise_for_status()

    return r.json()


def get_patient_docs(patient_id):
    url = f"http://127.0.0.1:8000/api/v1/p/patient/{patient_id}/docs"
    r = requests.get(url)
    r.raise_for_status()

    return r.json()


def get_patient(patient_id):
    url = f"http://127.0.0.1:8000/api/v1/p/patient/{patient_id}"
    r = requests.get(url)
    r.raise_for_status()

    return r.json()