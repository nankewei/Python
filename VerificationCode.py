from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色
def rndColor():
    return (random.randint(66, 127), random.randint(66, 127),
            random.randint(66, 127))


def rndColor2():
    return (random.randint(129, 255), random.randint(129, 255),
            random.randint(129, 255))


font = ImageFont.truetype('arial.ttf', 36)
width = 240
height = 60
# 创建画板
image = Image.new("RGB", (width, height), (255, 255, 255))
# 以image为画板
draw = ImageDraw.Draw(image)
# 填充每一个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 填充字母
for x in range(4):
    draw.text((60 * x + 10, 10), rndChar(), fill=rndColor2(), font=font)

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save("code.jpg", "jpeg")
