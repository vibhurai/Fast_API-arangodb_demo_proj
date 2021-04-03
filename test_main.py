from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# render main page
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

# read database
def test_read_database():
    response = client.get("/actor")
    assert response.status_code == 200

# insert actor successfully
def test_post_actor_success():
    response = client.post(
        "/actor",
        json=
        {
            "name": "string"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "code": "success",
    "message": "actor added to the database"
    }
    
# insert actor unsuccessfully
def test_post_actor_fail():
    response = client.post(
        "/actor",
        json=
        {
            "namee": "string"
        }
    )
    assert response.status_code == 422
    assert response.json() == {
    "detail": [
            {
                "loc": [
                    "body",
                    "name"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

# update actor successfully
def test_update_actor_success():
    response = client.patch(
        "/actor/sting",
        json=
        {
            "name": "string"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "code": "success",
        "message": "updation successfull"
    }

# update actor unsuccessfully
def test_update_actor_fail():
    response = client.patch(
        "/actor/sting",
        json=
        {
            "namee": "string"
        }
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "loc": [
                "body",
                "name"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }

# delete actor unsuccessfully
def test_delete_actor_fail():
    response = client.delete(
        "/actor",
        json=
        {
            "namee": "string"
        }
    )
    assert response.status_code == 422
    assert response.json() =={
        "detail": [
            {
            "loc": [
                "body",
                "key"
            ],
            "msg": "field required",
            "type": "value_error.missing"
            }
        ]
    }