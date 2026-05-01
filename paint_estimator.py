'''
Sadie Crandall
IS 303 - AO1

Paint Estimator
This program estimates the amount of paint (in gallons) needed to paint a wall based on user inputs.

Inputs:
- Room name (string)
- wall height in ft (float)
- wall width in ft (float)


Processes:
- calculates the area of the wall (height * width)
- calculates the amount of paint needed by dividing the area by 350 (1 gallon covers 350 sq ft)


Outputs:
-Prints the room name, wall dimensions, and the estimated amount of paint needed in a formatted manner.


'''

room_name = input("Enter the room name: ")
wall_height = float(input("Enter the wall height in feet: "))
wall_width = float(input("Enter the wall width in feet: "))

gallons_needed = (wall_height * wall_width) / 350

print("---")
print(f"Room: {room_name} | Wall Height: {wall_height} ft | Wall Width: {wall_width} ft")
print(f"Area of the wall: {wall_height * wall_width:.2f} sq ft")
print(f"Estimated amount of paint needed: {gallons_needed:.2f} gallons")
print("---")