#Konversi suhu dari kelvin ke Celcius
def k_to_c(K):
  E = K - 273.15
  print(f'Suhu dalam Celcius ( C ) = {E}')
  return E

k_to_c(300)