"""Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres."""

length = int(input("enter the length of fieldin feet \t"))
width = int(input("enter the width of field in feet\t"))

area_in_squarefeet = length*width

print(f"{area_in_squarefeet} square feet")
print(f"{area_in_squarefeet/43560} acres")
