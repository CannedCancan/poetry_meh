from sample_api import api_locals
from utils.utils import Util

def Hello():
    Util()
    return "hello from {}\n{}".format(__name__, api_locals.grosse_str)

