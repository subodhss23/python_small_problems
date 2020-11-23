''' Create a function that converts a string of letters to their respective number in the alphabet. 

    A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	...
    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	...

'''

def alph_num(txt):
    new_lst = []
    for i in txt:
        new_lst.append(str(ord(i) - 65))
    return (' ').join(new_lst)

print(alph_num("XYZ"))
print(alph_num("ABCDEF"))
print(alph_num("JAVASCRIPT") )
