import rapidminer
import os
rm_home="C:\Program Files\RapidMiner\RapidMiner Studio"
# If you don't want to see the log messages of the operations, use rm_stdout=open(os.devnull,"w")
connector = rapidminer.Studio(rm_home, rm_stdout=None)
df = connector.read_resource("//Samples/data/Iris")
print("The result is a pandas DataFrame:")
print(df.head())
# project = rapidminer.Project("RapidMiner_Python")

# df = project.read("data/mydata")
# df = rapidminer.Project().read("local/file/path.rmhdf5table")

# project.write(df, "data/mydata_modified")

#con