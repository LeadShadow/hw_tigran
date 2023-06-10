from handlers import *

COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact, 'phone': show_phone,
            'show all': show_all, 'exit': goodbye, 'close': goodbye, 'stop': goodbye, '.': goodbye,
            'help': help_me, '?': help_me}


# add Sasha +380937316048
# (Sasha, +380937316048)
def main():
    contacts = {}
    while True:
        user_command = input('Enter command: ')
        for key in COMMANDS:
            if user_command.lower().startswith(key):
                args = user_command[len(key):].split()
                result = COMMANDS.get(key)(contacts, *args)
                if result is None:
                    print('Good bye!')
                    exit(0)
                print(result, '\n')
                break
        else:
            print('Unknown command!')


if __name__ == "__main__":
    main()


