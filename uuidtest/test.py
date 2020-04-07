import uuid

def get_short_id():
    print(uuid.uuid4())
    id = '0x'+str(uuid.uuid4()).replace("-", '')
    return eval(id)

x=get_short_id()
print(x)