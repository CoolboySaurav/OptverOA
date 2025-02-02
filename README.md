# 🍹 Beverage Order Management System

## Overview
A robust system for managing beverage orders across multiple stores with enforced constraints on store count and beverage quantities.

## 🛠️ Class Structure: OrderState
### Core Functionality
- Tracks active stores and beverage orders
- Enforces system-wide limits
- Manages store operations and order processing

### Key Methods
| Method | Purpose |
|--------|---------|
| `UpdateLimits()` | Sets store and beverage constraints |
| `OrderUpdate()` | Processes new orders and updates |
| `CloseStore()` | Manages individual store closure |
| `CloseAllStores()` | System-wide reset functionality |
| `PrintState()` | Displays current system metrics |

## 📊 System Constraints
- Maximum number of stores
- Per-beverage quantity limits
- Automatic store closure on limit breach

## 🧪 Test Cases Overview
### Test Case 0: Basic Operations
- Tests multiple order updates
- Validates state printing
- Demonstrates beverage variety handling

### Test Case 1: Store Management
- Showcases store closure functionality
- Verifies order count updates
- Tests zero-quantity handling

### Test Case 2: Limit Enforcement
- Validates store count restrictions
- Tests beverage quantity constraints
- Demonstrates order rejection

### Test Case 3: Dynamic Limit Updates
- Tests limit modification impacts
- Validates system reset functionality
- Demonstrates constraint enforcement

## 🎯 System Features
- ✨ Real-time order tracking
- 🔄 Dynamic limit management
- 🛡️ Automated constraint enforcement
- 📝 Comprehensive state reporting


## Test Cases and Outputs

### Test Case 0
**Commands:**
1. `UPDATE_LIMIT(100, 1000)`
2. `ORDER_UPDATE(1, 1, "lemonade", 100)`
3. `ORDER_UPDATE(2, 2, "hot_chocolate", 50)`
4. `PRINT_STATE()`
5. `ORDER_UPDATE(3, 3, "lemonade", 75)`
6. `ORDER_UPDATE(4, 1, "lemonade", 150)`
7. `ORDER_UPDATE(5, 1, "water", 50)`
8. `PRINT_STATE()`

**Output:**
```
number_of_stores:2, number_of_orders:2, number_of_different_beverages:2, number_of_beverages:150
number_of_stores:2, number_of_orders:3, number_of_different_beverages:3, number_of_beverages:200
```

### Test Case 1
**Commands:**
1. `UPDATE_LIMIT(100, 1000)`
2. `ORDER_UPDATE(1, 1, "lemonade", 100)`
3. `ORDER_UPDATE(2, 2, "hot_chocolate", 50)`
4. `PRINT_STATE()`
5. `CLOSE_STORE(1)`
6. `PRINT_STATE()`
7. `ORDER_UPDATE(3, 2, "hot_chocolate", 0)`
8. `PRINT_STATE()`

**Output:**
```
number_of_stores:2, number_of_orders:2, number_of_different_beverages:2, number_of_beverages:150
number_of_stores:1, number_of_orders:1, number_of_different_beverages:1, number_of_beverages:50
number_of_stores:1, number_of_orders:1, number_of_different_beverages:1, number_of_beverages:50
```

### Test Case 2
**Commands:**
1. `UPDATE_LIMIT(2, 100)`
2. `ORDER_UPDATE(1, 1, "lemonade", 100)`
3. `ORDER_UPDATE(2, 2, "hot_chocolate", 50)`
4. `ORDER_UPDATE(3, 2, "lemonade", 1)`
5. `ORDER_UPDATE(4, 3, "hot_chocolate", 1)`

**Output:**
```
reject_order: 4
```

### Test Case 3
**Commands:**
1. `UPDATE_LIMIT(1, 100)`
2. `ORDER_UPDATE(1, 1, "lemonade", 100)`
3. `UPDATE_LIMIT(1, 50)`
4. `PRINT_STATE()`

**Output:**
```
number_of_stores:0, number_of_orders:0, number_of_different_beverages:0, number_of_beverages:0
```

