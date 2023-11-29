def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    artists = content.split(",")
    for artist in artists: #prints each element in string in different line
        print(artist.strip())


def write_file(file, string):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    

filename = "examples.txt"
write_file(filename, "Bongus, Biggie Cheese, Big Fat Rat")
read_file(filename)
