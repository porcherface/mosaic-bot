# mosaic-bot

to launch:
  
     python3 mosaic-bot.py PATH-TO-TARGET-PIC PATH-TO-BUCKET-DIRECTORY
 

here an example using the dota2 hero drow ranger.
the bucket is a preformatted set of random pictures ddowloaded from google images with query "drow ranger dota2". 
the target is a drow ranger picture.

    python3 mosaic-bot.py images/targets/drow_portrait.jpeg images/drow_ranger_edit/

all the assets are in the repo, you can run it by yourself

<img src="out_drow.png" width="400"/>

# personal usage  

if you want to run the code with your set of images you need to know two things:

1) at the current state (0.0.1-prealpha-hobby) this program on accepts same-size black and white pictures
it is possible that the program executes with no errors if you break this law, but the result is not guaranteed

2) all images must have a naming convention, you can't possibly do it manually, check the images folder!!


BUT) i made a fast script to process a scaped set of pics (color, different sizes) and return processed images with correct naming convention
