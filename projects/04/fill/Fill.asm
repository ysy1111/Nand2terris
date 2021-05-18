// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


// Put your code here.
@8192
D=A
@n
M=D // number of RAMs of the whole screen 

(KBDLoop)
@KBD
D = M
@WhiteLoop
D; JEQ // if no key is pressed, do nothing and keep detecting

@SCREEN
D=A
@addr
M=D // record the base address into addr

@i
M=0 // count the block of pixels. there are 256*512/16 = 8192 in total.

(BlackInnerLoop)
@n
D=M
@i
D = D-M
@KBDLoop
D;JEQ // if i == n(8192), finish black the screen, go back to detect the keyboard


@addr
A=M
M=-1

@i
M = M + 1
@addr
M = M + 1

@BlackInnerLoop
0;JMP

(WhiteLoop)
@SCREEN
D=A
@addr
M=D // record the base address into addr

@i
M=0 // count the block of pixels. there are 256*512/16 = 8192 in total.

(WhiteInnerLoop)
@n
D=M
@i
D = D-M
@KBDLoop
D;JEQ // if i == n(8196), finish black the screen, go back to detect the keyboard


@addr
A=M
M=0

@i
M = M + 1
@addr
M = M + 1

@WhiteInnerLoop
0;JMP