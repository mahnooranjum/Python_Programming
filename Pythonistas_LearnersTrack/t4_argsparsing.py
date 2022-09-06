import argparse
import traceback


def do_something(path, type):

    return {"message": "done"}



import argparse

def get_arg(parser, flag, name, text):
    parser.add_argument("-" + flag, "--" + name, dest=name, help=text)
    return parser


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = get_arg(parser, 'p', 'path', 'file path')
    parser = get_arg(parser, 't', 'type', 'can be x y z')
    
    value = parser.parse_args()
    print(value.path)
    print(value.dir)


    body = value 
    
    try:
        path = body.path
        typea = body.type
        print(path)
        print(typea)
        temp =  do_something(path, typea)
        
        print(temp)
    except Exception:
        
        printer = traceback.format_exc()
        print(printer)
        
        print({"message": printer })