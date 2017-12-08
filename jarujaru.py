# -*- coding: utf-8 -*-
import re
import jaconv


TSUKKOMI_DICT = {
  u'ﾋﾟﾝﾎﾟﾝﾊﾟﾝﾎﾟﾝﾋﾟﾝ': u'一個多いな',
  u'ﾋﾟﾝ': u'背筋伸びてるやん',
  u'ﾋﾟﾝﾎﾟﾝﾊﾟﾝ': u'一個少ないな',
  u'ﾋﾟﾝﾎﾟﾝ': u'誰か来ましたよ－',
  u'ﾎﾟﾝﾋﾟﾝ': u'来ましたよ－誰か',
}

Rice = [u'米', 'ライス']

PIN_COUNT = 0

def main():
  print('''今から変な校内放送やるから盛り上げてくれへん？
(Press Ctrl-C to exit.)''')
  boke = raw_input('> ')
  while True:
    tsukkomi = goto(boke)
    print(tsukkomi)
    boke = raw_input('> ')


def goto(boke):
  s = boke.decode('utf-8')
  if s == u'やったら絶対できる子やねん':
    return u'よしよしすな'
  s = jaconv.hira2kata(s)
  ends_with_rice, s = rice(s)
  noise = len(filter(lambda x: not x in [u'ピ', u'ン', u'ポ', u'パ', u'ー'], list(s)))
  if noise:
    return '変な校内放送やってや'
  s = filter(lambda x: x in [u'ピ', u'ン', u'ポ', u'パ'], list(s))
  s = jaconv.z2h(''.join(s))
  return evaluate(s, ends_with_rice=ends_with_rice)


def evaluate(s, ends_with_rice=False):
  global PIN_COUNT
  if ends_with_rice and s == u'ﾋﾟﾝﾎﾟﾝﾊﾟﾝ':
    return u'いや、ファミレス行ってピンポン押して店員さん呼んでハンバーグ定食頼んだらパンorライスって聞かれてるやん'
  if s == u'ﾋﾟﾝ':
    PIN_COUNT += 1
  else:
    PIN_COUNT = 0
  if PIN_COUNT == 5:
    PIN_COUNT = 0
    return u'背筋のびきってるやん'
  return TSUKKOMI_DICT[s]


def rice(s):
  s = jaconv.z2h(s)
  for r in [u'ﾗｲｽ', u'米']:
    if s.endswith(r):
      return True, jaconv.h2z(s.rstrip(r))
  return False, jaconv.h2z(s)

if __name__ == '__main__':
  main()