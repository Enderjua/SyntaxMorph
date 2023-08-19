SyntaxMorph
========

|Downloads| |Latest Version| |Build Status| |Documentation Status|

.. |Downloads| image:: https://img.shields.io/pypi/dd/syntaxmorph
   :target: https://img.shields.io/pypi/dd/syntaxmorph
.. |Latest Version| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&r=r&type=6e&v=1.0.0&x2=0
   :target: https://pypi.python.org/pypi/syntaxmorph

SyntaxMorph is a module that aims to facilitate the conversion between programming languages by utilizing OpenAI.

-  Free software: GPLv3 license
-  Github: https://github.com/Enderjua/SyntaxMorph



Features
~~~~~~~~

-  Determining which programming language a given code belongs to.
-  Identifying the general structure of the given code.
-  Converting the given code to the desired programming language.
-  Aiming to collect a comprehensive dataset.
-  Eliminating the dependency on OpenAI.

Developer
~~~~~~~~~

-  Marijua @ ``enderjua gmail com``


Quick Tutorial
--------------

.. code:: python

    import openai
   
    openai.api_key = "YOUR_API_KEY"

    from morph import formatCode
    from morph import columDetect
    from morph import languageDetect
    
    
Language Detection
~~~~~~~~~~~~~~~~~~

.. code:: python


    code = """ print('hello world') """
    languageDetection = languageDetect.languageDetect(code)
    print("Language Detected: "+languageDetection) # Python


.. parsed-literal::

    Language Detected: Python
    


Colum Detection
~~~~~~~~~~~~

.. code:: python

    code = """ def main(a, b, c):
    
           d = a+b+c
           print(d)

     main(5,7,9)"""
     columDetection = columDetect.columDetect(code)
     print("Colum Detected: "+columDetection) # Function && Fonksiyon


.. parsed-literal::

    Colum Detected: Fonksiyon


.. code:: python

    print(columDetect.columDetect(code))


.. parsed-literal::

    Function && Fonksiyon


Language translation
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    code = """ print('hello world') """
    
    newCode = formatCode.formatDetected(languageDetection, code, 1, C++, columDetection)
    print(newCode)
    
    


.. parsed-literal::

    #include <iostream>

    int main() {
        std::cout << "Hello World!" << std::endl;
        return 0;
    }


Create a function for Flask API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main.py:

.. code:: python

    import openai
    openai.api_key = "YOUR_API_KEY"
    
    from morph import formatCode as f
    from morph import languageDetect as l
    from morph import columDetect as c
    
    def morphApi(code, lang):
       language = l.languageDetect(code)
       colum = c.columDetect(code)
       newCode = f.formatDetected(language, code, 1, lang, colum)
       return newCode
       
    # code = morphApi("print('hello')", "C++")
    # print(code)


.. parsed-literal::

    #include <iostream>

    int main() {
        std::cout << "Hello World!" << std::endl;
        return 0;
    }


Create a Flask API
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from flask import Flask, jsonify
    from flask_cors import CORS
    from urllib.parse import unqoute
    
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/translateAPI/<string:language>/<path:code>', methods=['GET'])
    def translating(language2, code):
      from main import morphApi
      code = morphApi(code, language2)
      return code
      
    if __name__ = '__main__':
        app.run(debug=True)
    


.. parsed-literal::

    localhost:5000/translateAPI/C++/print('hello world')
    
    #include <iostream>

    int main() {
        std::cout << "Hello World!" << std::endl;
        return 0;
    }
    

Future
~~~~~~~~

-  We have set out on the process of training our own AI.
-  We will share our AI for free here as a result of the AI training.
-  We will ensure the independence of OpenAI.


