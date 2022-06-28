import pandas
import pandas
from utils.connection import connector
from sklearn.datasets import load_iris

# rm_main is a mandatory function, 
# the number of arguments has to be the number of input ports (can be none)
def rm_main():
    sklearn_iris = load_iris()
    iris = pandas.DataFrame(sklearn_iris["data"], columns=sklearn_iris["feature_names"])
    iris["target"] = sklearn_iris["target"]
    # set the parameter to the desired repository location
    connector.write_resource(iris, "//Local Repository/data/Iris")
    return iris.head(5)


if __name__ == '__main__':
    print(rm_main())