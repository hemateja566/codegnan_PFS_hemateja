'''
7.?
---
"this meta character will form  a searching pattern as it  will take any zero or any one character(?)

import re
any= "This meta character will form  a searching pattern as it  will take any one or more character(?)"
an=re.findall("Th.?",any)
nt=re.search("Th.?",any)
print(an)
print(nt)

8.{}
----
-->this meta character will form  a searching pattern as we mention the size in the {}
syntax-->re.search(".{size},variable")



import re
any= "This meta character will form  a searching pattern as it  will take any one or more character(?)"
pn=re.findall("Th.{20}",any)
sk=re.findall("{20}.",any)
mn=re.findall("{20}",any)
rn=re.search("Th.{20}",any)
print(pn)
print(sk)
print(mn)
print(rn)


9.|
---
-->This meta character will form  a searching pattern as it consider right or left any string is present or not for(|) 

import re
any="This meta character will form"
an=re.findall("that|will",any)
print(an)

10.Special sequence
A special sequence is a \ followed by one of the characters in the list below, and has a
special meaning:

\A
---
Returna a match if the specified characters are at the beginning of the string
eg: "\AThe" 
import re
txt ="The rain in spain "
#check if the string starts with "The":
x=re.findall("\AThe",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")


\b- Returns a match where the specified characters are at the beginning or end of the word
eg: r"\bain"

import re
txt ="The rain in spain "
#check if is present at the beginning of a word:
x=re.findall(r"\bSpain",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")

\d- Returns a match where the string contains digits(numbers from 0-9)
eg:"\d"

import re
txt ="The rain in 56 spain "
#check if the string contains any digit(numbers from 0-9):
x=re.findall("\d",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")

\s- Returns a match where the string Does not contains a white space character:
eg:"\s"

import re
txt ="The rain in spain "
#Return  a match at every white space character:
x=re.findall("\S",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")
\s- Returns a match where the string  contains a white space character:
eg:"\s"

import re
txt ="The rain in spain "
#Return  a match at every white space character:
x=re.findall("\s",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")

Time and date
-------------
%d--> Day
%m--> Month
%Y--> Year
%H--> Hour
%M--> Min
%S--> Sec
%P--> AM/PM
%A--> Day name
%B--> Month name

import datetime
now = datetime.datetime.now()
print(now)
'''
import datetime
today = datetime.date.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))



















