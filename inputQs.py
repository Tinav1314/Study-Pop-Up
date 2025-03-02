# read questions from text file 
f = open('Questions.txt', 'r')
questionFile = f.readlines()
f.close()

# read answers from text file
f = open('Answers.txt', 'r')
answerFile = f.readlines()
f.close()
"""

# rewrite the pre existing data + more
f = open('Questions.txt', 'w')
for x in questionFile:
    f.write("\n" + x)
"""
# use \n question but pop out line 1 after for no empty spaces or built function to remove 

def removeEmptySpace():
    """
    f = open('Questions.txt', 'r')
    questionFile = f.readlines()
    f.close()
    """
    f = open('Questions.txt', 'w')
    for x in questionFile:
        if not (x == "\n"):
                f.write(x)
    f.close()

def getIndex():   
    c = 0
    for x in questionFile:
        c += 1
    return c

def write():
    f = open('Questions.txt', 'w')
    for x in questionFile:
        f.write("\n" + x)
        
#write()
#removeEmptySpace()