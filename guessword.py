# -*- coding: utf-8 -*-
# Программа для угадывания слов.
# Игрок вводит букву. Если она есть, то открывается в слове.
# Действие повторяется пока не будут открыты все буквы

import random
import prettyprint

WORDS = ['балерина', 'программа', 'импульс']

print('Добро пожаловать в игру "УГАДАЙ СЛОВО"')
print('Это первая версия и она совсем простая. На экране вы видите закрытое слово.')
print('Вам предлагается вводя буквы попробовать угадать слово. Ограничений по времени и количеству попыток нет.')
print('Для выхода из игры введите 0 (ноль).')
print('-'*64)
print('\n Приступим!')

word = random.choice(WORDS)
vword = 'X'*len(word)
worduser = ['' for x in range(len(word))]

board = prettyprint.Prettyprint()
board.ppw(vword)
board.updateview = False  # признак необходимости вывода на экран слова в рамке

useletter = []  # список букв введённых пользователем

while ''.join(worduser) != word:
  char = ''
  while not char:
    char = input('Введите букву: ').lower()
    if len(char) > 1:
      print('Многовато символов, нужна только ОДНА буква!')
      print('Попробуйте ещё раз.')
      char = ''
    elif char in useletter:
      print('Такая буква уже была, попробуйте другую.')
      char = ''
    else:
      useletter.append(char)

  if char == '0': break
  if char in word:
    print('Есть такая буква!\n')
    for num, ch in enumerate(word):
      if ch == char:
        vword = vword[:num] + ch + vword[num+1:]
        worduser[num] = ch
        board.updateview = True
  else:
    print('Такой буквы нет.')

  if board.updateview:
    board.ppw(vword)
    board.updateview = False

if ''.join(worduser) == word:
  print('ПОЗДРАВЛЯЮ!')
  print('Слово ({}) угадано верно.'.format(word.upper()))
input('Для выхода нажмите Enter...')