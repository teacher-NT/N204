
# dict1 = {
#     "ism": "Saidaloxon",
#     "familya": "Tokhirov",
#     "yosh": 15,
#     "manzil": "Farg'ona"
# }

# with open("N204/fayl/data.txt", "w") as file:
#     for i in dict1:
#         file.write(f"{i}:{dict1[i]}\n")


import json

dict1 = {
    "ism": "Saidaloxon",
    "familya": "Tokhirov",
    "yosh": 15,
    "manzil": "Farg'ona"
}

with open("N204/fayl/data.json", "w") as file:
    json.dump(dict1, file, indent=4)


with open("N204/fayl/data.json", "r") as file:
    data = json.load(file)
    print(data['ism'])