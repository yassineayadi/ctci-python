import re


def urlify_regex(strng: str, *args):
    REGEX = re.compile(r"\s+")
    return REGEX.sub("%20", strng.rstrip())

    # return REGEX.sub(strng, "%20")


functions = [urlify_regex]
