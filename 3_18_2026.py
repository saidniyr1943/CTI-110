

#calculate the area of a circle
#function name is areaaCircle
#parameters are : int, radius and Pi
#retur float (area of a circle)

def areaCircle(radius):
    Pi=3.14
    A= Pi*radius*radius
    return A           


def header(funcName):
    print(f"{'':=^60}")
    print(f" {funcName:=^60} ")
    print(f"{'':=^60}")      



def main():
    (header("areaCircle"))
    print(areaCircle(5))    
