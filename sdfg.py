from PIL import Image
import os
h = os.listdir()
for file_name in h:
    try:
        image = Image.open(file_name)
        new_image = image.rotate(90, expand=True)
        new_image.convert("RGB").save('1' + file_name)
        #new_image.show()
        image.close()
        new_image.close()
    except:
        pass