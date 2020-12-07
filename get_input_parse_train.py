# Imports python modules
import argparse
import os, sys

# Input parser based on first project
# 

std_path = str(sys.path[0])

def get_input_parse_train():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Set directory to save checkpoints: python train.py data_dir --save_dir save_directory      
      2. CNN Model Architecture as --arch with default value 'vgg13'
      3. Set hyperparameters: python train.py data_dir 
        a) --learning_rate 0.003 
        b) --hidden_units 512 
        c) --epochs 20
      4. Use GPU for training: python train.py data_dir --gpu
      
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    
    parser = argparse.ArgumentParser()
    
    # Create command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('data_dir', type=str, default = 'flowers',
                        help='Folder that contains the images (default: ./flowers ')
    
    parser.add_argument('--save_dir', action='store', type=str, default = std_path,
                        help='Folder to save checkpoint.pth in (default: current path)')
    
    parser.add_argument('--arch', type=str, default = 'vgg', 
                        help='The CNN model architecture to use (default: VGG16)')
    
    parser.add_argument('--lr', type=float, default = 0.003,
                        help='Sets the learning rate for the training model (default: 0.003)')
    
    parser.add_argument('--huts', type=int, default = 512,
                        help='Sets the hidden units for the training model (default: 512)')
    
    parser.add_argument('--eps', type=int, default = 5,
                        help='Sets the epochs for the training model (default: 5)')
    
    parser.add_argument('--gpu', type=bool, default = True,
                        help='True/False: device where training will be performed (default: True)')
    
    
    return parser.parse_args()

