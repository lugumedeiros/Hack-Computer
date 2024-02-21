I got really confused about this Assembly language, but with a bit
of time and AI I was able to understand it. It's not that complicated...


First le'ts start with this @i command, this is a A-type instruction.
What it does is a LOAD into REGISTER-A, if you do somethins like "@300",
this really means "Load the number 300 into REG-A".
Exemples:
```
@200 // int 200 -> rA
@300 // int 300 -> rA
@R3  // value inside R3 -> rA
```

I used R3 in the last line, this is something we have available, 16
registers that we can use to store stuff. Use it for variables!


We also have too much Branch instructions I think, but i'ts not the point of
this text/tutorial.
The Branches works by doing a JUMP to the content of A-REGISTER, this is 
very important to understand, it will ALWAYS jump to A. The conditions
on the other hand, will use the D-REGISTER value as a variable, so always LOAD
what you need to test into D-REGISTER.
Exemple:
```
0: random code
1: random code
3: @90 // LOAD 90 -> A 
4: D=A // LOAD A -> D (90 -> D)
5: @0  // LOAD 0 -> A
6: D;JGT // JUMPS to A if D > 0 
//will Jump to the start where PC=0
```


Now for Labels, this is a bit simple, but very effective. Basically
this will store the PC of a determined part of our code, and can 
be used as a form of function.
Exemples:
```
(START) // PC = 0
random code
random code
random code
@START // LOAD START PC(0) -> A
0;JMP  // JUMP to A(0)
```


what is M? This is another weid thing for some, but basically, when you call 
for M this will go into the Memory Address represented by your REGISTER-A.
It's a Pointer.
Exemple:
```
@10 // LOAD 10 -> A 
D=A // LOAD A -> D 
@22 // LOAD 22 -> A
M=D // LOAD D -> Memory[22]
```

This means that now our Memory of Address 22 will have the D value inside.
