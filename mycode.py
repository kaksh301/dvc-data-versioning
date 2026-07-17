import pandas as pd
import os 

data = {
    "name":["kaksh","kaksh2","kaksh3"],
    "age" : [21,22,23],
    "gender" : ["male","male","male"]
}

df = pd.DataFrame(data)

make_dir = "data"

os.makedirs(make_dir,exist_ok=True)

path = os.path.join(make_dir,"sample_data.csv")

df.to_csv(path,index=False)