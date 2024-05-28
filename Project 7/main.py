with open('Project 7/story.txt','r')as  f:
    story = f.read()

start = -1
words = set()

for i,e in enumerate(story):
    if e == '<':
        start = i
    if e == '>' and start != -1:
        word = story[start : i+1]
        words.add(word)
answers =  {}

for i in words:
    ans =  input(f'which word will replace {i} :')
    answers[i] =ans

for key,value in answers.items():
    story = story.replace(key,value)
print('\033[2J\033[H', end='')
print(story)