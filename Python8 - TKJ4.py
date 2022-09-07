list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["Naufal", "Fadli", "Abyan", "Desta"]
list_mix = [20, "Arya", True, "Bryan"]

print("Data Sebelum diubah:", list_string)
list_string[1] = "Jamil"
print("Data Setelah diubah:", list_string)

print("Data Sebelum diubah:", list_string)
list_string[2] = "Rydho"
print("Data Setelah diubah:", list_string)

print("Data Sebelum diubah:", list_mix)
list_mix[0] = 30
print("Data Setelah diubah:", list_mix)

print("Data Sebelum diubah:", list_mix)
list_mix[1] = "Dimas"
print("Data Setelah diubah:", list_mix)

print("Data Sebelum diubah:", list_mix)
list_mix[2] = "Gatau"
print("Data Setelah diubah:", list_mix)

print("Data Sebelum diubah:", list_mix)
list_mix[3] = "Icak"
print("Data Setelah diubah:", list_mix)

# pengulangan for

x = ["Naufal", "Fadli", "Abyan", "Desta"]
for y in x :
    print(y)

print("\n")
for i in list_string:
      print(i)
      
print("\n")
for a in list_mix:
    print(a)

print("\n")
for b in list_integer:
    print(b)

