with open('myt.txt') as f:
    with open('myt2.txt', 'w') as f1:
        for line in f:
            f1.write(line)