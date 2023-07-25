"""
Module to translate between English and French
using MyMemoryTranslator from deep_translator package
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    English-French translation function
    input = English string
    output = French string
    """
    #create an instance of the translator and use it to translate
    #the input text to French

    e_to_f = MyMemoryTranslator(source='english', target='french')
    french_text = e_to_f.translate(english_text)

    return french_text

def french_to_english(french_text):
    """
    French-English translation function
    input = French string
    output = English string
    """
    #create an instance of the translator and use it to translate
    #the input text to English

    f_to_e = MyMemoryTranslator(source='french', target='english')

    english_text = f_to_e.translate(french_text)

    return english_text
