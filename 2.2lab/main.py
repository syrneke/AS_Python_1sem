# вар9

def TypeTrl(x1, y1, x2, y2, x3, y3):
    AB2 = (x2 - x1)**2 + (y2 - y1)**2
    BC2 = (x3 - x2)**2 + (y3 - y2)**2
    CA2 = (x1 - x3)**2 + (y1 - y3)**2
    
    AB = AB2**0.5
    BC = BC2**0.5
    CA = CA2**0.5
    
    if abs(AB - BC) < 0.001 and abs(BC - CA) < 0.001:
        return "равносторонний"
    
    elif (abs(AB - BC) < 0.001) or (abs(BC - CA) < 0.001) or (abs(CA - AB) < 0.001):
        return "равнобедренный"
    
    sides = [AB2, BC2, CA2]
    sides.sort()
    
    if abs(sides[2] - (sides[0] + sides[1])) < 0.001:
        return "прямоугольный"
    else:
        return "обычный"
print("Тестируем функцию:")
print(TypeTrl_simple(0, 0, 1, 0, 0, 1)) 
print(TypeTrl_simple(0, 0, 2, 0, 1, 1))
