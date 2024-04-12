def is_palindrome_letters_only(s):
    b = 0
    e = len(s) -1 

    while b < e:
        if not s[b].isalpha():
            b+=1
        if not s[e].isalpha():
            e-=1
        if s[b].isalpha() and s[e].isalpha():
            if s[b].lower() == s[e].lower():
                b+=1
                e-=1
            else:
                return False
        
    return True

if __name__ == "__main__":
  sample = 'A man, a plan, a canal. Panama!'
  is_palindrome_letters_only(sample)
