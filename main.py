from store import Store
from view import Actions


store = Store()
act = Actions()

#show the program title
with open("Bio Market Sas", "w", encoding="utf-8") as f:
    f.write("\t\t---------- SOFTWARE GESTIONALE BIO MARKET SAS ----------\n\n")


act.helpMenu()
act.insertCmd(store)