## Database Schema

### Company
- id (PK)
- name

### Warehouse
- id (PK)
- company_id (FK)
- name
- location

### Product
- id (PK)
- company_id (FK)
- name
- sku (UNIQUE)
- price (DECIMAL)
- product_type
- low_stock_threshold

### Inventory
- id (PK)
- product_id (FK)
- warehouse_id (FK)
- quantity

**Unique Constraint:** (product_id, warehouse_id)

### InventoryHistory
- id (PK)
- inventory_id (FK)
- change_amount
- reason
- created_at

### Supplier
- id (PK)
- name
- contact_email

### ProductSupplier
- product_id (FK)
- supplier_id (FK)

### ProductBundle
- parent_product_id (FK)
- child_product_id (FK)
- quantity
