# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_lists_access.asp

# You are given the following list of colors:
# colors = ["red", "green", "blue", "yellow", "purple"]
#
# Write a function color_info(items) that:
#   - prints the first color
#   - prints the last color
#   - prints the second and third colors using slicing
#
# Call the function with colors.
# 
# Write your code here:
colors = ["red", "green", "blue", "yellow", "purple"]
def color_info(items):
    print(f"First color: {items[0]}")
    print(f"Last color: {items[-1]}")
    print(f"Second and third colors: {items[1:3]}")
color_info(colors)