from utils.train_requests import get_headers

def test_get_headers():
    headers = get_headers()

    assert "content-type" in headers.keys()
    assert "Ocp-Apim-Subscription-Key" in headers.keys()
