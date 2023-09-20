![cbuff](https://github.com/RaghavGohil/cbuff/assets/71706645/4343a690-f4b4-402a-a83f-5849803cb642)

![version](https://img.shields.io/badge/version-1.0.0-blue)
![python](https://img.shields.io/badge/lang-python3-green)

# cbuff - Command Buffer

```cbuff``` (short for Command Buffer) is a versatile command-line tool that empowers users to efficiently store, manage, and execute frequently used commands and workflows. With its user-friendly interface, cbuff simplifies command-line tasks, improves productivity, and reduces the risk of errors.

cbuff can store long paths, commands, also multiple commands which can run sequentially.

## Key Features

- **Simplicity and Convenience**: `cbuff` offers a straightforward and convenient way to manage and execute command-line operations, reducing the need to remember complex commands.

- **Productivity Boost**: By streamlining repetitive tasks and simplifying command execution, `cbuff` can enhance productivity in various workflows.

- **Customization**: Users can create aliases for their most-used commands, tailoring `cbuff` to their specific needs and workflows.

- **Multicommand system**: Users can create aliases which can store multiple commands which execute sequentially.

- **Cross-Platform Compatibility**: `cbuff` is designed to work on multiple platforms, ensuring consistency in command execution across different environments.

- **Documentation and Collaboration**: `cbuff` can be used to store and share common commands and snippets, promoting consistency in command usage, especially in collaborative environments.

- **Open Source Community**: If `cbuff` is open-source and actively maintained, it may attract contributions from the open-source community, leading to feature enhancements and issue resolution.

## Installation

Use ```pip install cbuff``` to install cbuffer.

## Usage

How to use cbuff:
    
    The default storage dir is downloads.
    The users will be able to:
    - push one commands                                         -> cbuff push | p <command> <alias>
    - push multiple commands                                    -> cbuff push | p "<command1>::<command2>" <alias>
    - push a path when alias is prefixed by @ (open terminal)   -> cbuff push | p <path> @<alias>
    - view the commands with their unique alias key             -> cbuff view | v
    - run pushed commands with that alias key                   -> cbuff <alias>
    - remove the pushed commands with the key                   -> cbuff remove | r <alias>
    - open the buffer in notepad/vim for quick edit             -> cbuff open | o
    - reset the system                                          -> cbuff reset | re
    - get help                                                  -> cbuff help | h

    Note that you can use "" while making an alias for storing commands having spaces.

## License

`cbuff` uses the MIT License. For more details, look for the license file.

## Contributing

Contributions to `cbuff` are welcome! If you'd like to contribute or report issues, please visit the [cbuff GitHub repository](https://github.com/RaghavGohil/cbuff).
