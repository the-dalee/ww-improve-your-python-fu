from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter

name_completer = WordCompleter([
        'Emma', 'Noah', 'Ava', 'William', 'Sophia', 'Mason',
        'Isabella', 'James', 'Mia', 'Benjamin', 'Charlotte', 
        'Jacob', 'Abigail', 'Michael', 'Emily', 'Elijah',
        'Harper', 'Ethan'])

if __name__ == '__main__':
    name = prompt("What's yout name?: ", completer=name_completer)
    print('Hello {}. Nice to meet you!'.format(name))
