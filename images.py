from PIL import Image, ImageFilter

# img = Image.open("./Pokedex/pikachu.jpg")
# filtered_img = img.convert("L")
# crooked = filtered_img.rotate(180)
# resize = filtered_img.resize((300, 300))
#
# box = (100,100, 400, 400)
# region = filtered_img.crop(box)
# region.save("grey.png", "png")

# filtered_img.show()

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save("thumbnail.jpg")

print(img.size)