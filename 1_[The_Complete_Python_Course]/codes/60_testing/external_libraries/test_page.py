from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester("https://google.com")

    def test_make_request(self):
        with patch("requests.get") as mock_response:
            self.page.get()
            mock_response.assert_called()

    def test_content_returned(self):
        fake_content = "fakeitis"

        class FakeResponse:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()) as mock_response:
            result = self.page.get()
            self.assertEqual(result, fake_content)
