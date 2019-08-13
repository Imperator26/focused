import re


def head(html):
    head_reg = re.compile(r"<head.*?>([\w\W]*?)<\/head>", re.MULTILINE)
    return head_reg.search(html).group(0)


def title(html):
    title_reg = re.compile(r"<title.*?>(.*)</title>", re.MULTILINE)
    return title_reg.findall(html)[0]


def article(html):
    article_reg = re.compile(r"<article.*?>[\w\W]*?</article>", re.MULTILINE)
    return article_reg.search(html).group(0)


def _remove_block(text, p):
    return p.sub("", text)


def clean(html, no_scripts):
    # Compile patterns
    comments_reg = re.compile(r"<!--([\w\W]*?)-->", re.MULTILINE)
    scripts_reg = re.compile(r"<script.*?>([\w\W]*?)<\/script>", re.MULTILINE)
    no_scripts_reg = re.compile(r"(<noscript>|<\/noscript>)", re.MULTILINE)
    content = re.compile(
        r"(<((?P<p>p)|(?P<h>h[1-6])).*?>([\w\W]*?)<\/((?P=p)|(?P=h))>)",
        re.MULTILINE
    )

    html = _remove_block(html, comments_reg)
    if no_scripts:
        html = _remove_block(html, scripts_reg)
        html = _remove_block(html, no_scripts_reg)

    # Find article
    body = article(html)

    if body is None:
        matches = content.findall(html)
        return "".join([x[0] for x in matches])
    else:
        return body
