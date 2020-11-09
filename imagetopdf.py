import sys
from PIL import Image


def transparentToWhite(image):
    width, height = image.size
    print("Image Width: ", width, " Height: ", height)
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = image.getpixel(dot)
            if len(color_d) == 4:
                if(color_d[3] == 0):
                    color_d = (255, 255, 255, 255)
                    image.putpixel(dot, color_d)


def imagetopdf(inputPaths):
    for inputPath in inputPaths:
        image = Image.open(inputPath)
        imageName = inputPath.split(".")[0]
        transparentToWhite(image)
        outputImg = image.convert('RGB')
        outputImg.save(imageName + ".pdf", quality=95)


inputPaths = sys.argv[1:]
imagetopdf(inputPaths)
print("convert finished!")
