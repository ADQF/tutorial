# -*- coding: UTF-8 -*-


"""判断一个unicode是否是汉字"""


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


"""判断一个unicode是否是数字"""


def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False


"""判断一个unicode是否是英文字母"""


def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


"""判断是否是（汉字，数字和英文字符之外的）其他字符"""


def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


"""半角转全角"""
if is_other('878'):
    print('是其他字符')
else:
    print('不是其他字符')

if is_other('878'):
    print('是其他字符')
else:
    print('不是其他字符')