import random
random.seed()
out = """Jc = <JC>
Jmin = <JMIN>
Jmax = <JMAX>
S1 = <S1>
S2 = <S2>
H1 = <H1>
H2 = <H2>
H3 = <H3>
H4 = <H4>"""

jc = random.randint(3, 127)
jmin = random.randint(3, 700)
jmax = random.randint(jmin+1, 1270)
out = out.replace('<JC>', str(jc))
out = out.replace('<JMIN>', str(jmin))
out = out.replace('<JMAX>', str(jmax))
out = out.replace('<S1>', str(random.randint(3, 127)))
out = out.replace('<S2>', str(random.randint(3, 127)))
out = out.replace('<H1>', str(random.randint(0x10000011, 0x7FFFFF00)))
out = out.replace('<H2>', str(random.randint(0x10000011, 0x7FFFFF00)))
out = out.replace('<H3>', str(random.randint(0x10000011, 0x7FFFFF00)))
out = out.replace('<H4>', str(random.randint(0x10000011, 0x7FFFFF00)))

with open("headers.txt","w") as file:
    file.write(out)