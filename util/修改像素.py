from PIL import Image



def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

if __name__ == '__main__':
    for i in range(1, 44):
        file_in = "template" + str(i) + ".jpg"
        width = 608
        height = 608
        file_out = "tem" + str(i) + ".jpg"
        produceImage(file_in, width, height, file_out)