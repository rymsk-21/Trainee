# 制御構造の条件分岐（If文）について
def bmax(a,b):
  if a > b:
    return a
  else:
    return b

# x < y xはyより小さい
# x <= y xはy以下
# x > y xはyより大きい
# x >= y xはy以上
# x == y xとyは等しい
# ! = y xとyは等しくない
# 以下、以上のxはyに含まれる 

# 真理値とはTrue/Falseのどちらかの値のことです。組み込み定数である。
# ・True 正しいこと【真】
# ・False 間違ったこと【偽】
#  def is_even(x):
#   return x%2 == 0

# def is_odd(x):
#   if is_even(x):
#     return False
#   else:
#     return True

print(None)

if 0:
  print('ok')
else:
  print('ng')

if -1.1:
  print('ok')
else:
  print('ng')

# 4.8再帰
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)

# 5.1 文法エラー：syntax Errors
# ・クォーテーション忘れ
# ・コロンのつけ忘れ
# ・＝と＝＝の混同
# ・インデントの誤り
# ・全角の空白

# print("aaaa)
#   File "20211207.py", line 53
#     print("aaaa)
#                ^
# SyntaxError: EOL while scanning string literal