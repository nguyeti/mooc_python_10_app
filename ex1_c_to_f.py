"""
This script converts C temp into F temp
"""
# def celsiusToFahrenheit(temperatureC):
#     if temperatureC < -273.15:
#         print("That temperature doesn't make sense!")
#     else:
#         f = temperatureC * (9/5) + 32
#         return f

temperatures = [10, -20, -289, 100]
def writer(temperatures):
    """This is the function to convert C into F"""
    with open("example.txt",'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c * (9/5) + 32
                file.write(str(f) + "\n")
