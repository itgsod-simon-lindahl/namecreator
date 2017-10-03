# namecreator

Ett litet program som läser in användare, förnamn och efternam och utifrån detta skapar unika användarnamn.

Användarnamn läses in från en fil users.csv, resultatet sparas i en csvfil usernicks.csv i formen

    förnamn, efternamn, användarnamn

## användarnamn

Användarnamn skapas utifrån algoritmen 2 första bokstäverna från förnamn och 5 första bokstäverna från efternamn.

ex 

    bo, johansson
    
genererar 

    bo, johansson, bojohan


