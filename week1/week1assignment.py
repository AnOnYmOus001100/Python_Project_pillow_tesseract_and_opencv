import PIL
from PIL import Image
from PIL import ImageEnhance
#importig ImageFont and ImageDraw modules for Font Formatting and Image Formatting
from PIL import ImageFont
from PIL import ImageDraw

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different color
image_list=[] #list to hold 9 images
lable_list=[] #list to hold the font for 9 images

#iterating over i from 0 to 3, for channnel 1 to 3 and j over 0.1,0.5,0.9 for intesities
for i in range(3):
    for j in (0.1,0.5,0.9):
        source = image.split()
        mid = source[i].point(lambda x:x*j)
        source[i].paste(mid)
        img = Image.merge(image.mode, source)
        #using appropiate formatting to create the lables
        lable_list.append('channel {} intensity {}'.format(i,j))
        image_list.append(img)
        
#setting font to truetype font loacated in readonly/fanwood-webfont.ttf with a size of 75
font = ImageFont.truetype("readonly/fanwood-webfont.ttf",75)
# create a contact sheet from different color
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+3*85))
x=0
y=0
#drawing the image using Draw on the contact sheet
draw = ImageDraw.Draw(contact_sheet)
for i,image in enumerate(image_list):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(image, (x, y) )
    #drawing the text on the contact sheet at appropiate position
    draw.text((x,y+first_image.height+5), lables[i], font=font)
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+85
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
