import random

def create_name():
    name = []
    for x in range(2):
        name.append(chr(random.randint(97, 122)))
    for i in range(3):
        name.append(str(random.randint(0, 9)))
    full_name = ''.join(name)
    return full_name

class Robot(object):
    def __init__(self, name=None):
        self.name = name
        if name is None:
            self.name = create_name()


new = Robot()
print(new.name)

