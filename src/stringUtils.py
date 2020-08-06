import re
import random
import string

def replaceIgnoreCase(string, pattern, replace):
    return re.sub(pattern, replace, string, flags=re.I)


def upperFirst(str):
    return str[0:1].upper()+str[1:]


def randomStr(length):
    """生成随机的包含大写字母和数字的字符串,长度为length

    Args:
        length (int): 字符串长度

    Returns:
        [type]: [description]
    """
    letters = string.ascii_uppercase+'0123456789'
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string is:", result_str)
    return result_str


if __name__ == "__main__":
    randomStr(8)