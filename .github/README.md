# Coffee Reading

A command-line parser for Wii U OTP/SEEPROMs. 

Coffee Reading is a tool that can be run through Command Prompt or Terminal to parse Wii U [OTP (one-time programmable)](https://wiiubrew.org/wiki/Hardware/OTP) or [SEEPROM (serial electrically erasable programmable read only memory)](https://wiiubrew.org/wiki/Hardware/SEEPROM) files and present them in an easily-readable format. Please do not share any values obtained from this program! Many are illegal to share due to copyright law and/or unique to your own console!

## Installation
A Windows executable will be bundled with each release. Linux users will need to use the Python script in the source code in order to run the program.

## Usage
A Wii U OTP or SEEPROM file is most commonly obtained when following our [hacking guide](https://wiiu.hacks.guide/), with the help of [wiiu-nanddumper](https://github.com/wiiu-env/wiiu-nanddumper-payload/).
* Call the executable file and provide the path to your dumped one-time programmable. By default, only unique values are shown in the program. In order to read the entire file, pass `--unknown` (or `-u`) as an argument.
* The ability to save a report of obtained values is also available. Provide `--save` (or `-s`) as an argument to the program to do so. A text file named with a timestamp will be generated in the same directory as the tool. This can be used to refer to certain values without having to run the program again in the future.

Example inputs may include:
* `Coffee-Reading.exe -s -u otp.bin`
* `./Coffee-Reading -s -u otp.bin`