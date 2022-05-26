import random
jumper = ['''
    _____
   /____ \
   \     /
    \   /
      O  
     /|\ 
     / \ ''', '''
    _____
   /_____\
   \     /
    \   /
      O  
     /|\ 
     / \ ''', '''
    
    _____\
   \     /
    \   /
      O
     /|\ 
     / \ ''', '''
    
   
   \     /
    \   /
      O  
     /|\ 
     / \ ''', '''
    
         /
    \   /
      O  
     /|\ 
     / \  ''', '''
    
    \   /
      O  
     /|\ 
     / \ ''', '''
    
      x  
     /|\ 
     / \
''']
words = 'valoracion aprenderpython comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()
 
def randomwordAleat(wordlist):
    aleatoriword = random.randint(0, len(wordlist) - 1)
    return wordlist[aleatoriword]
 
def displayBoard(jumper, incorrectword, correctword, secretword):
    print(jumper[len(incorrectword)])
    print ("")
    end = " "
    print ('lyrics incorrect:', end)
    for lyrics in incorrectword:
        print (lyrics, end)
    print ("")
    space = '_' * len(secretword)
    for i in range(len(secretword)): 
        if secretword[i] in correctword:
            space = space[:i] + secretword[i] + space[i+1:]
    for lyrics in space: 
        print (lyrics, end)
    print ("")
 
def chooselyrics(somelyrics):
    while True:
        print ('guess a letter:')
        lyrics = input()
        lyrics = lyrics.lower()
        if len(lyrics) != 1:
            print ('Enter a single letter.') 
        elif lyrics in somelyrics:
            print ('You have already chosen that letter. How about you try another one?')
        elif lyrics not in 'abcdefghijklmnopqrstuvwxyz':
            print ('choose a letter.')
        else:
            return lyrics
 
def start():
    print ('you want to play again? (yes or no)')
    return input().lower().startswith('s')
 
print ('jumper')
incorrectword = ""
correctword = ""
secretword = randomwordAleat(words)
endgame = False
while True:
    displayBoard(jumper, incorrectword, correctword, secretword)
    letra = chooselyrics(incorrectword + correctword)
    if letra in secretword:
       correctword = correctword + letra
        lyricsFound = True
        for i in range(len(secretword)):
            if secretword[i] not in correctword:
                lyricsFound = False
                break
        if lyricsFound:
            print ('Very well! the secret word is "' + secretword + '"! ¡You won!')
            endgame = True
    else:
        incorrectword = incorrectword + lyrics
        if len(incorrectword) == len(jumper) - 1:
            displayBoard(jumper, incorrectword, correctword, secretword)
            print ('¡has run out of letters!\nAfter' + str(len(incorrectword)) + ' wrong letters y ' + str(len(correctword)) + 'correct letters, the word was "' + secretword + '"')
            endgame = True
    if endgame:
        if start():
            incorrectword = ""
            correctword = ""
            endgame = False
            secretword = randomwordAleat(words)
        else:
            break