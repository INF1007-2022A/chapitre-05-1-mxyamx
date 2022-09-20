def use_prefixes() -> list[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    SPACE = ' '
    noms= ''
    for lettre in prefixes:
        noms += f'{lettre}{suffixe} '
    print(noms)
print(use_prefixes())