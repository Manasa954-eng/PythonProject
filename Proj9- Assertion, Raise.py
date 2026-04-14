Itemsincart = 0

#if Itemsincart != 2:
    #raise Exception("Error!")

#assert(Itemsincart==0)

#For Exception Handling

#With customized error
try:
    with open('test1.txt','r') as reader:
        reader.read()

except:
    print("There is an error")

#With python error which is a good way
try:
    with open('test1.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

#finally block is used no matter the test is failed or passed
finally:
    print("Delete all the records")