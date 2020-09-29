#!/usr/bin/env python3
output4 = open("file4.txt","w")
with open("file3.txt","r") as f:
    for line in f:
        lines = line.split(" ")
        numOrfs = int(lines[0])
        #print(numOrfs)
        if numOrfs == 3:
            prob =str(float((3/5800)*(3/5800)))
            string = str("probability for 3 ORFs is "+prob+"\n")
            output4.write(string)
        elif numOrfs == 4:
            prob = str(float((4/5800)*(4/5800)*(4/5800)))
            string = str("probability for 4 ORFs is "+prob+"\n")
            output4.write(string)
output4.close()    
