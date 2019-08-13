import re


def head(html):
    head_reg = re.compile(r"<head.*?>([\w\W]*?)<\/head>", re.MULTILINE)
    return head_reg.search(html).group(0)


def title(html):
    title_reg = re.compile(r"<title.*?>(.*)</title>", re.MULTILINE)
    return title_reg.findall(html)[0]


def _remove_block(text, p):
    return p.sub("", text)


def clean(html, no_scripts):
    comments = re.compile(r"<!--([\w\W]*?)-->", re.MULTILINE)
    scripts = re.compile(r"<script.*?>([\w\W]*?)<\/script>", re.MULTILINE)
    content = re.compile(
        r"(<((?P<p>p)|(?P<h>h[1-6])).*?>([\w\W]*?)<\/((?P=p)|(?P=h))>)",
        re.MULTILINE
    )

    html = _remove_block(html, comments)
    if no_scripts:
        html = _remove_block(html, scripts)

    matches = content.findall(html)

    return "".join([x[0] for x in matches])
