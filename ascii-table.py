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
   
                                                        
