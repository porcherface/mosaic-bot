# mosaic-bot

generates mosaics by non linear optimization

to launch:
  
     python3 mosaic-bot.py PATH-TO-TARGET-PIC PATH-TO-BUCKET-DIRECTORY
 
the "BUCKET-DIRECTORY" is a dir containing a set of processed images, these images must satisfy the following requirements:
must be same size, and size must be known to program. must be black and white, must be labeled with an index, followed by the mean grayscale intensity and its variance

there are two uploaded buckets in the repo:
- 1200 drow ranger pics
- 2500 chimps pics

you can generate a bucket using image_parser.py 

here an example using the dota2 hero drow ranger.
the bucket is the drow-ranger_edit bucket, generated scraping drow ranger from google images and parsed by image parser. 
the target is a drow ranger picture. scraped pics are not filtered, there might be completely unrelated photos or doubles inside.

    python3 mosaic-bot.py images/targets/drow_portrait.jpeg images/drow_ranger_edit/

all the assets are in the repo, you can run it by yourself

<img src="out_drow.png" width="400"/>

# personal usage  

as mentioned above: if you want to run the code with your set of images you need to know two things:

1) at the current state (0.0.1-prealpha-hobby) this program only accepts same-size black and white pictures
it is possible that the program executes with no errors if you break this law, but the result is not guaranteed

2) all images must have a naming convention, you can't possibly do it manually, check the images folder!!


BUT) i made a fast script to process a scraped set of pics (color, different sizes) and return processed images with correct naming convention. check images/image_parser.py
