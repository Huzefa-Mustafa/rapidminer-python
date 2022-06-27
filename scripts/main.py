import os
from utils.connection import connector


def rm_main():
    df = connector.read_resource("//Samples/data/Iris")
    print("The result is a pandas DataFrame:")
    print(df.head())
    return df.head()


if __name__ == '__main__':
	rm_main()
