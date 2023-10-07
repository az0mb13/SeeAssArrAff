def read_request_from_file(file_path):
    with open(file_path, "r") as request_file:
        return request_file.read()
