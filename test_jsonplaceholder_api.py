import requests

link = "https://jsonplaceholder.typicode.com/posts"


class TestJsonplaceholderApi:

    def test_method_get(self):
        r = requests.get(link)
        assert r.status_code == 200, f"Method GET failed! Status code: {r.status_code}"

    def test_method_post(self, posts_data):
        r = requests.post(link, data=posts_data)
        assert r.status_code == 201, f"Method POST failed! Status code: {r.status_code}"

    def test_method_delete(self, posts_data):
        r = requests.delete(f"{link}/{posts_data.__getitem__('id')}")
        assert r.status_code == 200, f"Method DELETE failed! Status code: {r.status_code}"
