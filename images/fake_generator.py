# fake_generator.py

import random

RES_X = 20
RES_Y = 20

dest_fld = "fakes/"


from PIL import Image

# for each image 
index = 0
MAX = 4000
while index < MAX:
	
	THIS = int( 255*random.random() )

	new = Image.new(mode="L", color= THIS, size=(RES_X,RES_Y))
	

	# evaluate coarsed parameters 
	# - average pixel
	# - pixel variance? 
	# - rescaled pixel block?


	# give an unique incremental index 	
	# name new file and save in dest folder
	newname = str(index).zfill(5)+"_"+str(int(THIS))+"_.png"
	new.save(dest_fld+newname)
	index = index + 1
