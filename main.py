import argparse
from file_operations import read_request_from_file, write_result_to_file
from request_parser import parse_request
from html_generator import generate_html_form

def main():
    parser = argparse.ArgumentParser(description="SeeAssArrAff PoC Creator")
    parser.add_argument("request_file", help="Path to the HTTP request file")
    parser.add_argument("output_file", help="Path to the output CSRF PoC")
    args = parser.parse_args()

    out_file = args.output_file
    if "html" not in out_file:
        out_file += ".html"

    request_string = read_request_from_file(args.request_file)
    method, full_url, headers, parsed_body = parse_request(request_string)
    html_content = generate_html_form(method, full_url, headers, parsed_body)

    write_result_to_file(out_file, html_content)

    print(html_content)
    print(f"\n===> SeeAssArrAff PoC saved inside ./results/{out_file} <====")

if __name__ == "__main__":
    main()
