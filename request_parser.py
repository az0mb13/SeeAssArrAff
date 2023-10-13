import urllib.parse
import json

def hesc(input_string):
    encoded_string = ""
    for char in input_string:
        if char.isalnum():
            # If the character is alphanumeric, append it as is
            encoded_string += char
        elif char == '"':
            # If the character is a double quote, encode it as &quot;
            encoded_string += '&quot;'
        else:
            # If the character is not alphanumeric, encode it as an HTML entity
            encoded_string += f'&#{ord(char)};'

    return encoded_string


def parse_request(request_string):
    request_lines = request_string.strip().split('\n')
    request_line = request_lines[0]

    method, path, http_version = request_line.split()

    headers = {}
    for line in request_lines[1:]:
        if not line.strip():
            break
        key, value = line.split(': ', 1)
        headers[key] = value

    full_url = "https://" + headers["Host"] + path

    body = request_lines[-1]  # Assuming the body is the last line in this example

    if 'Content-Length' in headers and int(headers['Content-Length']) == 0:
        # If Content-Length is 0, return without parsing
        return method, full_url, headers, {}
    
    
    if headers["Content-Type"] == "application/x-www-form-urlencoded":
        pairs = body.split('&')
        parsed_body = {}
        for pair in pairs:
            key, value = pair.split('=')
            key = urllib.parse.unquote(key)  # Decode URL-encoded key
            value = urllib.parse.unquote(value)  # Decode URL-encoded value
            parsed_body[hesc(key)] = hesc(value)
            return method, full_url, headers, parsed_body
    elif headers['Content-Type'] == "application/json":
        body = hesc(body[:-1])
        return method, full_url, headers, body
