# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import charset_normalizer

# set seed for reproducibility
np.random.seed(0)


sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

new_entry = sample_entry.decode("big5-tw").encode("utf-8")

#didn't work with 10x fewer charecters
with open("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", "rb") as rawData:
    result = charset_normalizer.detect(rawData.read(100000))
print(result)

police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv",
                             encoding="windows-1250")


police_killings.to_csv("/kaggle/working/my_file.csv")
