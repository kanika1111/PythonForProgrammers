print("------ Question 1 ------")
class Quadratic(object):
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"{self.a:}x^2{self.b:+}x{self.c:+}"
    def __add__(self,other):
        return(Quadratic(self.a + other.a , self.b + other.b  , self.c + other.c )) 
    
    def __sub__(self,other):
        return( Quadratic(self.a - other.a , self.b - other.b  , self.c - other.c )) 
    def __eq__(self, other):

        return (self.a == other.a) and (self.b == other.b) and (self.c == other.c)
q1 =Quadratic(3,8,-5)
q2 = Quadratic(2,3,7)
quadsum=q1+q2
quaddiff=q1-q2
print("The sum is",quadsum)
print("The difference is",quaddiff)
print("Is q1==q2?",q1==q2)
print("Is q1==q1?",q1==q1)
print("------ Question 2 ------")
import re
import csv
class WordCounter (object):
    def __init__(self,filename) :
        self.file=''
        self.countdict = {} 
        with open(filename,"r") as fileinput:
            for word in fileinput:
                self.file += word.lower()
    def removepunctuation(self):
        result =''
        for word in self.file.split():
            regex = r'[^\w\s]'
            result = result + " " + (re.sub(regex, "", word, 0))
        self.file =result
    def  findcount(self):
        for word in self.file.split():
            if word not in self.countdict:
                self.countdict[word] = 1
            else:
                self.countdict[word] += 1
    def writecountfile(self,csvfilename):
        myFile = open(csvfilename, 'w')
        with myFile:
            writer = csv.writer(myFile)
            for k,v in self.countdict.items():
                writer.writerow([k,v])
        print("Content stored in the file",csvfilename)
        print("5 most popular words are:",sorted(self.countdict.items(),key=lambda a:a[1],reverse=True)[:5])
k = WordCounter("red-headed-league.txt")
k.removepunctuation()
k.findcount()
k.writecountfile("kanika_output_q2.csv")