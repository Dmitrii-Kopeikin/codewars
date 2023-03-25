from re import findall


def solution(s: str):
    return ' '.join(findall(r"[a-z]+|[A-Z]+[a-z]*", s))
