from morph import translate
import time
from black import FileMode, format_str

ChatSoftware = translate.ChatSoftware

lang1 = "C"
lang2 = "Python"
code = """int+main()+{++printf('Marijua');++}"""
on = 0

if lang1 != 'CHANGE_LANG1':
    function = ChatSoftware.translateFunction(lang1, lang2, code, on=1)
    def format_code(code: str) -> str:
        mode = FileMode()
        formatted_code = format_str(code, mode=mode)
        return formatted_code
    functions = format_code(function)



variables = ChatSoftware.translateVaribles(lang1, lang2, code, on)
classes = ChatSoftware.translateClasses(lang1, lang2, code, on)
conditions = ChatSoftware.translateConditions(lang1, lang2, code, on)
loops = ChatSoftware.translateLoops(lang1, lang2, code, on)
operators = ChatSoftware.translateOperators(lang1, lang2, code, on)
modules = ChatSoftware.translateModules(lang1, lang2, code, on)
exceptions = ChatSoftware.translateExceptions(lang1, lang2, code, on)
expressions = ChatSoftware.translateExpressionsandAssignments(lang1, lang2, code, on)