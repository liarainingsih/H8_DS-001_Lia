import celcius_to_fahrenheit
import kelvin_to_fahrenheit

def Temperature_to_Fahrenheit(suhu, degree):
  if suhu == 'C':
    celcius_to_fahrenheit.c_to_f(degree)
  elif suhu == 'K':
    kelvin_to_fahrenheit.k_to_f(degree)

Temperature_to_Fahrenheit('C', 70)
Temperature_to_Fahrenheit('K', 90)