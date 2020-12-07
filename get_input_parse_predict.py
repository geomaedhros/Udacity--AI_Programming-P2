# Imports python modules
import argparse
import os, sys
import glob 
import random

# Input parser based on first project
# 

std_path = str(sys.path[0])
rnd_pic = random.choice(glob.glob(os.path.join(std_path, 'flowers/test/*/*.jpg')))

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
    
    parser.add_argument('--img_path', type=str, default = os.path.join(std_path, 'flowers/checkpoint.pth'),
                        help='Path that contains the checkpoint (default: ./checkpoint.pth ')
    
    parser.add_argument('--load_path', type=str, default = os.path.join(std_path, 'checkpoint.pth'),
                        help='Path that contains the checkpoint (default: ./checkpoint.pth ')
        
    parser.add_argument('--catg_names', type=str, default = 'cat_to_name.json',
                        help='Mapping of categories to real names (default: cat_to_name.json')   
   
    parser.add_argument('--gpu', type=str, default = True,
                        help='Use GPU for inference (default: True)')
    
    
    return parser.parse_args()

