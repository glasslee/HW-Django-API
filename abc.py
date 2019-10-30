import json

lion = {
    'id' :1,
    'title' : 'likelion',
    'body' : 'At INHA univ',
}

print(lion)
print(type(lion))

lion_s = json.dumps(lion)

print(lion_s)
print(type(lion_s))

lion_d = json.loads(lion_s)

print(lion_d)
print(type(lion_d))