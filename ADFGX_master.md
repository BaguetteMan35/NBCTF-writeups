**Challenge : ADFGX master**

ADFGX est une méthode de chiffrement développée par les allemands et utilisée à la fin de la première guerre mondiale.
Le chiffrement suit 3 étapes :

* Substitution de chaque lettres d'un texte par une suite de deux lettres parmi les suivantes : A, D, F, G ou X, d'où le nom de l'algorithme, selon un tableaux de substitution défini au préalable. Ce tableau est une des clé nécessaire au décodage, mais il est possible de retrouver le message originel sans le connaitre.
* Par bloc de la taille de la clé de chiffrement, réarrangement du nouveau texte. La clé est une suite de nombres de la taille voulue, notée n, allant de 1 à n ou de 0 à n-1 et dans un ordre quelconque. Chaque bloc de texte est réarranger de telle manière que la nouvelle première lettre du bloc est celle dont l'indice originel est le premier nombre de la clé, la deuxième nouvelle lettres du bloc est celle dont l'indice était le deuxième nombre de la clé, etc... On peut aussi avoir une clé sous la forme de texte. Dans ce cas, on note l'indice de chaque de lettre dans la clé, puis on trie la clé par ordre alphabétique, enfin, on remplace chaque lettre par les indices qu'avait ces lettres avant d'être triées.
* La dernière étape consiste à séparer les blocs et les répartir eu travers du texte. Ceci est accompli en Prenant la première lettre de chaque bloc, puis de les concaténer. Ensuite, on concatène à ce nouveau str la concaténation des deuxièmes lettres de chaque bloc, et ainsi de suite.

Pour résoudre le challenge, il faut donc prendre l'inverse de ces étapes dans le sens inverse. Pour les deux dernières étapes, veuillez voir ici:
