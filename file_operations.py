import os
import textwrap

def read_request_from_file(file_path):
    with open(file_path, "r") as request_file:
        return request_file.read()

def write_result_to_file(file_path, content):
    cleaned_html_content = textwrap.dedent(content).strip()
    if not os.path.exists("results"):
        os.makedirs("results")
    
    with open(os.path.join("results", file_path), "w") as result_file:
        result_file.write(cleaned_html_content)