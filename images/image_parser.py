# image_parser.py
file_type = "stupid_script"
# some run params 

RES_X = 300
RES_Y = 200

src_fld  = "original/*.png"
dest_fld = "edited/"


# for an easy parsing lib
import glob
# for an easy data acquisition
from PIL import Image, ImageEnhance

# get all images in a list

# for each image 
index = 0
for image in glob.glob(src_fld):

	# remove path
	filename = image.split("/")[-1]


	# open the img
	preview = Image.open(image)
	#preview.show()

	# make it black/white
	preview = preview.convert("L")
	#preview.show()

	# resize to RES_X, RES_Y
	preview = preview.resize((RES_X,RES_Y))
	#preview.show()

	# evaluate coarsed parameters 
	width, height = preview.size
	total = 0
	for i in range(0, width):
		for j in range(0, height):
			total += preview.getpixel((i,j))

	mean = total / (width * height)
	# - average pixel
	# - pixel variance? 
	# - rescaled pixel block?


	# give an unique incremental index 	
	# name new file and save in dest folder
	newname = str(index).zfill(3)+"_"+str(int(mean))+"_.png"
	print("converting "+filename+" to "+newname)
	preview.save(dest_fld+newname)
	index = index + 1