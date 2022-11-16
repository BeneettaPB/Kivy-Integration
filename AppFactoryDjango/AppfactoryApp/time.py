import pytz
import random
import string
import urllib.request

from pathlib import Path
from datetime import datetime

def get_string_timestamp():
    tz = pytz.timezone('Asia/Kolkata')
    ist = datetime.now(tz)
    return ist.strftime("%Y-%m-%d %H:%M:%S")