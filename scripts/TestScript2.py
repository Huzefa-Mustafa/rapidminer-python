from pandas import DataFrame

def rm_main(a):
    data = DataFrame(dict(
        id = (1,2,3),
        values = ("A","B","C")

    ))
    # d = DataFrame([str(a.rm_metadata)])
    return data,a.head()