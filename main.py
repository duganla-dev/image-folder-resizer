from PIL import Image
from PIL import Image, ImageOps
from os import listdir
from os.path import isfile, join

# ONLY put image files in this fir
InputPath = './input'
# The resized images will be placed in this dir
OutputPath = './output'
# x, y
ImageResize = (266, 375)
# Will Overwrite files if True
Overwrite = False


inputDir = [f for f in listdir(InputPath) if isfile(join(InputPath, f))]
outputDir = [f for f in listdir(OutputPath) if isfile(join(OutputPath, f))]

for fileName in inputDir:
    if fileName not in outputDir or Overwrite == True:
        filePath = InputPath + "/" + fileName

        image = Image.open(filePath)
        image = ImageOps.fit(image, ImageResize, Image.ANTIALIAS, 0, (0.5, 0.5))
        image.save(f'{OutputPath}/{fileName}')
                
        print("Successfully Resized " + fileName + 'To ' + str(ImageResize))
    else:
        print(fileName + 'Already in output directory')


