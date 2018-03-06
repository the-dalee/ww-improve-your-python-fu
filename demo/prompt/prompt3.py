from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

history = InMemoryHistory()

if __name__ == '__main__':
    while True:
        name = prompt("What's yout name?: ", history=history)
        print('Hello {}. Nice to meet you!'.format(name))
