# class point:
#     x = 0
#     y = 0
# def set_nilai(self,a,b):
#     self.x = a
#     self.y = b

# # p1 = point()
# # print(p1.x)

# p1 = point()
# p1.x = 2
# p1.y = -5
# print(p1.x)

import math
class point:
    x = 0 #atribut
    y = 0
    
    def __init__ (self, x, y): #constructor
        self.x = x
        self.y = y
    
    # def set_nilai(self, x, y): #methods
    #     self.x = x
    #     self.y = y
        
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance(self, x1, y1):
        d = math.sqrt((self.x - x1)**2 + (self.y - y1)**2)
        return d
        
    def distance_from_origin(self):
        d= math.sqrt(self.x**2 + self.y**2)
        return d

def main(): #main fungtion      
    #objetct1    
    # p1 = point()
    # p1.x = 7
    # p1.y = 2
    # print(p1.x)
    # print(p1.y)
    #objetct2
    # p2 = point()
    # p2.set_nilai(5,9)
    # print(p2.x)
    # print(p2.y)
    p1 = point(5,6)
    p2 = point(9,3)
    print(p1.x)
    print(p1.y)
    print(p2.x)
    print(p2.y)
    
    p1.translate(-5,7)
    print(p1.x)
    print(p1.y)

    print(p1.distance(10,10))
    print(p1.distance_from_origin())
    
if __name__ == "__main__":
    main()