import construct
import os
import sys
import time

from datetime import datetime
from itertools import islice

# Show the corrosponding usage per platform.
def show_example_usage(platform):
    if platform == "nt":
        print("Usage Example: Coffee_Reading.exe -s -u otp.bin\n")
    else:
        print("Usage Example: ./Coffee_Reading -s -u otp.bin\n")

    print("-s / --save:")
    print("\tOptional argument.")
    print("\tSave values that are output to a text file.")

    print("-u / --unknown:")
    print("\tOptional argument.")
    print("\tShow any unknown, empty, or unused values.\n")

# Check if all arguments are properly provided.
def validate_arguments(arguments, backup_file):
    valid_arguments = ["-s", "-u", "--save", "--unknown"]
    
    if len(arguments) == 1:
        # No argumens were provided.
        show_example_usage(os.name)
        print("There is no provided file! Did you define a path?\n")
        sys.exit()

    try:
        if os.stat(backup_file).st_size not in [512, 1024]:
            # Neither an OTP or an SEEPROM was given to read.
            show_example_usage(os.name)
            print("The file provided isn't correct! Is this a valid backup?\n")
            sys.exit()

    except FileNotFoundError:
        # The file does not exist, so it can't be read.
        show_example_usage(os.name)
        print("The file provided doesn't exist! Did you enter the right path?\n")
        sys.exit()

    if len(arguments) >= 3:
        # It's possible there's more arguments than necessary?
        for flag in arguments[1:len(arguments) - 1]:
            if flag not in valid_arguments or len(arguments) > 4:
                show_example_usage(os.name)
                print("The provided arguments are invalid! Are they correct?\n")
                sys.exit()

# Read any provided backup data.
def read_backup_data(arguments, backup_data):
    unknown_keys = ["Unknown", "Unused", "Empty"]

    for item, value in islice(backup_data.items(), 1, None):
        value = str(value)
        value = value[11:-2].upper()

        if any(flag in arguments for flag in ["-u", "--unknown"]):
            print(f"{item}: {value}")
        else:
            if not any(word in item for word in unknown_keys):
                print(f"{item}: {value}")

# Write the backup data to an easy-to-read text file.
def write_backup_data(arguments, backup_data, text_file):
    with open(text_file, "w") as text_file:
        sys.stdout = text_file
        # Write a header for the file.
        print("Coffee Reading (v1.0.0)")
        print("Created by NoahAbc12345.\n")
        print("Please do not share any values obtained from this program!")
        print("Many are illegal to share due to copyright law and/or unique"
            + " to your own console!")
        if os.stat(backup_file).st_size == 512:
            print("Useful Information: https://wiiubrew.org/wiki/Hardware/SEEPROM\n")
        elif os.stat(backup_file).st_size == 1024:
            print("Useful Information: https://wiiubrew.org/wiki/Hardware/OTP\n")
        print("Generated: " + str(datetime.now()))

        if any(flag in arguments for flag in ["-u", "--unknown"]):
            print("Unknown Mode: True\n")
        else:
            print("Unknown Mode: False\n")
        # Read the backup data to the text file.
        read_backup_data(arguments, backup_data)
        sys.stdout = sys.__stdout__

# A construct for the Wii U OTP.
otp_structure = construct.Struct(
    "Wii boot1 SHA-1 Hash" / construct.Hex(construct.Bytes(20)),
    "Wii Common Key" / construct.Hex(construct.Bytes(16)),
    "Wii NG ID" / construct.Hex(construct.Bytes(4)),
    "Wii NG Private Key" / construct.Hex(construct.Bytes(28)),
    "Wii NAND HMAC" / construct.Hex(construct.Bytes(20)),
    "Wii NAND Key" / construct.Hex(construct.Bytes(16)),
    "Wii RNG Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 1" / construct.Hex(construct.Bytes(8)),
    "Security Level Flag" / construct.Hex(construct.Bytes(4)),
    "IOStrength Configuration Flag" / construct.Hex(construct.Bytes(4)),
    "Pulse Length for SEEPROM Manual CLK" / construct.Hex(construct.Bytes(4)),
    "Possibly a Signature Type" / construct.Hex(construct.Bytes(4)),
    "Wii U Starbuck Ancast Key" / construct.Hex(construct.Bytes(16)),
    "Wii U SEEPROM Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 2" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 3" / construct.Hex(construct.Bytes(16)),
    "vWii Common Key" / construct.Hex(construct.Bytes(16)),
    "Wii U Common Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 4" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 5" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 6" / construct.Hex(construct.Bytes(16)),
    "SSL RSA Encryption Key" / construct.Hex(construct.Bytes(16)),
    "USB Storage Seed Encryption Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 7" / construct.Hex(construct.Bytes(16)),
    "Wii U XOR Key" / construct.Hex(construct.Bytes(16)),
    "Wii U RNG Key" / construct.Hex(construct.Bytes(16)),
    "Wii U SLC Key" / construct.Hex(construct.Bytes(16)),
    "Wii U MLC Key" / construct.Hex(construct.Bytes(16)),
    "SHDD Encryption Key" / construct.Hex(construct.Bytes(16)),
    "DRH WLAN Data Encryption Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 8" / construct.Hex(construct.Bytes(48)),
    "Wii U SLC (NAND) HMAC" / construct.Hex(construct.Bytes(20)),
    "Unknown Space 9" / construct.Hex(construct.Bytes(12)),
    "Unknown Space 10" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 11" / construct.Hex(construct.Bytes(12)),
    "Wii U NG ID" / construct.Hex(construct.Bytes(4)),
    "Wii U NG Private Key" / construct.Hex(construct.Bytes(32)),
    "Wii U NSS Device Certificate Key" / construct.Hex(construct.Bytes(32)),
    "Wii U OTP RNG Seed" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 12" / construct.Hex(construct.Bytes(16)),
    "Wii U Root Certificate MS ID" / construct.Hex(construct.Bytes(4)),
    "Wii U Root Certificate CA ID" / construct.Hex(construct.Bytes(4)),
    "Wii U Root Certificate NG Key ID" / construct.Hex(construct.Bytes(4)),
    "Wii U Root Certificate NG Signature" / construct.Hex(construct.Bytes(60)),
    "Unknown Space 13" / construct.Hex(construct.Bytes(24)),
    "Unknown Space 14" / construct.Hex(construct.Bytes(32)),
    "Wii Root Certificate MS ID" / construct.Hex(construct.Bytes(4)),
    "Wii Root Certificate CA ID" / construct.Hex(construct.Bytes(4)),
    "Wii Root Certificate NG Key ID" / construct.Hex(construct.Bytes(4)),
    "Wii Root Certificate NG Signature" / construct.Hex(construct.Bytes(60)),
    "Wii Korean Key" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 15" / construct.Hex(construct.Bytes(8)),
    "Wii NSS Device Certificate Key" / construct.Hex(construct.Bytes(32)),
    "Unknown Space 16" / construct.Hex(construct.Bytes(32)),
    "Wii U boot1 Key (Locked)" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 17" / construct.Hex(construct.Bytes(16)),
    "Empty Space 1" / construct.Hex(construct.Bytes(32)),
    "Empty Space 2" / construct.Hex(construct.Bytes(4)),
    "OTP Version & Revision" / construct.Hex(construct.Bytes(4)),
    "OTP Date Code" / construct.Hex(construct.Bytes(8)),
    "OTP Version Name String" / construct.Hex(construct.Bytes(8)),
    "Empty Space 3" / construct.Hex(construct.Bytes(4)),
    "JTAG Status" / construct.Hex(construct.Bytes(4))
)

# A construct for the Wii U SEEPROM.
seeprom_structure = construct.Struct(
    "Empty Space 1" / construct.Hex(construct.Bytes(18)),
    "SEEPROM RNG Seed" / construct.Hex(construct.Bytes(8)),
    "Empty Space 2" / construct.Hex(construct.Bytes(6)),
    "PPC PVR" / construct.Hex(construct.Bytes(4)),
    "SEEPROM Version Name String" / construct.Hex(construct.Bytes(6)),
    "SEEPROM Version Code" / construct.Hex(construct.Bytes(2)),
    "OTP Version Code" / construct.Hex(construct.Bytes(2)),
    "OTP Revision Code" / construct.Hex(construct.Bytes(2)),
    "OTP Version Name String" / construct.Hex(construct.Bytes(8)),
    "BC Structure CRC32" / construct.Hex(construct.Bytes(4)),
    "BC Structure Size" / construct.Hex(construct.Bytes(2)),
    "BC library version" / construct.Hex(construct.Bytes(2)),
    "BC author" / construct.Hex(construct.Bytes(2)),
    "BC boardType" / construct.Hex(construct.Bytes(2)),
    "BC boardRevision" / construct.Hex(construct.Bytes(2)),
    "BC bootSource" / construct.Hex(construct.Bytes(2)),
    "BC ddr3Size" / construct.Hex(construct.Bytes(2)),
    "BC ddr3Speed" / construct.Hex(construct.Bytes(2)),
    "BC ppcClockMultiplier" / construct.Hex(construct.Bytes(2)),
    "BC iopClockMultiplier" / construct.Hex(construct.Bytes(2)),
    "BC video1080p" / construct.Hex(construct.Bytes(2)),
    "BC ddr3Vendor" / construct.Hex(construct.Bytes(2)),
    "BC movPassiveReset" / construct.Hex(construct.Bytes(2)),
    "BC sysPllSpeed" / construct.Hex(construct.Bytes(2)),
    "BC sataDevice" / construct.Hex(construct.Bytes(2)),
    "BC consoleType" / construct.Hex(construct.Bytes(2)),
    "BC devicePresense" / construct.Hex(construct.Bytes(4)),
    "Empty Space 3" / construct.Hex(construct.Bytes(32)),
    "Wii U Drive Key" / construct.Hex(construct.Bytes(16)),
    "Wii U Factory Key" / construct.Hex(construct.Bytes(16)),
    "Wii U SHDD Key" / construct.Hex(construct.Bytes(16)),
    "Wii U SHDD Key Seed" / construct.Hex(construct.Bytes(16)),
    "Drive Key's Status Flag" / construct.Hex(construct.Bytes(2)),
    "USB Key Seed's Status Flag" / construct.Hex(construct.Bytes(2)),
    "SHDD Key's Status Flag" / construct.Hex(construct.Bytes(2)),
    "Empty Space 4" / construct.Hex(construct.Bytes(106)),
    "Unknown Space 1" / construct.Hex(construct.Bytes(4)),
    "Unknown Space 2" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 3" / construct.Hex(construct.Bytes(2)),
    "Empty Space 5" / construct.Hex(construct.Bytes(8)),
    "sys_prod.version" / construct.Hex(construct.Bytes(4)),
    "sys_prod.eeprom_version" / construct.Hex(construct.Bytes(4)),
    "sys_prod.product_area" / construct.Hex(construct.Bytes(4)),
    "sys_prod.game_region" / construct.Hex(construct.Bytes(4)),
    "sys_prod.ntsc_pal" / construct.Hex(construct.Bytes(4)),
    "sys_prod.5ghz_country_code" / construct.Hex(construct.Bytes(2)),
    "sys_prod.5ghz_country_code_revision" / construct.Hex(construct.Bytes(2)),
    "sys_prod.code_id" / construct.Hex(construct.Bytes(8)),
    "sys_prod.serial_id" / construct.Hex(construct.Bytes(16)),
    "sys_prod.model_number" / construct.Hex(construct.Bytes(16)),
    "Unknown Space 4" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 5" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 6" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 7" / construct.Hex(construct.Bytes(2)),
    "Production Date (Year)" / construct.Hex(construct.Bytes(2)),
    "Production Date (Month and Day)" / construct.Hex(construct.Bytes(2)),
    "Production Date (Hour and Minute)" / construct.Hex(construct.Bytes(2)),
    "CRC32 of the Last 0x0E Bytes" / construct.Hex(construct.Bytes(4)),
    "0xAA55 Marker" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 8" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 9" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 10" / construct.Hex(construct.Bytes(2)),
    "Empty Space 6" / construct.Hex(construct.Bytes(4)),
    "Unknown Space 11" / construct.Hex(construct.Bytes(4)),
    "0xBB66 Marker" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 12" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 13" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 14" / construct.Hex(construct.Bytes(8)),
    "Unknown Space 15" / construct.Hex(construct.Bytes(2)),
    "Unknown Space 16" / construct.Hex(construct.Bytes(2)),
    "Empty Space 7" / construct.Hex(construct.Bytes(8)),
    "Unknown Space 17" / construct.Hex(construct.Bytes(4)),
    "boot0 Parameters 1" / construct.Hex(construct.Bytes(16)),
    "boot0 Parameters 2" / construct.Hex(construct.Bytes(16)),
    "boot0 Parameters 3" / construct.Hex(construct.Bytes(16)),
    "Empty Space 8" / construct.Hex(construct.Bytes(16)),
)

# Defining necessary arguments.
arguments = sys.argv
backup_file = arguments[-1]
# Print when the program is started.
print("Coffee Reading (v1.0.0)")
print("Created by NoahAbc12345.\n")
print("Please do not share any values obtained from this program!")
print("Many are illegal to share due to copyright law and/or unique "
    + "to your own console!")
# Begin to parse through the backup data.
validate_arguments(arguments, backup_file)
if os.stat(backup_file).st_size == 512:
    print("Useful Information: https://wiiubrew.org/wiki/Hardware/SEEPROM\n")
    backup_data = seeprom_structure.parse_file(backup_file)
elif os.stat(backup_file).st_size == 1024:
    print("Useful Information: https://wiiubrew.org/wiki/Hardware/OTP\n")
    backup_data = otp_structure.parse_file(backup_file)
# Run the reading function to pull keys.
read_backup_data(arguments, backup_data)
text_file = f"Coffee_Reading_{int(time.time())}.txt"
# If saving is requested, run the writing function.
if any(flag in arguments for flag in ["-s", "--save"]):
    write_backup_data(arguments, backup_data, text_file)
    print(f"\nThe report has been written to {text_file} successfully.\n")
else:
    # Remind the user that saving the keys to a file is possible.
    print("\nProvide \"-s\" or \"--save\" as an argument to save a report.\n")
