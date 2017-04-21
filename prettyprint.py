# -*- coding: utf-8 -*-

class Prettyprint(object):
  def ppw(self, word):
    '''Функиция побуквенно выводит на печать слово'''
    print('+---'*len(word)+'+')
    for char in word:
      print('| {} '.format(char), end='')
    print('|')
    print('+---' * len(word) + '+')

  def ppl(self, container):
    '''Функиция поэлементно выводит на печать список'''
    lenBuf = [len(element) for element in container]
    top = ['+-'+'-'*ln+'-' for ln in lenBuf]
    top.append('+')
    borderStr = ''.join(top)
    print(borderStr)
    for element in container:
      print('| {} '.format(element),end='')
    print('|')
    print(borderStr)

if __name__ == '__main__':
  pp = Prettyprint()
  test = ['1111', '2222', 'ABcDe']
  pp.ppw(test[2])
  pp.ppl(test)
