## Conversion from Celsius to Farenheit
degree_sign = u"\u00b0"

# Request input
temp = input ("What is the Celsius temperature that you would like to convert to Fahrenheit? ")

# Convert input temp to float
float_temp = float(temp)

# Convert the temp into farenheight
farenheit = (9/5) * float_temp + 32 

# Print the tempertaure in farenheight
print (temp, degree_sign, "C Is " ,farenheit ,degree_sign,"F")