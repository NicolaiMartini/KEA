"""
Prøv at print værdien “something interesting here” fra følgende json
"""
try:
    import ujson as json
except:
    import json

json_sample = """{"key1":"value1", "key2":[{"key3":"value3"}, {"wow":"something interesting here!"}]"""

json_dict=json.loads(json_sample)
print(json_dict)
print(type(json_dict))

key2=json_dict.get("key2") # Dict med key2
print(key2)
key2_1=key2[1]
print(key2_1)
wow=key2_1.get("wow")
print(wow)
# print(json_dict.get("key2")[1].get("wow"))