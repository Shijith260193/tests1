import csv
def convert_csv():
    file_name=input('I/p txt file with the extension')
    with open(file_name,'r') as f:
        for lines in f:
            line=0
            if 'MEASURE' in lines:
                print ('found')
                next(f)
                with open('output.csv','wb') as csvfile:
                    writer=csv.writer(csvfile)



if __name__=='__main__':
    convert_csv()

