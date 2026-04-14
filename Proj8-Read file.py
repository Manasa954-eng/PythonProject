#read the test.txt file
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    #Let's reverse the list
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


