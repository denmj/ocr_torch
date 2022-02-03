import numpy as np
import pandas as pd
import copy
import csv
import functools
import glob
import os
from utils.logconfig import logging

log = logging.getLogger(__name__)
# log.setLevel(logging.WARN)
# log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


annotation_data = pd.read_csv('D://LUNA_Dataset//data_unversioned//part2//luna//annotations.csv')

print(annotation_data.head(5))
