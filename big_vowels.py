#method for making the vowels upper case
print("Making the vowels to upper")
def vowelsToUpper(string):

    vowels = "aeiou"

    modified = ''.join([char.upper() if char.lower() in vowels  else char for char in string])

    return modified
#for displaying the result
print( '" "==" "')
print('"Hello world" == ',vowelsToUpper('"Hello world"'))
print('"hello hi bye" == ',vowelsToUpper('"hello hi bye"'))