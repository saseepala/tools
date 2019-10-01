import os
import glob
import fileinput
from datetime import datetime

src_path = os.path.join("C:\\", "Users", "sg317l", "Source", "dot-net")
#src_path = os.path.join("C:\\", "Users", "sg317l", "Desktop", "scripts", "test")
excluded_files = ["AssemblyInfo.cs"]
current_year = datetime.today().year

def add_signatures(folder):
    if (not os.path.exists(folder)):
        print ("not found " +  folder)
        return
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isdir(path):
            add_signatures(path)
        elif os.path.isfile(path):
            name, ext = os.path.splitext(path)
            filepath, filename = os.path.split(path)           
            if filename not in excluded_files and ext == '.cs':
                add_signature(path)          
        else:
            print("not found " + path)
   
def add_signature(filename):
    signature_added = False
    f = fileinput.input(filename, inplace=1)
    first_non_empty_line_found = False
    add_signature = False
    for xline in f:
        add_signature = False
        if not first_non_empty_line_found and xline.strip():
            first_non_empty_line_found = True
            if not xline.startswith('/*'):
                add_signature = True              
            
        if add_signature:
            signature_added = True
            print("/**")
            print("* @copyright " + str(current_year) + " Wayfair LLC - All rights reserved")
            print("**/")
            print()
            print(xline, end = '')
        else:
            if first_non_empty_line_found:
                print(xline, end = '')
                
    if signature_added:
        print ("Signature added to " + filename)
    
def add_signatures_to_cost_dirs():
    print ("Scanning all Cost folders in " + src_path)
    for file in glob.glob(os.path.join(src_path, 'Wayfair.SCS.Cost*')):
        add_signatures(file)


add_signatures_to_cost_dirs()
