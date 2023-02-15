import re

CYRiLLIC_SYM = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ('a', 'b', 'v', 'g', 'e', 'e', 'j', 'z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's',
               't', 'u', 'f', 'h', 'ts', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'yu', 'u', 'ja', 'je', 'ji', 'g')

# a -> 96
TRANS = {}
for c, l in zip(CYRiLLIC_SYM, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '.', t_name)
    return t_name

