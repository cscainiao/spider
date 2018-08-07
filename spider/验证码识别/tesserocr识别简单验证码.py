from PIL import Image
import tesserocr

image = Image.open('123.png')

image = image.convert('L')  # 图像灰度化处理
# image.show()
threshold = 130
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)