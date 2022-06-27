import os
from utils.connection import connector


def rm_main():
    df = connector.read_resource("//Samples/data/Iris")
    print("The result is a pandas DataFrame:")
    return df.head()