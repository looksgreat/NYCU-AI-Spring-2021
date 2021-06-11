import numpy as np
import pandas as pd
import seaborn as sns
import io
import requests
import re
import warnings
import os
print(os.listdir("./data"))
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import matplotlib.pyplot as plt
plt.style.use('seaborn-notebook')
from matplotlib.ticker import StrMethodFormatter
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelBinarizer

#I used plotly and sns for the visuals

for dirname, _, filenames in os.walk('/data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
train_data = pd.read_csv("./data/train.csv")
df_train = pd.read_csv("./data/train.csv")
train_data.head()
print(train_data)