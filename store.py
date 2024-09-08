class Store:

    def __init__(self):
        """
        set two dictionaries:
        - warehouse: nested dictionary; for each good will be specified amount, purchase and selling price
        - cash: nested dictionary; describe total amount of purchases and sales; both entries are initialized
                to zero
        """
        self.warehouse = {}
        self.cash = {"purchases": 0, "sales": 0}

    def getStore(self):
        """
        :return: show the warehouse contents
        """
        return self.warehouse


    def isPositiveInteger(self, value):
        """
        :param value: string to check if it's an integer and positive value
        :return: return True if the value is a number int or float; negative if it's a string
        """
        try:
            value = int(value)
            assert (value > 0), "Attenzione: il valore deve essere positivo"
            return True

        except ValueError:
            print("Attenzione il valore deve essere numerico")
            return False

        except Exception as e:
            print(e)
            return False

    def isPositiveFloat(self, value):
        """
        :param value: string to check if it's a float and positive value
        :return: True if is a float and positive value; False otherwise
        """
        try:
            value = float(value)
            assert(value > 0), "Attenzione: il valore deve essere positivo"
            return True

        except ValueError:
            print("Attenzione il valore deve essere numerico")
            return False

        except Exception as e:
            print(e)
            return False

    def inStore(self, good):
        """
        :param good: str -> name of good
        :return: True: if the good is present in the warehouse; False: if the good is not present
        """
        if good in self.warehouse:
            return True
        else:
            return False

    def add(self, name, amount, purchase, sale):
        """
        :param name: str -> name of product
        :param amount: int-> amount of product
        :param purchase: float -> purchasing price
        :param sale: float -> selling price
        :return: warehouse with product added
        """
        self.warehouse[name] = {
            "quantità": amount,
            "prezzo di acquisto": purchase,
            "prezzo di vendita": sale
        }

        return self.warehouse

    def increase(self, good, quantity):
        """
        :param good: product added to warehouse
        :param quantity: product quantity to add to original amount
        :return: warehouse
        increase the amount of good added in warehouse
        """
        self.warehouse[good]["quantità"] += quantity

    def decrease(self, good, quantity):
        """
        :param good: product to sell
        :param quantity: quantity of product to sell
        :return: warehouse
        decrease the amount of good to sell in warehouse
        """

        self.warehouse[good]["quantità"] -= quantity

    def buy(self, name, quantity):
        """
        :param good: str -> name of good bought
        :param quantity: int -> amount of good bought
        :return: cash dict
        """
        purchase = round(quantity * self.getStore()[name]["prezzo di acquisto"], 2)
        self.cash["purchases"] += purchase

        return self.cash

    def inStock(self, good, quantity):
        """
        check if the good to sell is present in warehouse and his amount is available
        :param good: str -> name of  good to sell
        :param quantity: int -> amount to sell
        :return: True if the amount is available; False if it's not available

        """
        try:
            assert(quantity <= self.warehouse[good]["quantità"]), "Attenzione: la quantità richiesta non è " \
                                                                "disponibile in magazzino"
            return True

        except Exception as e:
            print(e)
            return False

    def sale(self, good, quantity):
        """
        record the sale
        :param good: name of the product to sell
        :param quantity: int -> amount of good to sell
        :return: cash dict
        """

        sale = round(quantity * self.warehouse[good]["prezzo di vendita"], 2)
        self.cash["sales"] += sale

        return sale

    def grossProfit(self):
        """
        :return: show the gross profit -> only the sales
        """
        return round(self.cash["sales"], 2)

    def netProfit(self):
        """
        :return: show the net profit -> subtracts purchases from sales
        """

        return round(self.cash["sales"] - self.cash["purchases"], 2)

    def help(self):
        """
        :return: show and print on file the list of available commands
        """

        cmd = {
            "acquisto": "acquistare un prodotto",
            "vendita": "vendere un prodotto",
            "magazzino": "mostrare l'inventario di magazzino",
            "cassa": "mostrare i profitti lordi e netti",
            "esci": "uscire dal programma"
        }

        print("---MENÙ LISTA COMANDI---")
        for key, value in cmd.items():
            print(f"- Digita {key} per {value}")