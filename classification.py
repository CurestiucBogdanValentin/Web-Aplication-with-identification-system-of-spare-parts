from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os, os.path 
import sys

# Load the model

with open('labels.txt', 'r') as f:
 class_names= f.read().split('\n')

print(class_names)


