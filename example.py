from googletrans import Translator

translator = Translator()

class Person:
    '''Simple person class to handle languages and translations.'''
    
    def __init__(self, name: str, lang: str):
        self.name = name
        self.lang = lang

    def say(self, text: str, target: 'Person') -> str:
        '''Translates the given text to target's language and retuns the result.'''

        result = translator.translate(text, src=self.lang, dest=target.lang)
        return result.text

def main():
    # Defines person models.
    jane = Person(name='Jane', lang='en')
    juan = Person(name='Juan', lang='es')

    # Some random messages.
    from_jane = 'Hello! My name is Jane.'
    from_juan = '¡Hola! Mi nombre es Juan.'

    # Translate messages.
    to_juan = jane.say(from_jane, target=juan)
    to_jane = juan.say(from_juan, target=jane)

    print(f'''
    Jane's message: {from_jane}
    Translated message: {to_juan}
    ''')

    print(f'''
    Juan's message: {from_juan}
    Translated message: {to_jane}
    ''')

if __name__ == '__main__':
    main()
