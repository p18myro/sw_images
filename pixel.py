from PIL import Image

img = Image.open('testphoto.jpg')
# img.show()
# Resize smoothly down to x pixels
imgSmall = img.resize((100, 100), resample=Image.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size, Image.NEAREST)
# result.show()
result.save('new_lefkos.jpg')
