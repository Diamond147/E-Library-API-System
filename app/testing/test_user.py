from typing import Dict
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from routers.user import Users
from crud.user import Users
from fastapi import status
from uuid import uuid4

client = TestClient(app)

Mock_Users = {
    "ed24b9ef-239d-4d7d-894d-cd6fe892227f": {
        "name": "first name",
        "email": "first email",
        "user_id": "ed24b9ef-239d-4d7d-894d-cd6fe892227f",
        "is_active": True
    }
}


@patch("routers.user.Users", new=Mock_Users)
def test_get_all_users():
    response = client.get("/v1/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": Mock_Users, "message": "successful"}


@patch("crud.user", Mock_Users)
@patch("crud.user.uuid4", return_value="5b49e896-d9ab-45da-b9b8-4d6f709bd6b5")
def test_create_user(mock_uuid):
    create_user = {
        "name": "Opeyemi",
        "email": "email1@gmail.com",
        "is_active": True
    }
    expected_create_user = {
        "detail": {
        "user_id": "5b49e896-d9ab-45da-b9b8-4d6f709bd6b5",
        "name": "Opeyemi",
        "email": "email1@gmail.com",
        "is_active": True
    }, "message": "User created successfully"
    }

    response = client.post("/v1/users", json = create_user)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected_create_user


@patch("crud.user.Users", Mock_Users)
def test_get_user_by_id():

    expected_user = {
        "user_id": "ed24b9ef-239d-4d7d-894d-cd6fe892227f",
        "name": "first name",
        "email": "first email",
        "is_active": True
    }

    response = client.get("/v1/users/ed24b9ef-239d-4d7d-894d-cd6fe892227f")
    print(Mock_Users)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == expected_user
    assert response.json()["message"] == "successful"


@patch("crud.user.Users", Mock_Users)
def test_updated_user():

    new_data = {
        "name": "Williams",
        "email": "email2@gmail.com",
    }

    updated_user = {
        "detail": {
            "name": "Williams",
            "email": "email2@gmail.com"
        }, "message": "User updated successfully"
    }

    response = client.put("/v1/users/ed24b9ef-239d-4d7d-894d-cd6fe892227f", json = new_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == updated_user


@patch("crud.user.Users", Mock_Users)
def test_patch_user():

    new_data = {
        "name": "Johnson",
        "email": "email2@gmail.com",
    }

    patched_user = {
        "detail": {
            "name": "Johnson",
            "email": "email2@gmail.com"
        }, "message": "Name updated successfully"
    }

    response = client.patch("/v1/users/ed24b9ef-239d-4d7d-894d-cd6fe892227f", json = new_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == patched_user


@patch("crud.user.Users", Mock_Users)
def test_delete_user():
    response = client.delete("/v1/users/ed24b9ef-239d-4d7d-894d-cd6fe892227f")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User deleted successfully"


# @patch("crud.user.Users", Mock_Users)
# def test_deactivate_user():
#     expected_user = {
#         "user_id": "ed24b9ef-239d-4d7d-894d-cd6fe892227f",
#         "name": "first name",
#         "email": "first email",
#         "is_active": True
#     }
#     response = client.put("/v1/users/ed24b9ef-239d-4d7d-894d-cd6fe892227f/deactivate")
#     print(response.json())
#     print(Mock_Users)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json()["detail"] == expected_user
#     assert response.json()["message"] == "User deactivated successfully"

    