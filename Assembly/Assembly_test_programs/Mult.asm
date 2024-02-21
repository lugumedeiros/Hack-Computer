//R2 must be the result
//R0 and R1 our variables

//////////////////////////////////////////////////////////
//LOAD X INTO SAFE ADDRESS
@R0     //THIS IS WHERE OUR 1ST VALUE IS
D=M
@X      //SELECT EMPTY MEMORY
M=D     //X

//LOAD Y INTO SAFE ADDRESS
@R1
D=M 
@Y
M=D

//LOAD SUM SAFE ADDRESS
@SUM
M=0

//////////////////////////////////////////////////////////
//MAIN FUNCITON
(LOOP)
@Y      //SELECT Y FOR TEST
D=M
@END
D;JLE   //JUMP TO (END) if Y < 1

//MULTIPLY 1 TIME
@SUM    
D=M     //STORE SUM INTO D
@X
D=D+M   //D <- SUM + X
@SUM
M=D     //LOAD RESULT INTO SUM
@Y
D=M
D=D-1   //SUB 1 FROM Y
M=D     //STORE RESULT IN Y
@LOOP
0;JMP   //JUMP TO MAIN FUNCITON

(END)
@SUM
D=M 
@R2 
M=D     //STORE SUM INTO R2
//////////////////////////////////////////////////////////

(ENDLOOP)
@ENDLOOP
0;JMP