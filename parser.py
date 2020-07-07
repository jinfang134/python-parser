import re
#  PaymentDebitPostProcess.transactionType == '@' \
# && (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
# && PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
# && (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') && PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0


PATTERN_INDEXOF = r"(\w+)\.(\w+)\.indexOf\('(.*)'\)\s?>=\s?0"
PATTERN_EQUAL = r"(\w+)\.(\w+)\s?[=,>,<]=\s?'?(.*?)'?$"


def parse(validate):
    result = {}
    if '&&' in validate:
        arr = validate.strip().split('&&')
        for item in arr:
            if (item.strip().startswith('(')):
                dic = parse(item.strip())
                if not dic:
                    print('parse it null: ', item.strip())
                    continue
                for key in dic.keys():
                    result[key] = dic[key]
            else:
                data = parseExpress(item.strip())
                result[data[0]] = data[1]

    else:
        arr = validate.strip().lstrip('(').rstrip(')').split('||')
        data = parseExpress(arr[0].strip())
        result[data[0]] = data[1]
    return result


def parseExpress(express):
    express = express.lstrip('(').rstrip(')')
    data = ()
    obj = re.match(PATTERN_INDEXOF, express)
    if obj:
        return getData(obj)

    obj = re.match(PATTERN_EQUAL, express)
    if obj:
        return getData(obj)
    print('fail to parse: ', express)


def getData(obj):
    return (f"{obj.group(1)}.{upperFirst(obj.group(2))}", obj.group(3))


def upperFirst(str):
    return str[0:1].upper()+str[1:]


def match(reg, str):
    obj = re.match(reg, str)
    return (f"{obj.group(1)}.{obj.group(2)[0:1].upper()}{obj.group(2)[1:]}", obj.group(3))
