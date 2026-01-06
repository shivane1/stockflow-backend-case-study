# StockFlow – Backend Case Study

## Overview
StockFlow is a B2B inventory management platform that helps businesses manage products
across multiple warehouses and suppliers. This repository contains my solution to the
backend case study, focusing on debugging, database design, and API implementation while
working with incomplete requirements.

---

## Part 1: Code Review & Debugging

### Issues Identified

**Technical Issues**
- No validation for required or optional input fields
- No error handling or rollback mechanism
- Multiple database commits instead of a single atomic transaction
- Price handled without enforcing decimal precision
- API does not return proper HTTP status codes
- Assumes request payload is always valid JSON
- No protection against partial writes if inventory creation fails

**Business Logic Issues**
- SKU uniqueness is not enforced across the platform
- Product is incorrectly tied to a single warehouse
- Products cannot exist in multiple warehouses as required
- Inventory is created even if product creation partially fails
- Optional fields like initial_quantity are assumed to exist

### Impact in Production
- Missing validation can lead to runtime crashes and corrupted records
- Duplicate SKUs can cause incorrect inventory tracking and billing issues
- Partial commits can result in orphan inventory records
- Incorrect product-warehouse modeling prevents multi-warehouse scaling
- Floating-point prices can cause rounding errors in financial calculations
- Lack of rollback can leave the system in an inconsistent state

### Corrected Implementation
The corrected version ensures proper validation, transactional safety, SKU uniqueness,
and accurate handling of decimal prices.

(See: part1_code_review/create_product_fixed.py)

---

## Part 2: Database Design

### Assumptions
- A company can own multiple warehouses
- Products belong to a company, not a warehouse
- Inventory is tracked per product per warehouse
- Inventory changes must be auditable
- Products can have multiple suppliers
- Some products may be bundles of other products

### Schema Overview
The schema separates products, warehouses, and inventory to allow scalability and
accurate stock tracking.

(See: part2_database_design/schema.md)

---

## Part 3: Low-Stock Alert API

### Endpoint
GET /api/companies/{company_id}/alerts/low-stock

### Business Rules
- Low-stock threshold varies by product
- Alerts are generated only for products with recent sales
- Inventory is evaluated per warehouse
- Supplier information is included for reordering

(See: part3_low_stock_api/low_stock_alerts.py)

---

## Assumptions
Due to incomplete requirements, several assumptions were made and documented to ensure
a realistic and scalable backend design.

(See: assumptions.md)
