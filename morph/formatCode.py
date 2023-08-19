from morph.main import ChatSoftware

def formatDeteced(lang, code, on, language2, colm):
    if colm == 'Fonksiyon' or 'fonksiyon' or 'Function' or 'Functions' or 'Fonksiyonlar' or 'fonksiyonlar':
        formatted_code = ChatSoftware.translateFunction(lang, language2, code, on)
        colm = "Function"
    elif colm == 'Değişkenler' or 'değişkenler' or 'değişken' or 'Değişken' or 'Variables' or 'varibales':
        formatted_code = ChatSoftware.translateVaribles(lang, language2, code, on)
        colm = "Variables"
    elif colm == 'Sınıflar' or 'sınıflar' or 'sınıf' or 'Sınıf' or 'Classes' or 'class':
        formatted_code = ChatSoftware.translateClasses(lang, language2, code, on)
        colm = "Classes"
    elif colm == 'Koşullar' or 'koşullar' or 'koşul' or 'Koşul' or 'Conditions' or 'conditions':
        formatted_code = ChatSoftware.translateConditions(lang, language2, code, on)
        colm = "Conditions"
    elif colm == 'Koşullu ifadeler' or 'koşullu ifadeler' or 'koşul' or 'Koşul' or 'Expressions and Assignments' or 'Expressions':
        formatted_code = ChatSoftware.translateExpressionsandAssignments(lang, language2, code, on)
        colm = "Expressions and Assignments"
    elif colm == 'Modül' or 'modül' or 'Modüller' or 'modüller' or 'modules' or 'Modules':
        formatted_code = ChatSoftware.translateModules(lang, language2, code, on)
        colm = "Modules"
    elif colm == 'Döngüler' or 'döngü' or 'döngüler' or 'Döngüler' or 'Loops' or 'loops':
        formatted_code = ChatSoftware.translateLoops(lang, language2, code, on) 
        colm = "Loops"
    elif colm == 'Operatörler' or 'operatörler' or 'operatör' or 'Operatör' or 'Operators' or 'operators':
        formatted_code = ChatSoftware.translateOperators(lang, language2, code, on) 
        colm = "Operators"
    else:
        formatted_code = ChatSoftware.translateExceptions(lang, language2, code, on)
        colm = "General"
    return formatted_code