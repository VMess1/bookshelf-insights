# bookshelf-insights (Current Status = Work In Progress)
An organiser for keeping track of your reading habits. This app uses the Google Books API and Bookshelf capabilities, as well as the Open Library API to add, organise and check out your reading habits. You'll need to know the International Standard Book Number (ISBN) which can be found printed on the lower portion of the back cover of a book above the bar code and on the copyright page in order to use this app. Most ebooks will also have ISBN at the time of creation, although not all ebooks have them (especially if self-published).

## APIs and Doc Help
* [Google API key docs](https://cloud.google.com/docs/authentication/api-keys)
* [Open Library API docs](https://openlibrary.org/dev/docs/api/books)

### Getting started
To get your environment setup:
* Fork and clone the repository into a directory that you wish to keep it.
* Run 'chmod u+x setup.sh' to allow permissions to the setup file
* Run 'source setup.sh' which will prompt you for your API key and Google Books User ID and save these into a .env file for you

To use the Google Books API, you will require an API key to access and need to allow permissions to access via your Google Cloud Console. You will need to have a Google account for this. The steps are explained below but for further information, please refer to the google documentation linked above. These links have helpful information about API usage and how to create an API key for the Google Books API.

![Image of API key creation](./data/create_api_key.png)

Following the links, you'll be sent to a page to create a new project in order to obtain your API key. Click on the CREATE CREDENTIALS link in order to create a new key for you to use with this program. You'll also have to allow your created project access to the books api in order for this program to work.

