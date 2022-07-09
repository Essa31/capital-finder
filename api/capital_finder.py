from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'country' in dic:
            country = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()

            the_name = data[0]["capital"][0]
            message = "The capital of " + str(country) + " is " + str(the_name)
        elif 'capital' in dic:
            capital = dic['capital']
            url = 'https://restcountries.com/v2/capital/'
            r = requests.get(url + capital)
            data = r.json()

            the_name = data[0]["name"]
            message = str(capital) + " is the capital of " + str(the_name)
        else:
            message = "Make sure you right ?capital=example  or ?country=example  is correct !!!"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return

