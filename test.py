

import cv2
from  LeptonDataConverter import * 
from  tifffile  import TiffFile  
#import argparse 


filename = "test_2.tiff"

tif = TiffFile(filename) 

conv = LeptonDataConverter()

for page in tif.pages :

    conv.setRawData(page.asarray())

    im = conv.getRGBImage() 
  
    cv2.imshow("wind" , im)

    cv2.waitKey(0)
