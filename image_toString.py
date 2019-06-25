import base64
 
with open("_images/img1.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    

with open("_images/imageToSave.png", "wb") as fh:
    fh.write(base64.b64decode(str))
    