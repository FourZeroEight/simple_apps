# -*- coding: utf-8 -*-
import re

def remove_puncs(text):
    """只留中英文數字
    """
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    output = rule.sub('',text)
    return output
