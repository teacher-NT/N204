import os
os.system("cls")

salon = {
    "BMW": [
        {
            "model": "M3",
            "price": 12000,
            "color": 'black'
        },
        {
            "model": "I8",
            "price": 45000,
            "color": 'White'
        }
    ],
    "Mercedes Benz": [
        {
            "model": "Maybach",
            "price": 200000,
            "color": 'black'
        },
        {
            "model": "CLS",
            "price": 63000,
            "color": 'grey'
        }
    ],
    "BYD": [
        {
            "model": "Song Plus",
            "price": 40000,
            "color": 'black'
        },
        {
            "model": "Chazor",
            "price": 22000,
            "color": 'White'
        }
    ]
}

for i in salon:
    print("= " * 15)
    print(i)
    for j in salon[i]:
        print("\t", "- "*10)
        for k in j:
            print(f"\t{k} : {j[k]}")
        