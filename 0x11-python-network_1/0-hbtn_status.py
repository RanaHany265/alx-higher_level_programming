i!/usr/bin/python3
"""A script that
-  fetches https://alx-intranet.hbtn.io/status
-   use the package urllib
-    not allowed to import any packages other than urllib
"""
def main():
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)

if __name__ == "__main__":
    main()
