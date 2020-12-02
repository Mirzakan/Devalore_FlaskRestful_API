import unittest
from index import app
import json
import requests
from unittest.mock import patch

fake_db = {
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    },
    "test_user2": {
    "id": "test2",
    "name": "Test User2",
    "favorite_color": "Black2"
    }
}

get_users_result = {
    "test_user": {
        "name": "Test User",
        "favorite_color": "Black"
    },
    "test_user2": {
    "name": "Test User2",
    "favorite_color": "Black2"
    }
}

get_user_result = {
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    }
}

class APITests(unittest.TestCase):
    @patch('index.getData', return_value = fake_db )
    def test_users(self, val):
        tester = app.test_client()
        response = tester.get("/users")
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json, get_users_result)

    @patch('index.getData', return_value = fake_db )
    def test_user(self, val):
        tester = app.test_client()
        response = tester.get("/user/test_user")
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json, get_user_result)

    @patch('index.getData', return_value = fake_db )
    def test_NotExist(self, mock):
        tester = app.test_client()
        response = tester.get("/user/test_user123")
        self.assertEqual(response.status, '404 NOT FOUND')
        
if __name__ == "__main__":
    unittest.main()

