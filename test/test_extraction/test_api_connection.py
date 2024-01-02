import json
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from requests import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException
)
from src.extraction.utils.api_connection import (
    get_book_by_isbn,
    get_bookshelf_connection
)


def get_mock_OL_data():
    """
    Mocking the response object from the Open Library (OL) API.
    The structure was taken from an example provided by the
    documentation.
    """
    with open("test/mock_data/mock_OL_data.json") as file:
        return json.load(file)


def get_mock_google_bookshelf():
    """
    Mocking the response object from the Google Books API.
    The structure was taken from an example provided by the
    documentation.
    """
    with open("test/mock_data/mock_OL_data.json") as file:
        return json.load(file)


class TestGetBookByISBN(unittest.TestCase):
    def setUp(self):
        self.mock_response = MagicMock()

    def test_get_book_by_isbn_successful_call(self):
        """
        The get_book_by_isbn() should return the correct reponse object
        as well as the correct message if a successful call is made to
        the Open Library API.
        """
        mock_OL_data = get_mock_OL_data()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = mock_OL_data

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('src.extraction.utils.api_connection.requests.get',
                       return_value=self.mock_response):
                result = get_book_by_isbn(1234567890)
        out = mock_stdout.getvalue()

        self.assertEqual(result, mock_OL_data)
        self.assertEqual(out.strip(), "Successfully found book")

    def test_http_error_handling(self):
        """
        The get_book_by_ibsn() should return a helpful message if
        a HTTP error is encountered. The messages have been taken
        from the requests documentation found here:
        https://requests.readthedocs.io/en/latest/user/quickstart.html#response-status-codes # noqa
        """
        self.mock_response.status_code = 404
        self.mock_response.raise_for_status.side_effect = HTTPError(
            ("404 Client Error: Not Found for url: "
             + "https://openlibrary.org/isbn/3.json")
        )
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_book_by_isbn(3)
        self.assertEqual(result,
                         ("HTTP Error: 404 Client Error: Not Found"
                          + " for url: https://openlibrary.org/isbn/3.json"))

    def test_connection_error_handling(self):
        """
        The get_book_by_isbn() should return a helpful message with
        the specific error if a connection error occurs
        """
        self.mock_response.raise_for_status.side_effect = ConnectionError()
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_book_by_isbn(12345)
        self.assertEqual(result, "Error connecting: ")

    def test_timeout_error_handling(self):
        """
        The get_book_by_isbn() should return a helpful message with
        the specific error if a connection error occurs
        """
        self.mock_response.raise_for_status.side_effect = Timeout()
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_book_by_isbn(12345)
        self.assertEqual(result, "Timeout error: ")

    def test_request_exception_error_handling(self):
        """
        The get_book_by_isbn() should return a helpful message with
        the specific error if a request exception error occurs
        """
        self.mock_response.raise_for_status.side_effect = RequestException()
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_book_by_isbn(12345)
        self.assertEqual(result, "Request error: ")

    def test_other_exception_error_handling(self):
        """
        The get_book_by_isbn() should return a helpful message if any
        other type of error is encountered
        """
        self.mock_response.raise_for_status.side_effect = Exception()
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_book_by_isbn(12345)
        self.assertEqual(result, "An unexpected error occurred: ")


class TestGetBookshelfConnection(unittest.TestCase):
    def setUp(self):
        self.mock_response = MagicMock()

    def test_returns_correct_json_object(self):
        """
        The get_bookshelf_connection() connects to a specified bookshelf
        on a users Google Books account. This function should return
        a JSON object with details of the books on the specific shelf
        """
        mock_bookshelf_data = get_mock_google_bookshelf()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = mock_bookshelf_data
        with patch('src.extraction.utils.api_connection.requests.get',
                   return_value=self.mock_response):
            result = get_bookshelf_connection()

        self.assertEqual(result, mock_bookshelf_data)
    