import re


def extract_title(markdown: str) -> str:
    text_lines = markdown.splitlines()
    for line in text_lines:
        if re.match(r"\#\s", line):
            return line.strip("# ")
    raise Exception("No H1 header (title) found")