# Implemented in Google collab

#!pip install deepface

import json

from deepface import DeepFace


# face matching

result = DeepFace.verify(img1_path= "/f7.jpeg", img2_path= "/f8.jpeg" )
print(json.dumps(result, indent=2))


# face analysis 

objs = DeepFace.analyze(img_path= "/f7.jpeg",  actions = ['age', 'gender', 'race', 'emotion'])
print(json.dumps(objs, indent=2))
