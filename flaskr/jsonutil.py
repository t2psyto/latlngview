import json
from collections import OrderedDict


def asdict(self):
    result = OrderedDict()
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result


def to_array(all_vendors):
    v = [ ven.asdict() for ven in all_vendors ]
    return json.dumps(v)
