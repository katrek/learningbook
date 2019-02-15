def main():

    file_read = open('numbers.txt', 'r')
    line = file_read.readline()
    line2 = file_read.readline()
    line3 = file_read.readline()
    line4 = file_read.readline()
    line5 = file_read.readline()

    line = line.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    line5 = line5.rstrip()


    file_read.close()

    print(line)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

main()