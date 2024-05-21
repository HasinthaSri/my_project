def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  if length <= 0 or width <= 0:
    print("Error: Length and width must be positive numbers.")
    return None  
  else:
    area = length * width
    return area


def get_unit_choice():
  """Prompts user for unit choice (feet or meters)."""
  while True:
    unit = input("Enter the unit (ft or m): ").lower()
    if unit in ("ft", "m"):
      return unit
    else:
      print("Invalid unit. Please enter 'ft' or 'm'.")


def calculate_perimeter(length, width):
  """Calculates the perimeter of a rectangle."""
  perimeter = 2 * (length + width)
  return perimeter


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


unit = get_unit_choice()


area = calculate_area(length, width)
if area is not None:
  if unit == "ft":
    area *= 0.0929  # Convert to square meters if ft is chosen
  print(f"The area of the rectangle is: {area:.2f} {unit.upper()}")


perimeter = calculate_perimeter(length, width)
print(f"The perimeter of the rectangle is: {perimeter:.2f} {unit.upper()}")
