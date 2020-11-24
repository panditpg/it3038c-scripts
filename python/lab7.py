
##virtualenv /venv/pillow
##venv/webscraping/scripts/activate.ps1
##pip install pillow

##from PIL import Image, ImageFilter
##import string
##myImage = Image.open
##myImage.load


##myImage.format
##myImage.size
##myImage.show()


##blur = myImage.filter(ImageFilter(BLUR)).show()
##quit()

from PIL import Image;
 
#Open existing image
OriImage = Image.open('images/lamb.jpg')
OriImage.show()

#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
boxImage.show()

#Save Boxblur image
boxImage.save('images/boxblur.jpg')