///////////////////////////////////////////////////////////////////////
//MAIN
(MAIN)
@8191
D=A
@N
M=D  //LOAD 4096 THAT SUMS TO ALL SCREEN ADDRESSES
@KBD
D=M
@WHITE
D;JEQ   // JUMP TO WHITE IF KEYBOARD = 0 OR CONTINUE TO BLACK

///////////////////////////////////////////////////////////////////////
(BLACK)
@N
D=M
@MAIN
D;JLE   //JUMP TO MAIN IF CHANGE ENDED (D<1)
@SCREEN
A=D+A   //BASE ADDRESS + N
D=-1
M=D     //CHANGE ALL BITS TO 1
@N
D=M
M=D-1    //SUB 1 FROM N
@BLACK
0;JMP

///////////////////////////////////////////////////////////////////////
(WHITE)
@N
D=M 
@MAIN
D;JLE
@SCREEN
A=D+A 
D=0
M=D     //JUST CHANGE ALL TO 0
@N
D=M
M=D-1
@WHITE
0;JMP

///////////////////////////////////////////////////////////////////////

// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//MY NOTES:
//WHILE TRUE PROGRAM 
//TEST IF KEYBOARD HAS ANY NUMBER
//IF YES, THEN SCREEN BECOMES BLACK 
//IF NOT, GOES WHITE AGAIN
//KBD IS THE MEMORY ADDRESS OF OUR KEYBOARD
//SCREEN IS THE MEMORY ADDRESS OF THE FIRST ELEMENT OF OUR SCREEN
//SCREEN =(256x512)
//EACH ROW HAS 512 BITS THAT ARE DIVIDED INTO 16 ADDRESSES
//THERE'S 256 ROWS
//IN TOTAL THERE'S 8192 ADDRESSES
//MOST LEFT BITS REPRESENTS THE MOST LEFT BITS IN THE ADDRESS
//BLACK WHEN TRUE(1), WHITE WHEN FALSE(0)
//00110011 WOULD BE WWBBWWBB IN ORDER.
//AS WE WANT TO CHANGE THE ENTIRE SCREEN, NO ARITHMETIC IS NEEDED
