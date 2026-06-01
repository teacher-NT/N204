

with open("image.jpeg", "rb") as file:
    pixels = list(file.read())
    # for i in pixels:
    #     print(i, end=" ")
    print(len(pixels))
