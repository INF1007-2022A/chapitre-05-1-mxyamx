#Vérifier si un groupe est acceptable selon l'âge de plusieurs personnes faisant partie de plusieurs groupes. Vous devez retourner une liste booléenne. Les conditions d'acceptation sont les suivantes:
# Critère de taille: Si le groupe possède plus que 10 membres ou 3 membres et moins, il n'est pas acceptable
# Critère d'âge: Si au moins un membre du groupe est mineur, le groupe n'est pas acceptable
# Critère d'âge: Si un membre du groupe est plus vieux que 70 ans et qu'un autre membre du groupe à exactement 50 ans, le groupe n'est pas acceptable
# Critère d'âge: Si au moins un membre du groupe à exactement 25 ans, alors le groupe est acceptable peut-importe les autres critères d'âges
def verify_ages(groups: list[list[int]]) -> list[bool]:
 groupes = {
    [15, 28, 65, 70, 72], [18,24,22,50,70], [25, 2]
}
result= ''
SPACE = ' '
for groupe in groupes:
    if len <= 3 and len > 10:
        result += str(False) + SPACE
        continue
    if 25 in groupe:
        result += str(True) + SPACE
        continue
    if min(groupe) < 18:
        result += str(False) + SPACE
    if max(groupe) > 70 and 50 in groupe:
        result += str(False) + SPACE
        continue
    result += str(True) + SPACE

print(verify_ages(groupe))

