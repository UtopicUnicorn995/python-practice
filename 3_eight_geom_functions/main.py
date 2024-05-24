import math

def circle_area(type, value):
    if type.lower() == 'radius':
        return f"The area of the circle is {math.pi * (value * value)}"
    elif type.lower() == 'diameter':
        return f"The area of the circle is {(math.pi/4) * (value * value)}"
    elif type.lower() == 'circumference':
        return f"The area of the circle is {(value * value) / (4*math.pi)}"
    else:
        return 'We could not calculate area based on the values you have given.'
    
def circle_circumference(radius):
    return f"The circumference of the circle is {(2 * math.pi) * radius}."

def rectangle_area(width, length):
    return f"The area of the rectangle is {width * length}."

def rectangle_perimeter(width, length):
    return f"The perimeter of the rectangle is {2 * (width + length)}."

def triangle_area(base, perpendicular_height):
    return f"The area of the triangle is {(base / 2) * perpendicular_height}."

def triangle_perimeter(side1, side2, side3):
    return f"The perimeter of the triangle is {side1 + side2 + side3}."

def sphere_surface_area(radius):
    return f"The surface area of the sphere is {4 * math.pi * (radius * radius)}."

def sphere_volume(radius):
    return f"The volume of the sphere is {4/3 * math.pi * (radius ** 3)}."

shape = input("What shape do you want to have it's measurements? ")

if shape.lower() == 'circle':
    geom_func = input("What function do you want to ues? [circumference, area]")
    if geom_func == 'area':
        input("Give the type of value you have. [radius, diameter, circumference]; Also kindly give it's value separated by comma.")
    elif geom_func == 'circumference':
        circumference = input('What is the radius of the circle that we could use to solve for the circumference.')
        print(circle_circumference(circle_circumference))
    else:
        print('The function does not exist.')

