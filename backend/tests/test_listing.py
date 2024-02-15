import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can do the relative import
from app.main import app

"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)


def test_provinces():
    """
    Test if all provinces are correctly listed
    """

    response = client.get("/all/provinces")
    assert response.status_code == 200
    assert response is not None
    elements = response.json()['elements']
    elements.sort()
    check = sorted(["Belluno", "Padova", "Rovigo", "Treviso", "Venezia", "Vicenza", "Verona"])

    assert elements == check


def test_cities():
    """
    Test if all cities are correctly listed
    """

    response = client.get("/all/cities")
    assert response.status_code == 200
    assert response is not None
    elements = response.json()['elements']
    
    elements.sort()

	# Check expected size
    assert len(elements) == 552

    elements = elements[0: 10]

    check = sorted(['Abano Terme', 'Adria', 'Affi', 'Agna', 'Agordo', 'Agugliaro', 'Alano di Piave', 'Albaredo d`Adige', 'Albettone', 'Albignasego'])

    assert elements == check


def test_schools():
    """
    Test if all school types are correctly listed
    """

    response = client.get("/all/school_types")
    assert response.status_code == 200
    assert response is not None
    elements = response.json()['elements']
    elements.sort()
    check = sorted(["ISTITUTO COMPRENSIVO","PRIMARIA","SECONDARIA PRIMO GRADO","Not found","SECONDARIA SECONDO GRADO","INFANZIA","CPIA - CENTRO TERRITORIALE","DIREZIONE DIDATTICA","CONVITTO/EDUCANDATO","IP"])

    assert elements == check
    
def test_not_found():
    """
    Test if all school types are correctly listed
    """

    response = client.get("/all/invalid_input")
    assert response.status_code == 200
    assert response is not None
    msg = response.json()['error']

    assert msg == 'element not found'