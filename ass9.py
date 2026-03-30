str1=input("enter the string:")
vowel=0
conso=0
spaces=0
for i in str1:
    if i in "aeiouAEIOU":
        vowel=vowel+1
    elif i in " ":
        spaces=spaces+1
    else:
        conso=conso+1
print(f"vowel count is {vowel}")
print(f"consonent count is {conso}")
print(f"number of spaces:{spaces}")
