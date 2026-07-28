with open('test.txt', 'r') as f:
    # for line in f:
    #     print(line , end='')
    # f_contents = f.readline()
    # print(f_contents, end = '')
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end = '')

    f.seek(0)
    
    f_contents = f.read(size_to_read)
    print(f_contents)
    
    print(f.tell())
    # while len(f_contents) > 0:
    #     print(f_contents, end ='*')
    #     f_contents = f.read(size_to_read)
