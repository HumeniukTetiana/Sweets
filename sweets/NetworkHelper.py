import requests

class NetworkHelper:

    @staticmethod
    def get_ingredients():
        response = requests.get('http://127.0.0.1:8001/ingredients/', auth=('test11', 'Q1wertyuI'))
        if response.status_code == 200:
            return response.json()
        return []

    @staticmethod
    def get_ingredient(ingredient_id):
        response = requests.get(f"http://127.0.0.1:8001/ingredients/{ingredient_id}/", auth=('test11', 'Q1wertyuI'))
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def delete_ingredient(ingredient_id):
        response = requests.delete(f"http://127.0.0.1:8001/ingredients/delete/{ingredient_id}/", auth=('test11', 'Q1wertyuI'))
        return response.status_code == 204
