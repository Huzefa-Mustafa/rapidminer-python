import os
from utils.connection import connector
# rm_main is a mandatory function, 
# the number of arguments has to be the number of input ports (can be none)
def rm_main():
    iris, deals, golf = connector.read_resource(["//Samples/data/Iris", "//Samples/data/Deals", "//Samples/data/Golf"])
    print("The result are pandas DataFrames")
    print(iris.head(1))
    print(deals.head(1))
    print(golf.head(1))
    return iris.head(1) , deals.head(1), golf.head(1)

if __name__ == '__main__':
    rm_main()