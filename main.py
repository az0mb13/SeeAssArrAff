import os
import functools
import socketserver
import http.server
import argparse
from file_operations import read_request_from_file, write_result_to_file
from request_parser import parse_request
from html_generator import generate_html_form

def main():
    parser = argparse.ArgumentParser(description="SeeAssArrAff PoC Creator")
    parser.add_argument("request_file", help="Path to the HTTP request file")
    parser.add_argument("output_file", help="Path to the output CSRF PoC")
    parser.add_argument("-s", "--server", help="Server the PoC on this port")
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
    
    if args.server:
        port = int(args.server)
        curdir = os.path.abspath(os.curdir) + "/results"
        print(curdir)
        Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=curdir)
        
        try:
            with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
                print(f"Serving the PoC at http://127.0.0.1:{port}/{out_file}")
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nCiao")
            httpd.server_close()



if __name__ == "__main__":
    main()
