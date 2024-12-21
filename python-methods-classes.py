class Rectangle:
    def __init__(self,c,l,w):
        self.l = l
        self.w = w
    def area(self):
        self.area = self.l * self.w
        return self.area
    def volume(self):
        self.vol = self.area *2
        return self.vol
    


myrect1 = Rectangle('red',2,1)
area = myrect1.area()
# print(area)
vol = myrect1.volume()
print(vol)
