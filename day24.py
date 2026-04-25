'''
File handling
-------------
-->File handler is an object oriented file to maintain several functions of file such as creating, reading, writing and update also deleting the file.

How to open a file
------------------
1.open()
--------
-->This open() takes 2 parameters and in this we have to close the file by calling close() function after program
1.file name
2.mode


2.with open()
-------------

Modes("r","w","a","x","t")
---------------------------
1."r"-->read
-->to read the file we will use this mode and if the file doesn't exist. it will through the error
any=open("teja.txt","r")
print(any.read())
any.close()


2."w"-->write
-->to write the text into the file this is used and it will create the file if it doesn't exist
any=open("teja.txt","w")
print(any.write())
any.close()


3."a"-->append
-->to add the text into the file this is used and it will create the file if it doesn't exist
-->it will write text at the end

any=open("teja.txt","a")
print(any.write("this is a line"))
any.close()

4."x"-->create
-->this is used to create the file, but is the is already in the system it through error

To read the file
----------------
1.read()
--------
-->this method can read the entire file chunk by chunk we can also specify the size

syntax:-
------
any=open("teja.txt","r")
print(any.read(1000))
any.close

2.readline()
------------
-->this method reads only the first line from the file

syntax:-
--------
any=open("teja.txt","r")
print(any.readline())
any.close()


3.readlines()
-------------
-->This method can read the entire file and return into list with each lline is one index in the list


syntax:-
--------
'''
any=open("teja.txt","r")
print(any.readlines())
any.close()






























