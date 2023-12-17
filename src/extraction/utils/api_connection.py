import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('API_KEY')
UID = os.getenv('UID')


def get_book_by_isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        book_data = response.json()
        print("Successfully found book")
        return book_data
    except requests.exceptions.HTTPError as errhttp:
        return f"HTTP Error: {errhttp}"
    except requests.exceptions.ConnectionError as errcon:
        return f"Error connecting: {errcon}"
    except requests.exceptions.Timeout as errtime:
        return f"Timeout error: {errtime}"
    except requests.exceptions.RequestException as err:
        return f"Request error: {err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def get_bookshelf_connection():
    """
    Connects to your individual bookshelf in your google books library
    and returns a json object with details of the books that you have
    saved in a particular shelf. For a successful connection, you will
    need to have a google API key and have allowed the google books api
    """
    url = ("https://www.googleapis.com/books/v1/users/"
           + f"{UID}/bookshelves/2/volumes?key={KEY}")
    response = requests.get(url)
    bookshelves = response.json()
    return bookshelves


def get_details(bookshelves):
    print(f"Book Count: {bookshelves["totalItems"]}")
    bookshelf_array = bookshelves["items"]
    for book_info in bookshelf_array:
        book_specifics = book_info["volumeInfo"]
        print(f"Book title: {book_specifics["title"]}")
        print(f"Author: {book_specifics["authors"][0]}")
        print(f"Page Count: {book_specifics["pageCount"]}")
        try:
            print(f"Publisher: {book_specifics["publisher"]}\n")
        except KeyError:
            print("No publisher recorded")
