import pandas

# rm_main is a mandatory function, 
# the number of arguments has to be the number of input ports (can be none),
#     or the number of input ports plus one if "use macros" parameter is set
# if you want to use macros, use this instead and check "use macros" parameter:
#def rm_main(data,macros):
def rm_main():
    print('Hello, world!')
    # output can be found in Log View
    # print(type(data))

    #your code goes here

    #for example:
    data2 = pandas.DataFrame([3,5,42,8])

    # connect 2 output ports to see the results
    return data2