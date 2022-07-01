import pandas as pd
maisons = pd.read_csv("housing.csv")
maisons.info() # getting infos about the dataset
maisons['ocean_proximity'].value_counts() 
