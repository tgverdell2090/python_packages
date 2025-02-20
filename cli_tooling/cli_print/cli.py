import sys

def cli_function():
    
    args = sys.argv
    
    if len(args) == 1:
        print('Help')
    
    else:
        if args[1] == 'art':
            from cli_print.art import main
        elif args[1] == 'quote':
            from cli_print.art import main
        else:
            raise NotImplementedError
        
        main()