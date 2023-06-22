# bmi kalkulator
nama = "franco"
tinggi_m = 2
berat_kg = 90

bmi = berat_kg / (tinggi_m ** 2)
if bmi < 25:
    print(nama, "tidak overweight")
else:
    print(nama, "overweight! olahraga bro!")