with open('test.txt', "r") as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

    

# for pictures we need binary read and write

with open('test.jpg', "rb") as ri:
    with open('test_copy.jpg', 'wb') as wi:
        for line in ri:
            wi.write(line)

    
