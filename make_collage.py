# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:17:21 2018

@author: dominik.cichon
"""
import os
import random
import PIL
from photocollage import render, collage


#####################################################################
# Read Images 
#####################################################################

path = '/img'

files = [os.path.join(path, fn) for fn in os.listdir(path)]
img_paths = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
random.shuffle(img_paths)





#####################################################################
# Options
#####################################################################

out_h = 10000
out_w = 20000
savefile = 'collage_01.jpg'


#####################################################################
# Run
#####################################################################


photolist = render.build_photolist(img_paths)



mycollage = collage.UserCollage(photolist)

mycollage.make_page(out_h, out_w)

print(mycollage.page)

enlargement = float(out_w) / mycollage.page.w
mycollage.page.scale(enlargement)


t = render.RenderingTask(mycollage.page, output_file=savefile)
t.start()


t.is_alive == True