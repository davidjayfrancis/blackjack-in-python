class Card:
    def __init__(self, num, face):
        self.num = num
        self.face = face
        
    def __str__(self):
        print(f"{self.num} of {self.face}")