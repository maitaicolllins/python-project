from OOP import myobj


class Dad:
    def __init__(self,color,dadhoobby,):
        self.color=color
        self.dadhooby=dadhoobby
class Mum:
    def __init__(self,color,mumhobby):
        self.color=color
        self.mumcolor=mumhobby
class Boy (Dad):
    def boyinherits(self):
        print(f"Boys inherits {self.color} and the {self.dadhooby}")
class Girl (Mum):
    def girlinherit(self):
        print(f"the girl inherits {self.hobby} and the {self.color}")



# instances
myobj=Boy("African descent",'watching football from')
myobj.boyinherits()
