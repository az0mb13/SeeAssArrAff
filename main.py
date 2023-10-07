import os
import textwrap
import argparse
from file_operations import read_request_from_file
from request_parser import parse_request
from html_generator import generate_html_form

def main():
    parser = argparse.ArgumentParser(description="Generate an HTML form from an HTTP request.")
    parser.add_argument("request_file", help="Path to the HTTP request file")
    args = parser.parse_args()

    request_string = read_request_from_file(args.request_file)
    method, full_url, headers, parsed_body = parse_request(request_string)
    html_content = generate_html_form(method, full_url, headers, parsed_body)

    if not os.path.exists("results"):
        os.makedirs("results")

    cleaned_html_content = textwrap.dedent(html_content).strip()
    with open("results/output.html", "w") as html_file:
        html_file.write(cleaned_html_content)

    print(cleaned_html_content)
    print("\nSeeAssArrAff PoC saved inside results/output.html")

if __name__ == "__main__":
    main()
