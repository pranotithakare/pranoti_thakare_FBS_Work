###2. Write a program to input any alphabet and check whether it is vowel or consonant.
ch = input("Enter a alphabet:")
if(ch.isalpha()):
  if(ch in 'aeiouAEIOU'):
    print(f'{ch} is vowel.')
  else:
    print(f'{ch} is consonant.')
else:
    print(f'{ch} it not alphabet.')