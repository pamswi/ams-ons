# init method, str method, int method

class Rectangle():
    # creates new object
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    # calculates the area
    def __int__(self):
        return self.height * self.width
    
    def __add__(self, rec2):
        return Rectangle(self.width + rec2.width, self.height + rec2.width)
    
    # prints a rectangle in the terminal using ascii 
    def __str__(self):
        horizon_border = '+' + '-' * self.width + '+\n'
        vertic_border = '|' + ' ' * self.width + '|\n'

        rec_ascii = horizon_border
        for _ in range(self.height):
            rec_ascii += vertic_border
        rec_ascii += horizon_border
        return rec_ascii



if __name__ == '__main__':
    rec1 = Rectangle(5,7)
    rec2 = Rectangle(3,6)    
    area = int(rec1)
    print(f"the area is {area}")
    pic = str(rec1)
    print(pic)
    print(str(rec2))