# Imports python modules
import argparse
import os, sys
import glob 
import random

# Input parser based on first project
# 

from get_input_parse_train import std_path

def get_input_parse_predict():
    """
        Predict flower name from an image with predict.py along with the probability of that name. 
        That is, you'll pass in a single image /path/to/image and return the flower name and class probability.

        Basic usage: python predict.py /path/to/image checkpoint
        Options:
        1) Return top KK most likely classes: python predict.py input checkpoint --top_k 3
        2) Use a mapping of categories to real names: python predict.py input checkpoint --category_names cat_to_name.json
        3) Use GPU for inference: python predict.py input checkpoint --gpu  

    """
    # Create Parse using ArgumentParser
    
    parser = argparse.ArgumentParser()
    
    # Create command line arguments as mentioned above using add_argument() from ArguementParser method
        
    parser.add_argument('--top_k', type=int, default = 3,
                        help='Return top KK most likely classes (default: 3')
    
    parser.add_argument('--img_path', type=str, default = 'flowers/test/1/image_06743.jpg',
                        help='Path that contains the checkpoint (default: ./flowers/test/1/image_06743.jpg')
    
    parser.add_argument('checkpoint', action='store', type=str, default = '/checkpoint.pth',
                        help='Path that contains the checkpoint (default: ./checkpoint.pth ')
        
    parser.add_argument('--catg_names', type=str, default = 'cat_to_name.json',
                        help='Mapping of categories to real names (default: ./cat_to_name.json')   
   
    parser.add_argument('--gpu', type=bool, default = True,
                        help='True/False: Use GPU for inference. default: True)')
    
    
    return parser.parse_args()

