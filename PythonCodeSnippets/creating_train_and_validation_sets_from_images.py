# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:00:50 2020

- Given a folder of cats and dog images, create training and validation sets
- In general, given a folder of data files from 'n' classes, create training and validation sets

@author: cgokh
"""

import os
import random
import shutil

# Parent dir path
# My images were in /parent_dir/train/
parent_path = 'C:\\DataScience\\Kaggle\\dogs_vs_cats\\train'

# Getting names of all files including format
all_files = os.listdir(os.path.join(parent_path, 'train'))

# Segregating cat and dog files
# cat files start with 'cat' and dog files with 'dog'
cat_files = []
dog_files = []
for filename in all_files:
    if filename[:3] == 'cat':
        cat_files.append(filename)
    elif filename[:3] == 'dog':
        dog_files.append(filename)
    else:
        raise Exception("Error. Neither dog nor cat")

# Stats

# len(cat_files)
# Out[9]: 12500

# len(dog_files)
# Out[10]: 12500

# There are a total of 25k files, 12.5k each for cats and dogs
# We don't need to use these much
# We will first select a subset of 3k each from dogs and cats
# Then we will divide them into train and validation as 2k and 1k in each group

# Selecting 3k of 25k files
file_range_cats_and_dogs = range(0, len(cat_files))
cat_sample = random.sample(file_range_cats_and_dogs, 3000)	
dog_sample = random.sample(file_range_cats_and_dogs, 3000)


# Create a directory structure
# /training/cats - 2000
# /training/dogs - 2000
# /validation/cats - 1000
# /validation/dogs - 1000

os.chdir(parent_path)
os.mkdir('subset')
os.chdir(os.path.join(parent_path, 'subset'))
os.mkdir('training')
os.mkdir('validation')
os.chdir(os.path.join(parent_path, 'subset', 'training'))
os.mkdir('cat')
os.mkdir('dog')
os.chdir(os.path.join(parent_path, 'subset', 'validation'))
os.mkdir('cat')
os.mkdir('dog')


# Copy/cut and paste the images in the target directories
target_dir_train_cat = os.path.join(parent_path, "subset", "training", "cat")
target_dir_valid_cat = os.path.join(parent_path, "subset", "validation", "cat")

target_dir_train_dog = os.path.join(parent_path, "subset", "training", 'dog')
target_dir_valid_dog = os.path.join(parent_path, "subset", "validation", 'dog')

pick_files_from_path = os.path.join(parent_path, "train")


# indexes of each folder
index_train_cat = random.sample(cat_sample, 2000)
index_valid_cat = [i for i in cat_sample if i not in index_train_cat]
index_train_dog = random.sample(dog_sample, 2000)
index_valid_dog = [i for i in dog_sample if i not in index_train_dog]



# Finally moving files using shutil package
# Changing directory to the path where files are is very important
os.chdir(os.path.join(parent_path, 'train'))

for index in index_train_cat:
    shutil.copy(cat_files[index], target_dir_train_cat)
    
for index in index_valid_cat:
    shutil.copy(cat_files[index], target_dir_valid_cat)
    
for index in index_train_dog:
    shutil.copy(dog_files[index], target_dir_train_dog)
    
for index in index_valid_dog:
    shutil.copy(dog_files[index], target_dir_valid_dog)







