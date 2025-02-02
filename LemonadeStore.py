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
            f"number_of_stores: {number_of_stores}, number_of_orders: {number_of_orders}, "
            f"number_of_different_beverages: {number_of_different_beverages}, number_of_beverages: {number_of_beverages}"
        )


if __name__ == "__main__":
    import sys

    def read_line(): 
        return sys.stdin.readline().strip().split()

    orderState = OrderState()

    while True:
        line = read_line()
        if not line:
            break

        operation = line[0]

        if operation == 'UPDATE_LIMIT':
            numberOfStores = int(line[1])
            perBeverageTotal = int(line[2])
            orderState.UpdateLimit(numberOfStores, perBeverageTotal)

        elif operation == 'ORDER_UPDATE':
            uniqueId = int(line[1])
            storeId = int(line[2])
            beverageName = line[3]
            quantity = int(line[4])
            orderState.OrderUpdate(uniqueId, storeId, beverageName, quantity)

        elif operation == 'CLOSE_STORE':
            storeId = int(line[1])
            orderState.CloseStore(storeId)

        elif operation == 'PRINT_STATE':
            orderState.PrintState()

        else:
            raise ValueError("Invalid Input")
