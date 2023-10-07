import urllib.parse

# Sample request body
request_body = "email=random%40test.com&name[]=%5B%22alex%22%2C%201234%5D&namex=asdasd"

# Split the request body into key-value pairs
pairs = request_body.split('&')

# Create a dictionary to store the key-value pairs
parsed_body = {}

# Process and populate the dictionary
for pair in pairs:
    key, value = pair.split('=')
    key = urllib.parse.unquote(key)  # Decode URL-encoded key
    value = urllib.parse.unquote(value)  # Decode URL-encoded value
    parsed_body[key] = value

print(parsed_body)
# Process and print the key-value pairs without extra brackets
# for key, value in parsed_body.items():
#     key = key.rstrip('[]')  # Remove trailing brackets
#     print(f"Key: {key}")
#     print(f"Value: {value}")