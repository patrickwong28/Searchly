from search.interface import run_interface
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) != 1:
            raise IndexError
        run_interface()
    except FileNotFoundError:
        print('File not found!')
    except IndexError:
        print('Invalid amount of arguments!')