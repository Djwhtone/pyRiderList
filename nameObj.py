# Rider class stores variables
class Riders:
    def __init__(self, id=0, name=None, shift=None,location=None, group_label=None):
        self.id = id
        self.name = name
        self.shift = shift
        self.location = location
        self.group_label = group_label

    def __str__(self):
        return f'Name: {self.name} \nShift: {self.shift} \nLocation: {self.location} \nGroup: {self.group_label}'
#push test
