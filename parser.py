import re
#  PaymentDebitPostProcess.transactionType == '@' \
# && (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
# && PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
# && (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') && PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0


def parse(validate):
    arr = validate.split('&&')
    result={}
    for item in arr:
        if (item.strip().startswith('(')):
            orList = item.strip().lstrip('(').rstrip(')').split('||')
            data=parseExpress(orList[0])
        else:
            data=parseExpress(item)
        result[data[0]]=data[1]
    return result

def parseExpress(express):
    data=()
    if 'indexOf' in express.strip():
        data = match(
            r"(\w+)\.(\w+)\.indexOf\('(.*)'\)\s?>=\s?0", express.strip())
    elif '==' in express:
        data = match(r"(\w+)\.(\w+)\s?==\s'?(.*?)'?$", express.strip())
    return data



def match(reg, str):
    obj = re.match(reg, str)
    return (f"{obj.group(1)}.{obj.group(2)[0:1].upper()}{obj.group(2)[1:]}",obj.group(3))
