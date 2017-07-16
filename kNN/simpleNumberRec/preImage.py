from PIL import Image  
import os

def scaleImages():
    resdir = './res'
    for x in os.listdir(resdir):
        ifile = os.path.join(resdir,x)
        print ifile
        if os.path.isfile(ifile):
            im = Image.open(ifile)
            im.thumbnail((50,50))
            im.save(x+'.jpg','jpeg')
