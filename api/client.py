import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def register_plate(self, plate_text):
        url = f"{self.base_url}/park/register/{plate_text}"
        try:
            response = requests.get(url, timeout=5)
            print(f"API Response for {plate_text}: {response.status_code}")
        except requests.RequestException as e:
            print(f"API call failed for {plate_text}: {e}")