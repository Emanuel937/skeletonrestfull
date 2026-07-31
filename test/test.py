from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_root(capfd):
    client = TestClient(app)
    response = client.get("/testing/")
    print("DATA:", response.json())

    out, err = capfd.readouterr()
    print(out)

    assert response.status_code == 200
