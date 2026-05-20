import os
os.system("cls")
from translate import Translator

tarjimon = Translator(to_lang='en', from_lang='ru')

text = input(">>> ")
res = tarjimon.translate(text)
print(res)