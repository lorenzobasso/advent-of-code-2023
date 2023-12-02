def parse_lines(text: str):
    lines = [line.strip() for line in text.splitlines()]
    return [line for line in lines if line]
