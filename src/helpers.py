import pandas as pd
import numpy as np
import re



def getReMax(val:str) -> np.float:
    """Returns maximum number in a string using regex"""
    search = re.findall('\d+', val) 
    nums = map(np.float, search) 
    return max(nums)