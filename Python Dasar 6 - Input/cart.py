item = input("Barang apa yang kamu beli? ")
harga = float(input("Berapa harga satu itemnya? "))
jumlah = int(input("Berapa jumlahnya? "))

total = harga * jumlah

print(f"Kamu membeli {jumlah}x {item}")
print(f"Dengan harga total {total}")