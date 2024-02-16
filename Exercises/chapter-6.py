# q1
with open('test.txt', 'r') as file:
    contents = file.read()
    cleaned_contents = contents.replace(" ", "").replace("\n", "")
    print(cleaned_contents)

# q2
def is_float(str):
  try:
    float_val = float(str)
    return True
  except ValueError:
    return False
