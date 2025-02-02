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
