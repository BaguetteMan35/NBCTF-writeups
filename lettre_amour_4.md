**Challenge : Lettres d'amour 4/4**


Ce challenge nous demandait de faire une attaque Man-in-the-Middle sur un échange de clefs Diffie-Hellman.

Je rapelle que l'échange de clefs Diffie-Hellman ce fait comme ceci :

1) Alice et Bob veulent échanger des clefs, ils se mettent d'accord sur un modulo premier p et un générateur de p nommé g.
2) Alice génère une clef privée notée a, Bob génère une clef privée notée b. On a, bien sûr, a < p et b < p.
3) Alice calcule g puissance a mod p et obtient sa clef publique A. Bob fait de même : sa clef publique B est g puissance b mod p.
4) Alice envoie à Bob A et reçoit de Bob B.
5) Alice calcule B puissance a mod p et Bob calcule A puissance b mod p. Alice et Bob ont maintenant la clef : g puissance a * b mod p car (g puissance a) puissance b = (g puissance b) puissance a.

Pour notre attaque Man-in-the-Middle, les valeurs que l'ont peut changer lors de l'envoi sont p, g, A et B. On peut procéder de plusieurs manières:

* Changer p pour que p = 1. Alors, lorsque Bob va calculer B, il obtiendra g puissance b mod 1, qui est égal à 0. En envoyant ce B à Alice, elle obtiendra 0 puissance a mod p = 0 et Bob, lorsqu'il calculera A puissance b mod 1 obtiendra également 0.
* Changer A pour que A = 1 (ou A = 0). Ainsi, lorsque Bob calculera la clef, il obtiendra 1 (ou 0). Ensuite, quand Bob envoie B à Alice, on modifie le message pour que B = 1 (ou B = 0). Alors, lorsque Alice calculera la clef, elle obtiendra 1 (ou 0).

La première méthode étant plus facile car il n'y a aucun besoin de recopier la modulo lors du Man-in-the-Middle (celui-ci est très long), je décrirais comment obtenir le flag en utilisant cette méthode:

1) Ouvrir un invitée de commande sur Linux
2) Entrer la commande suivante:
    nc amour.nobrackets.fr 30340
3) Ecrire le texte suivant:
    {"p" : 1, "g" : 2, "A" : 1}
La valeur de A entrée ici est peu importante tant qu'elle est entière.
4) En réponse, on obtient:
    Interception du message de Bob : {B : 1}
Ecrire le texte suivant:
    {"B" : 1}
5) Indiquer la valeur de la clef partagée : 1
6) Obtenir le flag:
    NBCTF{Att3nT10n_A_L'H0mm3_Du_M1LL13U}
    
