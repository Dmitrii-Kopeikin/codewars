from re import sub


def solution(s: str):
    return sub('([A-Z])', r' \1', s)
