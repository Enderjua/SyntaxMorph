import openai


class ChatSoftware:
    
    @staticmethod
    def translateFunction(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this function from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###"]
        )
        response = response['choices'][0]['text']
        return response
    
    @staticmethod
    def translateVaribles(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Variables from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateClasses(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Classes from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    

    @staticmethod
    def translateConditions(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Conditions from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateLoops(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Loops from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateOperators(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Operators from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
               presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateModules(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Modules from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateExceptions(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Exceptions from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
               presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
    @staticmethod
    def translateExpressionsandAssignments(languageOne, languageTwo, code, on):
        if on == True:
            prompt = f"#### Translate this Expressions and Assignments from {languageOne} into {languageTwo}\n {languageOne} \n {code} \n### {languageTwo}"
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            response = response['choices'][0]['text']
            return response
    
