import pandas as pd
from google.colab import drive

drive.mount('/gdrive', force_remount=True)
csv_path = "/gdrive/Shared drives/folder/folder/name.csv"
df = pd.read_csv(csv_path, encoding='latin1')
df.head()