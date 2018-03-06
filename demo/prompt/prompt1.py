from prompt_toolkit import prompt

if __name__ == '__main__':
    name = prompt("What's yout name?: ")
    password = prompt("What's yout password?: ", is_password=True)
    print('Hello {}. Your password is {}. Nice to meet you!'.format(name, password))
