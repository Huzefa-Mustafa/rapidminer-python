from pandas import DataFrame

def rm_main(file):
    data = DataFrame(dict(
        id = (1,2,3),
        values = ("A","B","C")
    ))
    d = DataFrame([str(file.rm_metadata)])
    return data,d