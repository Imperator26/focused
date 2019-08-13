import sys
import html

import requests

from blocks import clean, head, title


def focused(on, no_scripts=True, to_file=True):
    # Set headers
    headers = {"user-agent": "focused"}

    # Get website
    response = requests.get(
        on,
        headers=headers
    )
    if response.status_code != 200:
        raise Exception(f"[{response.status_code}]")

    # Unescape html entites
    text = html.unescape(response.text)

    # Remove comments and scripts
    content = clean(text, no_scripts)

    # Compose web page
    page = f"<!DOCTYPE html>\n<html>\n{head(text)}\n<body>\n{content}\n</body>\n</html>"

    if to_file:
        with open(f"{title(text)}.html", "w") as file:
            file.write(page)
    else:
        return page


if __name__ == "__main__":
    focused(on=sys.argv[1])
