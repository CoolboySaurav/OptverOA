from collections import defaultdict

class OrderState:
    def __init__(self):
        self.limits = {"stores": 0, "per_beverage_total": 0}
        self.stores = {}  # storeId -> {beverageName: quantity}
        self.beverage_totals = defaultdict(int)  # beverageName -> total quantity

    def UpdateLimits(self, numberOfStores: int, perBeverageTotal: int) -> None:
        self.limits["stores"] = numberOfStores
        self.limits["per_beverage_total"] = perBeverageTotal

        # If limits are exceeded, reset everything
        if len(self.stores) > numberOfStores or any(
            qty > perBeverageTotal for qty in self.beverage_totals.values()
        ):
            self.CloseAllStores()

    def OrderUpdate(self, uniqueId: int, storeId: int, beverageName: str, quantity: int) -> None:
        if storeId not in self.stores:
            self.stores[storeId] = {}

        prev_quantity = self.stores[storeId].get(beverageName, 0)

        # Check limits before updating
        new_total = self.beverage_totals[beverageName] - prev_quantity + quantity
        if len(self.stores) > self.limits["stores"] or new_total > self.limits["per_beverage_total"]:
            print(f"reject_order: {uniqueId}")
            return

        # Update beverage quantity
        self.stores[storeId][beverageName] = quantity
        self.beverage_totals[beverageName] = new_total

        # Remove store if its orders become empty
        if sum(self.stores[storeId].values()) == 0:
            self.CloseStore(storeId)

    def CloseStore(self, storeId: int) -> None:
        if storeId in self.stores:
            for beverage, quantity in self.stores[storeId].items():
                self.beverage_totals[beverage] -= quantity
            del self.stores[storeId]

    def CloseAllStores(self) -> None:
        self.stores.clear()
        self.beverage_totals.clear()

    def PrintState(self) -> None:
        number_of_stores = len(self.stores)
        number_of_orders = sum(len(orders) for orders in self.stores.values())
        number_of_different_beverages = len(self.beverage_totals)
        number_of_beverages = sum(self.beverage_totals.values())

        print(
            f"number_of_stores:{number_of_stores}, number_of_orders:{number_of_orders}, "
            f"number_of_different_beverages:{number_of_different_beverages}, number_of_beverages:{number_of_beverages}"
        )


# --- TESTING THE IMPLEMENTATION ---
if __name__ == "__main__":
    orderState = OrderState()

    # Manual Testing (You may ignore)
    # Sample case 0
    commands = [
        ("UPDATE_LIMIT", 100, 1000),
        ("ORDER_UPDATE", 1, 1, "lemonade", 100),
        ("ORDER_UPDATE", 2, 2, "hot_chocolate", 50),
        ("PRINT_STATE",),
        ("ORDER_UPDATE", 3, 3, "lemonade", 75),
        ("ORDER_UPDATE", 4, 1, "lemonade", 150),
        ("ORDER_UPDATE", 5, 1, "water", 50),
        ("PRINT_STATE",),
    ]

    # Sample case 1
    commands = [
         ("UPDATE_LIMIT", 100, 1000),
        ("ORDER_UPDATE", 1, 1, "lemonade", 100),
        ("ORDER_UPDATE", 2, 2, "hot_chocolate", 50),
        ("PRINT_STATE",),
        ("CLOSE_STORE", 1),
        ("PRINT_STATE",),
        ("ORDER_UPDATE", 3, 2, "hot_chocolate", 0),
        ("PRINT_STATE",),
    ]

    # Sample case 2
    commands = [
        ("UPDATE_LIMIT", 2, 100),
        ("ORDER_UPDATE", 1, 1, "lemonade", 100),
        ("ORDER_UPDATE", 2, 2, "hot_chocolate", 50),
        ("ORDER_UPDATE", 3, 2, "lemonade", 1),
        ("ORDER_UPDATE", 4, 3, "hot_chocolate", 1),

    ]   

    # Sample case 3
    commands = [
        ("UPDATE_LIMIT", 1, 100),
        ("ORDER_UPDATE", 1, 1, "lemonade", 100), 
        ("UPDATE_LIMIT", 1, 50),
        ("PRINT_STATE",),
    ]



    for cmd in commands:
        if cmd[0] == "UPDATE_LIMIT":
            orderState.UpdateLimits(cmd[1], cmd[2])
        elif cmd[0] == "ORDER_UPDATE":
            orderState.OrderUpdate(cmd[1], cmd[2], cmd[3], cmd[4])
        elif cmd[0] == "PRINT_STATE":
            orderState.PrintState()
        elif cmd[0] == "CLOSE_STORE":
            orderState.CloseStore(cmd[1])
