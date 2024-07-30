# Coffee Reading

A command-line parser for Wii U OTP/SEEPROMs.

<p align="left">
  <a href="https://discord.nightkingale.com/">
    <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join us!" width="10%" height="10%">
  </a>
  <a href="https://donate.nightkingale.com/">
    <img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Thank you!" width="10%" height="10%">
  </a>
  <a href="https://nightkingale.com/">
    <img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white" alt="Visit us!" width="10%" height="10%">
  </a>
</p>

Coffee Reading is a tool that can be run through Command Prompt or Terminal to parse Wii U [OTP (one-time programmable)](https://wiiubrew.org/wiki/Hardware/OTP) or [SEEPROM (serial electrically erasable programmable read only memory)](https://wiiubrew.org/wiki/Hardware/SEEPROM) files and present them in an easily-readable format.

> ⚠️ **Disclaimer:** Please do not share any values obtained from this program, especially values such as common keys! Many are illegal to share due to copyright law and/or unique to your own console, so sharing them can be dangerous and risky.

## Installation
A Windows executable will be bundled with each release. Linux users will need to use the Python script in the source code in order to run the program.

## Usage
A Wii U OTP or SEEPROM file is most commonly obtained when following our [hacking guide](https://wiiu.hacks.guide/), with the help of [wiiu-nanddumper](https://github.com/wiiu-env/wiiu-nanddumper-payload/).
* Call the executable file and provide the path to your dumped one-time programmable. By default, only unique values are shown in the program. In order to read the entire file, pass `--unknown` (or `-u`) as an argument.
* The ability to save a report of obtained values is also available. Provide `--save` (or `-s`) as an argument to the program to do so. A text file named with a timestamp will be generated in the same directory as the tool. This can be used to refer to certain values without having to run the program again in the future.

Example inputs may include:
* `Coffee-Reading.exe -s -u otp.bin`
* `./Coffee-Reading -s -u otp.bin`

## Assistance
If you encounter bugs, the best place to report them would be the [Issues](https://github.com/Nightkingale/Coffee-Reading/issues) tab. This allows for easy tracking and reference, though please check for duplicates first and comment there if possible!

For assistance or other inquiries, the best place to reach out would be the [Nightkingale Studios](https://discord.nightkingale.com/) Discord server ([#chat-hangout](https://discord.com/channels/450846070025748480/1127657272315740260) is okay). I am active in many other Wii U homebrew Discord servers as well.