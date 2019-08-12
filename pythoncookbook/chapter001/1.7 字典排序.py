# OrderedDict在迭代操作的时候它会保持元素被插入时的顺序
from collections import OrderedDict
import json


def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    json.dumps(d)
    print(d)


ordered_dict()
