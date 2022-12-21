# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
    text = f.read()
    decoded_text = text.decode('utf-8')
    print(textwrap.fill(decoded_text, width=50))
print()

obj = json.loads(decoded_text)
print(f"Book Kind: {obj['kind']}")
print(f"Book Id: {obj['items'][0]['id']}")
print(f"Title: {obj['items'][0]['volumeInfo']['title']}")
print(f"Book Snippet: {obj['items'][0]['searchInfo']['textSnippet']}")