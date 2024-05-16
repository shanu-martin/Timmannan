from difflib import SequenceMatcher as chk
print('\033[2J\033[H', end='')
player_score = 0

def evaluvator(ans, key):
    global player_score
    score = chk(None, ans.lower(), key.lower()).ratio()
    min_score = 0.6
    if score == 1:
        player_score += 1
        return '\033[92mCorrect\033[0m'
    elif score >= min_score:
        player_score += 0.5
        return '\033[96mAlmost Correct\033[0m'
    else:
        return '\033[91mWrong\033[0m'

question={
    "What is the capital of France? ": "Paris",
    "What is 5 + 7? ": "12",
    "Who wrote 'To Kill a Mockingbird'? ": "Harper Lee",
    "What is the square root of 64? ": "8",
    "What is the chemical symbol for water? ": "H2O",
    "In which year did the Titanic sink? ": "1912",
    "Who painted the Mona Lisa? ": "Leonardo da Vinci",
    "What is the largest planet in our solar system? ": "Jupiter",
    "What is the freezing point of water in degrees Celsius? ": "0",
    "What is the tallest mountain in the world? ": "Mount Everest"
}
for i , (key,value) in enumerate(question.items()):
    x=input(f'Q{i+1}.{key} ' )
    res=evaluvator(x,value)
    print('\033[1A', end='\t\t\t\t\t\t\t\t\t\t\t\t')
    print(res)

print(f'your score : {player_score}')


