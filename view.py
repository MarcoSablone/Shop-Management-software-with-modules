from store import Store

class Actions():
    """
    This class contains the main actions of the market, like:
    - buy a product
    - sell a product
    - show the contents of warehouse
    - show the gross and net profit
    - show the available commands
    - input the commands
    """

    def renderBuy(self, store):
        """
        :param store: object of class Store
        It describes the purchase steps
        :return: print on file the products purchased
        """
        prod_bought = {}  # key = name; value = quantity
        answer_list = ["si", "no"]
        demand = answer_list[0]

        while demand == "si":
            name = input("Inserisci un prodotto: ")

            if store.inStore(name) is False:
                amount = (input("Inserisci la quantità da acquistare: "))

                while store.isPositiveInteger(amount) is False:
                    amount = (input("Inserisci la quantità da acquistare: "))

                amount = int(amount)

                purchase = input("Inserisci il prezzo di acquisto: ")

                while store.isPositiveFloat(purchase) is False:
                    purchase = input("Inserisci il prezzo di acquisto: ")

                purchase = float(purchase)

                sale = input("Inserisci il prezzo di vendita: ")

                while store.isPositiveFloat(sale) is False:
                    sale = input("Inserisci il prezzo di vendita: ")

                sale = float(sale)

                store.add(name, amount, purchase, sale)
                store.buy(name, amount)
                prod_bought[name] = amount

                demand = input("Vuoi acquistare un altro prodotto? [si/no]: ")

            else:
                amount = input("Inserisci la quantità da acquistare: ")

                while store.isPositiveInteger(amount) is False :
                    amount = input("Inserisci la quantità da acquistare: ")

                amount = int(amount)

                store.increase(name, amount)
                store.buy(name, amount)
                prod_bought[name] = amount

                demand = input("Vuoi acquistare un altro prodotto? [si/no]: ")

        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:

            f.write("\n----ACQUISTO REGISTRATO----\n\n")
            f.write("AGGIUNTO:\n\n")

            for key, value in prod_bought.items():
                f.write(f"- N. {value} X {key}\n")


    def renderSale(self, store):
        """
        :param store: object of class Store
        It describes the sale steps
        :return: print on file the products sold and the total cash collected
        """

        prod_sold = {} #key = name; value = {quantity; total sale}
        answer_list = ["si", "no"]
        demand = answer_list[0]

        while demand == "si":
            name = input("Inserisci il prodotto da vendere: ")

            if store.inStore(name) is True:
                quantity = input("Inserisci la quantità da vendere: ")

                while store.isPositiveInteger(quantity) is False:
                    quantity = input("Inserisci la quantità da vendere: ")

                quantity = int(quantity)

                if store.inStock(name, quantity) is True:
                    round( store.sale(name, quantity), 2 )
                    store.decrease(name, quantity)
                    prod_sold[name] = {"quantity": quantity, "sell": store.sale(name, quantity)}

                    total_sold = 0
                    total_sold += store.sale(name, quantity)

                    demand = input("Vuoi vendere un altro prodotto? [si/no]: ")

        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:

            f.write("\n-----VENDITA REGISTRATA-----\n\n")

            for key, value in prod_sold.items():
                f.write( "- %d X %s: %f €\n" % ( value["quantity"], key, round(value["sell"], 2) ) )

            f.write(f"\nTotale vendita: {total_sold} €\n")


    def renderShow(self, store):
        """
        :param store: object of class Store
        :return: show and print on file the current contents of warehouse
        """
        #on file
        with open("Bio Market Sas", "a") as f:

            f.write("\n----- BIO MARKET MAGAZZINO -----\n\n")

            for num, value in enumerate(store.getStore().items()):
                f.write(f"{num + 1} - {value[0]}: {value[1]}\n")

        #on program
        for num, value in enumerate(store.getStore().items()):
            print(f"{num + 1} - {value[0]}: {value[1]}")

    def renderProfit(self, store):
        """
        :param store: object of class Store
        :return: print on file gross and net profit
        """
        #on file
        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:
            f.write("\n-----SALDO ATTUALE-----\n\n")
            f.write(f"Profitto lordo: {store.grossProfit()} €\n")
            f.write(f"Profitto netto: {store.netProfit()} €\n\n")

        #on program
        return print(f"Profitto lordo: {store.grossProfit()} € \n Profitto netto: {store.netProfit()} €")

    def helpMenu(self):
        """
        :return: show and print on file the list of available commands
        """
        cmd = {
            "acquista": "acquistare un prodotto",
            "vendita": "vendere un prodotto",
            "magazzino": "mostrare l'inventario di magazzino",
            "cassa": "mostrare i profitti lordi e netti",
            "esci": "uscire dal programma"
        }

        #on file
        with open("Bio Market Sas", "a+", encoding= "utf-8") as file:
            file.write("---MENÙ LISTA COMANDI---\n\n")

            for key, value in cmd.items():
                file.write(f"- Digita {key} per {value} \n")

        #on program
        print("---MENÙ LISTA COMANDI---")
        for key, value in cmd.items():
            print(f"- Digita {key} per {value}")

    def insertCmd(self, store):
        """
        :param store: object of class Store
        :return: input the command to run
        """

        cmd = ""

        while cmd != "esci":
            cmd = input("Inserisci un comando: ")

            if cmd == "acquista":
                self.renderBuy(store)

            elif cmd == "vendita":
                self.renderSale(store)

            elif cmd == "magazzino":
                self.renderShow(store)

            elif cmd == "cassa":
                self.renderProfit(store)

            elif cmd == "aiuto":
                store.help()

            else:
                if cmd == "esci":
                    print("Bye")

                else:
                    print("Questo comando non è presente nella lista!")