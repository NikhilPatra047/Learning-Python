class add:
    def __init__(self, value):
        self.value = value

    def add_amt(self, amt):
        self.value += amt

obj = add(20)
print(obj.value)
