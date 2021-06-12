import requests
import json
import unittest

class TestPetstoreTests(unittest.TestCase):
    def test_get_not_found(self):
        petstore_service_address = 'https://petstore.swagger.io/v2/pet/get'
        response = requests.get(petstore_service_address) 
        assert response.status_code == 404

    def test_post_server_error(self):
        requestBody = "{'id' : '106', 'status' : 'available', 'name' : 'fluffy'}"
        petstore_service_address = 'https://petstore.swagger.io/v2/pet'
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(petstore_service_address,headers = headers, json = requestBody)
        assert response.status_code == 500

    def test_post_ok(self):
        petstore_service_address = 'https://petstore.swagger.io/v2/pet'
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        requestBody = {'id' : '107', 'status' : 'available', 'name' : 'kitty'}
        response = requests.post(petstore_service_address,headers = headers, json = requestBody)
        assert "107" in response.text 

if __name__ == '__main__':     
    unittest.main()