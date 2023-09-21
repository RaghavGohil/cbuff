import os
import sys
import platform
import json
import subprocess
import pathlib

CMD_BUFFER_FOLDER_PATH = str(pathlib.Path.home() / "Downloads")
CMD_BUFFER_FILE_NAME = 'CMD_BUFFER'
BUFFER_PATH = CMD_BUFFER_FOLDER_PATH+'//'+CMD_BUFFER_FILE_NAME+".txt"

SUPPORTED_PLATFORMS = ['Windows','Linux']

COMMANDS= ['push','view','remove','open','reset','help','p','v','r','re','o','h']


def exit_r(reason: str)->None:
    print(reason)
    sys.exit()

def check_platform()->None:
    supported = False
    for p in SUPPORTED_PLATFORMS:
        if p == platform.system():
            supported = True
    if not supported:
        exit_r('Your platform is not supported. \nSupported platforms are: \n' + str(SUPPORTED_PLATFORMS))

def exec_op()->None:
    # if platform is supported, set the data in buffer
    set_buffer()
    try:
        if sys.argv[1] == 'push' or sys.argv[1] == 'p':
            push_command(sys.argv[3],sys.argv[2]) # push the description, alias and command in order
        elif sys.argv[1] == 'view' or sys.argv[1] == 'v':
            view_commands()

        elif sys.argv[1] == 'open' or sys.argv[1] == 'o':
            open_buffer()
        
        elif sys.argv[1] == 'reset' or sys.argv[1] == 're':
            reset_buffer()

        elif sys.argv[1] == 'remove' or sys.argv[1] == 'e':
            remove_command(sys.argv[2])

        elif sys.argv[1] == 'help' or sys.argv[1] == 'h':
            print(
                '''
    This program will help users to create a cmd prompt command dictionary.
    
    The default storage dir is downloads.
    The users will be able to:
    - push one command                                          -> cbuff push | p <command> <alias>
    - push multiple commands                                    -> cbuff push | p "<command1>&&<command2>" <alias>
    - push a path when alias is prefixed by @ (open terminal)   -> cbuff push | p <path> @<alias>
    - view the commands with their unique alias key             -> cbuff view | v
    - run pushed commands with that alias key                   -> cbuff <alias>
    - pass params when you run alias (command must contain {})  -> cbuff <alias> <param1> <param2> ...
    - remove the pushed commands with the key                   -> cbuff remove | r <alias>
    - open the buffer in notepad/vim for quick edit             -> cbuff open | o
    - reset the system                                          -> cbuff reset | re
    - get help for cbuff                                        -> cbuff help | h

    * You can provide an alias for cbuff altogether. Instead of typing cbuff you can define something like 'cb' in your terminal.
    * You can use "" while making an alias for storing commands having spaces.
    * You can execute cbuff commands inside cbuff.
    * You can combine cbuff commands like cbuff p "cbuff reset&&cbuff open" quick-edit
      and run it like : cbuff quick-edit or cb quick-edit if defined as stated earlier.
                ''')
        elif sys.argv[1] not in COMMANDS: # if input is an alias
            param_list=sys.argv[2:]
            execute_command(sys.argv[1],param_list)
    except Exception as e:
        print("Invalid use of cbuff. Use cbuff help for more information.")
        #print("\n",e)

def set_buffer()->None:
    with open(BUFFER_PATH , 'a'):
        pass

def execute_command(alias:str,params:list=[])->None:
    json_data = {}
    with open(BUFFER_PATH , 'r') as buffer:
        json_data = json.loads(get_data(buffer.read()))
        keys = json_data.keys()
        if alias in keys:
            if alias[0] == '@': # is a path alias
                if sys.platform.startswith('win'):
                    # On Windows, use the "start" command to open a new command prompt window
                    subprocess.Popen(['cmd', '/K', f'cd /D {json_data[alias].format(*params)}'],shell=True,creationflags=subprocess.DETACHED_PROCESS)

                elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                    # On Linux and macOS, use the terminal emulator to open a new terminal window
                    terminal = os.getenv('TERMINAL', 'x-terminal-emulator')  # Use 'x-terminal-emulator' as the default
                    subprocess.Popen([terminal, '--working-directory', json_data[alias].format(*params)],shell=True,creationflags=subprocess.DETACHED_PROCESS)
            else:
                os.system(json_data[alias].format(*params))
        else:
            exit_r('Alias not found. Define an alias using cbuff push.')

def push_command(alias:str,path:str)->None:
    json_data = {}
    if alias in COMMANDS:
        exit_r('Alias can\'t be a command.')
    with open(BUFFER_PATH , 'r') as buffer:
        json_data = json.loads(get_data(buffer.read()))
        json_data[alias] = path
    with open(BUFFER_PATH , 'w') as buffer:
        buffer.writelines(json.dumps(json_data)+"\n")

def open_buffer():
    if sys.platform.startswith('win'):
        subprocess.run("notepad "+BUFFER_PATH)
    else:
        subprocess.run("vim "+BUFFER_PATH)

def reset_buffer():
    with open(BUFFER_PATH , 'w'):
        pass

def remove_command(alias:str)->None:
    json_data = {}
    with open(BUFFER_PATH , 'r') as buffer:
        json_data = json.loads(get_data(buffer.read()))
        json_data.pop(alias,'Cannot remove undefined alias.')
    with open(BUFFER_PATH , 'w') as buffer:
        buffer.writelines(json.dumps(json_data))

def view_commands()->None:
    with open(BUFFER_PATH , 'r') as buffer:
        json_data = json.loads(get_data(buffer.read()))
        for data in json_data:
            print(data,'->',json_data[data])

def get_data(data:str)->str: #get the correct json
    if data == '':
        return '{}'
    else:
        return data

def main():

    check_platform()
    exec_op()
