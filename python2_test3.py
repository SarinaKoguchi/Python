from PIL import Image

def image_width():
    width = image.width
    print(width)
    return width

def image_height():
    height = image.height
    print(height)
    return height

def aspect_ratio(width, height):
    x, y = width, height
    while y:
        x, y = y, x % y
    print(f"{width/x}:{height/x}")

# 任意の画像のサイズ、アスペクト比を出力
image = Image.open("sample.png")
aspect_ratio(image_width(), image_height())