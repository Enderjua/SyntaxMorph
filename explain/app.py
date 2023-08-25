import openai

openai.api_key = "sk-"

from morph.columDetect import columDetect
from morph.languageDetect import languageDetect
from morph.formatCode import formatDeteced

code = input("Write your code: \n")
language = input("Write translate language: \n")

def translateing(code, language, on):
  colum = columDetect(code)
  lang = languageDetect(code)
  translateCode = formatDeteced(lang, code, 1, language, colum)
  return translateCode

print(translateing(code, language, 1))