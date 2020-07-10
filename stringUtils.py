import re


def replaceIgnoreCase(string, pattern, replace):
    return re.sub(pattern, replace, string, flags=re.I)


def upperFirst(str):
    return str[0:1].upper()+str[1:]
