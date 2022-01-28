Words = input ('Enter a list of items : ')
# list = []
list =  Words.split()
print(list)
longest = len(Words[0])
#list = len(Words)
for i in list:
  longer =len(i)
  if longer > longest:
      longer= longest
      word=i
print(word)