#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.



ransomNote = "aa"
magazine = "ab"
mag=list(magazine)
for i in ransomNote:

    if i not in mag:

        print(False)

        break

    else:

        mag.remove(i)
        

else:

    print(True)