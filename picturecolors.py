
from PIL import Image
# RGB values for recoloring.
darkBlue = (133, 19, 223)
red = (234, 42, 112)
lightBlue = (66, 244, 235)
yellow = (126, 138, 249)

# Import image.
my_image = Image.open("prayingotter.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.
#photo = input("What photo do you want to recolor?")
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
#print (image_list)
#print (image_list[0][0])
#print (image_list[0])
#print(sum(image_list[0]))
#for pixel in image_list:
#    print(pixel[0])
for pixel in image_list:
    intensity = sum(pixel)
    if intensity < 182:
        recolored.append(darkBlue)
    elif (intensity >= 182) and (intensity < 364):
        recolored.append(red)
    elif (intensity >= 364) and (intensity < 546):
        recolored.append(lightBlue)
    else:
        recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
