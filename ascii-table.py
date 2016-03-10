import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


#Printing ascii characters
print("Ascii code 100= " + chr(100))

#Ascii table program
# ASCII Table Printer #2
# Chapter 14

chars = \
"☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !\"#$%&'()*+,-./0123456789:;<=>?@"\
"ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂Ç"\
"üéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└"\
"┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■? "


cols = 8
rows = 256//cols
table = list("" for n in range(rows+1))
char = 0

for col in range(1,cols+1):
    for row in range(1,rows+1):
        table[row] += '{:3.0f}'.format(char) + ' '
        table[row] += chars[char]
        table[row] += '\t'
        char += 1

print(len(chars))

for row in table: print(row)

#some strange univode issues if not using english here, don;t know how to fix that
#cp950 cant encode character, illegal multibyte sequence
   
                                                        
#create a list to be filled with characters for a map

tiles=list()
for y in range(0,45):
    for x in range(0,80):
        tiles.append(8)
        
#load sprite sheet

text=MySprite()
text.load("ascii8*12.png",8,12,32)

        
#referencing the sprite sheet fill the map
#todo write the myLibrary lubrary since we skipped that
for y in range(0,45):
    for x in range(0,80):
        index=y*80+x
        value=tiles[index]
        text.X=30+x*8
        text.Y=30+y*12
        text.frame=text.last_frame=value
        text.update(0)
        text.draw(surface)