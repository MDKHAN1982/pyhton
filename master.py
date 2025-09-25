import os 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../') 
current_path()

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 8))

# comment to check from vscode to git 