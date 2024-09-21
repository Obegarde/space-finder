import os
import argparse

parser = argparse.ArgumentParser(description='A program to locate filepaths with spaces in them. Starting with the current working directory')
parser.add_argument('path',default= os.path.dirname(__file__),nargs='?', help = 'Specify the folder you want to start finding spaces from')

args = parser.parse_args()




def space_checker(src): 
    for item in os.listdir(src):
        if " " in item:
            print(f"{src}/{item}")
        if os.path.isdir(os.path.join(src,item)):
            space_checker(f"{src}/{item}")

space_checker(args.path)
