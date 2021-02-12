import os
import glob
import numpy as np
import nibabel as nib
import imageio
import matplotlib
from nibabel.viewers import OrthoSlicer3D
from matplotlib import pylab as plt
from tqdm.notebook import tqdm

#read niifile file
def read_niifile(niifilepath): 
  img = nib.load(niifilepath) #download niifile file (actually extract the file)
  img_fdata = img.get_fdata() #Get niifile data
  return img_fdata

#Save as picture
def save_fig(niifilepath,savepath, format = ".png"):
  output_file = niifilepath[:-7].replace('/content/nii/','')
  fdata = read_niifile(niifilepath) #Call the above function to get data
  (x,y,z) = fdata.shape #Get data shape information: (length, width, dimension-number of slices, fourth dimension)
  for k in tqdm(range(z)):
    silce = fdata[:,:,k] #Three positions represent three slices with different angles
    imageio.imwrite(os.path.join(savepath,f'{output_file}_{k}{format}'),silce)