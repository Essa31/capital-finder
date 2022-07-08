from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        if 'country' in dictionary:
            country = dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            response = requests.get(url + country)
            data = response.json()
            capital_response = data[0]["capital"]
            message = f"The capital of " + str(country) + " is " + str(capital_response)

        elif 'capital' in dictionary:
            capital = dictionary['capital']
            url = 'https://restcountries.com/v2/capital/'
            response = requests.get(url + capital)
            data = response.json()
            capitals = data[0]["capital"]
            country_name = data[0]["name"]
            message = str(capitals) + " is " + "the capital of " + str(country_name)

        else:
            message = "Please write a city name to get info about it"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return

def main():
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, Handler)
    print(f'Server is running')
    server.serve_forever()


if __name__ == "__main__":
    main()