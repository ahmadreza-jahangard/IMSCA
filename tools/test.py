from demo.predictor import COCODemo
from pysgg.config import cfg
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as T
from pysgg.data import make_data_loader
from PIL import Image
import requests
import matplotlib.pyplot as plt
import random

cfg_path = "/content/SQUAT/configs/e2e_relSQUAT_vg bert.yaml"
cfg.merge_from_file(cfg_path)
cfg.freeze()

data_loaders_val = make_data_loader(cfg, mode="test", is_distributed=False)
tester = COCODemo(cfg)
i = 0
ids = [random.randint(10, 50) for _ in range(20)]
used = []
for batch in data_loaders_val:
  for b in batch:
    
    images,targets,image_ids= b
    if i in ids:
      res = tester.run_on_opencv_image(images, targets, image_ids)
      used.append(image_ids)
    i += 1
    if len(used) == 1:
      break
print(ids)