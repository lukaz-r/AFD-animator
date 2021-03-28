
def readFile(archive):
    with open(archive) as f:
        lines = [line.rstrip() for line in f]
    return lines;


    

        