"""
File: anagram.py
Name: Chasel Fan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19
If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams


"""
# Constants

FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

lst=[]
count=0
d=[]

def main():
    global lst
    global count
    while True:
        word=input(f'Welcome to stanCode "Anagram Generator"\ngive me a word(or {EXIT} to quit): ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)
            lst = []
            count=0


def read_dictionary():
    global d
    with open(FILE,'r')as f:
        for line in f:
            line=line.strip()
            d.append(line)

def find_anagrams(s):
    """
    :param s:
    :return:
    """

    read_dictionary()
    find_anagrams_helper(s,'')
    print(str(count) + f' anagram{lst}')


def find_anagrams_helper(s,ans):
    global count
    global lst
    if len(ans) == len(s):
        if ans in d:
            print('Searching...')
            lst.append(ans)
            print(ans)
            count+=1
    else:
        if has_prefix(s) is True:
            for i in range(len(s)):
                if s[i] not in ans:
                    ans+=s[i]
                    #if has_prefix(s[i]) is True:
                    find_anagrams_helper(s, ans)
                    ans = ans[:len(ans)-1]


def has_prefix(s):
    global d
    if s in d:
        return True
    else:
        return False

if __name__ == '__main__':
    main()