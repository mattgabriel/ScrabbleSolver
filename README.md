#Scrabble Solver#

This program will do 2 things:

1. Return a number of random letters that can be used to play Scrabble
2. Given a number of letters it will find all the words that can be formed with them


It currenlty uses an English dictionary but can also be extended to any other language



#Usage#

##Python: Get random letters##

`cd Python`

`python main.py` 

This will return:

```
------------------------------------------------
Form the longest possible word with the following letters:
A - I - E - N - Q - N - D - O - G
------------------------------------------------


------------------------------------------------
BEST: 7 letters
SOLUTIONS:
['Deaning', 'Nonage', 'Ginned', 'Ganoid', 'Gained', 'Eonian', 'Ending']
------------------------------------------------
```


##Python: Get solution##

`cd Python`

`python main.py --letters lostpenis` 

This will return

```
BEST: 9 letters
SOLUTIONS:
['Pointless', 'Toplines', 'Potlines', 'Plenists', 'Pistoles', 'Epsilons', 'Topline', 'Topless', 'Tonsils', 'Tipless', 'Tinsels', 'Telsons', 'Stipels', 'Stepson']
```

