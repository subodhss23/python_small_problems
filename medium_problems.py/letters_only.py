''' Check if the given string consists of only letters and space and if every
    letter is  in lower case.'''

def letters_only(s):
  if len (s)==0 : return False
  for i in s:
    if i == " " or i.islower():
      continue
    else :
      return False
  return True

print(letters_only("PYTHON"))
print(letters_only("python"))
print(letters_only("12321313"))
print(letters_only("i have spaces"))
print(letters_only("i have numbers(1-10)") )
print(letters_only(""))