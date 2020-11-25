from __future__ import print_function
import numpy as np
import argparse
from PIL import Image, ImageFilter
import time

import chainer
from chainer import cuda, Variable, serializers
from net import *

from pathlib import Path

selectedModel = ""
selectedContent = ""
path=Path(__file__).parent
with open(str(path)+"/../static/media/" +"/content-file.txt",'r') as f:
    selectedContent = str(path)+'/' +f.read()
with open(str(path)+"/../static/media/" +"/style-file.txt",'r') as f:
    selectedModel = str(path)+'/'+f.read()

output_file_name = selectedContent[75:-4]+"_"+selectedModel[50:-6]+".jpg"

# print(selectedContent)
# print(selectedModel)
# print("out: "+output_file_name)

# from 6o6o's fork. https://github.com/6o6o/chainer-fast-neuralstyle/blob/master/generate.py
def original_colors(original, stylized):
    h, s, v = original.convert('HSV').split()
    hs, ss, vs = stylized.convert('HSV').split()
    return Image.merge('HSV', (h, s, vs)).convert('RGB')

model = FastStyleNet()
serializers.load_npz(selectedModel, model)
xp = np

start = time.time()
original = Image.open(selectedContent).convert('RGB')
image = np.asarray(original, dtype=np.float32).transpose(2, 0, 1)
image = image.reshape((1,) + image.shape)
image = np.pad(image, [[0, 0], [0, 0], [50, 50], [50, 50]], 'symmetric')
image = xp.asarray(image)
x = Variable(image)

y = model(x)
result = cuda.to_cpu(y.data)

result = result[:, :, 50:-50, 50:-50]
result = np.uint8(result[0].transpose((1, 2, 0)))
med = Image.fromarray(result)
med = med.filter(ImageFilter.MedianFilter(3))
print(time.time() - start, 'sec')

med.save(str(path)+"/../static/media/output/_.jpg")

