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
    response = client.get("/module/search/infrastructure/treviso/Mensa")
    assert response.status_code == 200
    assert response is not None
    assert len(response.json()['result']) != 0
    
def test_search_empty():
    response = client.get("/module/search/infrastructure/treviso/Biblioteca")
    assert response.status_code == 200
    assert response is not None
    assert response.json() == {'error': "Unable to find school"}
    
def test_search_edge():
    # Conegliano is not a province
    response = client.get("/module/search/infrastructure/treviso/awfffgerg##=")
    assert response.status_code == 200
    assert response.json() == {'error': "Unable to find school"}
    