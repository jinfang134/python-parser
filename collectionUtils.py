

def mergeDic(dica, dicb):
    """合并两个dict，如果dica已经存在的属性，不进行覆盖

    Args:
        dica (dict): [description]
        dicb (dict): [description]

    Returns:
        [dict]: [description]
    """
    result = dica
    for item in dicb.keys():
        if item not in dica.keys():
            result[item] = dicb[item]
    return result
