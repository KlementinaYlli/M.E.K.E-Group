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

def test_search_valid():
    """
    Tests a valid request to the backend.

    Checks the status code and the quality of the response.
    In particular it should be not empty and should be able to successfully convert to json.
    """

    response = client.get("/module/search/infrastructure/treviso/Mensa")
    assert response.status_code == 200
    assert response is not None
    assert len(response.json()['result']) != 0
    
def test_search_empty():
    """
    Tests an empty request to the backend.

    Checks the status code and that no results are returned.
    """

	# Biblioteca is not a supported infrastructure for search.
    response = client.get("/module/search/infrastructure/treviso/Biblioteca")
    assert response.status_code == 200
    assert response is not None
    assert response.json() == {'error': "Unable to find school"}
    
def test_search_edge():
    """
    Tests an invalid request to the backend.

    Checks the status code and verifies that the no valid result is found.
    Even if the request was bad, it still should be able to convert to json, in order to retrieve the error.
    """

    # Invalid input
    response = client.get("/module/search/infrastructure/treviso/awfffgerg##=")
    assert response.status_code == 200
    assert response.json() == {'error': "Unable to find school"}
    
	# Invalid input province (does not exist)
    response = client.get("/module/search/infrastructure/conegliano/awfffgerg##=")
    assert response.status_code == 200
    assert response.json() == {'error': "Unable to find school"}
    