#!/usr/bin/env python3

# This script recursively looks in the `img` directory for image paths, then
# generates image_data.json.

import os
import json

image_tuples = []
for (dirpath, dirnames, filenames) in os.walk("img"):
    for filename in filenames:
      image_path = os.path.join(dirpath, filename)
      image_tuple = {"image": image_path}
      image_tuples.append(image_tuple)

with open('image_data.json', 'w') as outfile:
    json.dump(image_tuples, outfile)

