# Arduboy Home

Play Arduboy games on the big screen with the Arduboy Home game console.  The tiny OLED display of the Arduboy has been replaced with VGA output, and the Home has a separate, handheld controller.  The home console is compatible with the existing Arduboy game library.

Arduboy Home was inspired by (but is not affiliated with) the open source [Arduboy](https://arduboy.com/) handheld gaming platform.

## How It Works

An Arduboy game is compiled and loaded onto an Arduino Micro.  The compilation uses an `Arduboy2` library that [I modified](https://github.com/nickbild/arduboy_home/tree/main/Arduboy2) to support VGA output.  Only the library has been modified—games are compatible without change.

The primary changes to the library are in the `Arduboy2Base::display()` function, which normally writes to an OLED display over SPI.  I changed the function to write to my custom VGA output device.  I also removed the code that PWMs the RGB LEDs in `Arduboy2Core::setRGBled`.  I have no need for the LEDs in my console, and need to repurpose the pins for VGA digital I/O, so I can't have them PWMing.

I've tested a half dozen or so games, which all work flawlessly.  Because I made changes to the core display function, I would expect this modified library to work everywhere, but haven't extensively tested the game library (there are over 200!).

VGA output is achieved with a TinyFPGA BX.  I used a modified version of my [MiniVGA](https://github.com/nickbild/fpga_vga) VGA generator.  I had to change how pixels are updated to require a lower pin count such that it would work with the ATmega32U4.  The code is [here](https://github.com/nickbild/arduboy_home/tree/main/vga).

## Media

## Bill of Materials

- 1 x Arduino Micro (or similar, with ATmega32U4 microcontroller)
- 1 x TinyFPGA BX
- 2 x 74LVC245AN level shifters
- 6 x push buttons
- 1 x VGA breakout adapter
- 3 x 100 ohm resistors
- 3 x 387 ohm resistors
- Miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
