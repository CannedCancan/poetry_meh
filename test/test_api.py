import pytest



from sample_api import api

class TestAPI:
    def test_api(self):
        print(api.Hello())
        