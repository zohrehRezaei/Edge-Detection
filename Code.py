#import dicom 
import pydicom as dicom
import pandas as pd
import glob
import os
from tqdm import tqdm
#import cv2
from PIL import Image
outdir = '/tmp'
folder_path = "C:\\Users\\snapp\\Desktop\\Data Science (Goalearn)\\Task 1\\dicom_dir"
images_path = os.listdir(folder_path)


def dictify(ds):
    output = dict()
    for elem in ds:
        if elem.VR != 'SQ': 
            output[elem.tag] = elem.value
        else:
            output[elem.tag] = [dictify(item) for item in elem]
    return output

metadata_dicom= []
image_names_train = []
for i in tqdm(range(len(images_path))):
    t = os.listdir(folder_path+images_path[i])
    for j in range(len(t)):
        img_path = os.listdir(folder_path+images_path[i]+'/'+t[j])
        for k in range(len(img_path)):
            #ds = dicom.dcmread(folder_path+images_path[i]+'/'+t[j]+'/'+img_path[k])
            ds1 = dicom.dcmread(folder_path+images_path[i]+'/'+t[j]+'/'+img_path[k], stop_before_pixels=True)
            metadata_dicom.append(dictify(ds1))
            #img = ds.pixel_array
            #im = Image.fromarray(img)
            #im.save(img_path[k].replace('.dcm','.png'))
            #image_names_train.append(img_path[k].replace('.dcm','.png'))


train = pd.DataFrame(metadata_dicom)      
train.head()