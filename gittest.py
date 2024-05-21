def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  if length <= 0 or width <= 0:
    print("Error: Length and width must be positive numbers.")
    return None  # Indicate error
  else:
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)

if area is not None:
  print(f"The area of the rectangle is: {area}")

