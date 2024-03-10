def generate_door_mat(n, m):

  if not n % 2:
    raise ValueError("n must be an odd natural number")

  # Calculate the center row
  center_row = int(n / 2)

  # Initialize an empty list to store the door mat design
  door_mat = []

  # Build the top half of the door mat
  for i in range(center_row):
    # Calculate the number of '-' characters to print on each side
    border_length = int((m - (i * 3 + 1)) / 2)
    design_string = "-" * border_length + ".|." * (i + 1) + "-" * border_length
    door_mat.append(design_string)

  # Add the welcome message to the center row
  welcome_string = "-" * int((m - len("WELCOME")) / 2) + "WELCOME" + "-" * int((m - len("WELCOME")) / 2)
  door_mat.append(welcome_string)

  # Build the bottom half of the door mat (reverse of the top half)
  for i in range(center_row - 1, -1, -1):
    # Calculate the number of '-' characters to print on each side
    border_length = int((m - (i * 3 + 1)) / 2)
    design_string = "-" * border_length + ".|." * (i + 1) + "-" * border_length
    door_mat.append(design_string)

  return door_mat

# Example usage
n = 7
m = 21
door_mat = generate_door_mat(n, m)

for row in door_mat:
  print(row)
