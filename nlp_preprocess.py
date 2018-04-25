# -*- coding: utf-8 -*-
import re
import jieba
from hanziconv import HanziConv

def remove_puncs(text):
    """只留中英文數字
    """
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    output = rule.sub('',text)
    return output

def chs_to_cht(text):
    """簡中轉繁中
    """
    output = HanziConv.toTraditional(text)
    return output

def jieba_work(text):
    """結巴分詞
    cut_all=False: 不產生衍生字, 只從現有字串切分
    """
    seg_list = jieba.cut(text, cut_all=False)
    output = " ".join(seg_list)
    return output

def str_to_list(text):
    """string轉list
    """
    text_list = text.split()
    return text_list

def trim_terms(text_list, n=2):
    """把長度小於 n 的字詞砍掉
    """
    output = [x for x in text_list if not len(x) < n]
    return output
