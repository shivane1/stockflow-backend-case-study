@app.route('/api/companies/<company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    inventories = Inventory.query.join(Product).join(Warehouse)\
        .filter(Warehouse.company_id == company_id).all()

    for inventory in inventories:
        product = inventory.product

        if not has_recent_sales(product.id):
            continue

        if inventory.quantity > product.low_stock_threshold:
            continue

        supplier = None
        if product.suppliers:
            supplier = {
                "id": product.suppliers[0].id,
                "name": product.suppliers[0].name,
                "contact_email": product.suppliers[0].contact_email
            }

        alerts.append({
            "product_id": product.id,
            "product_name": product.name,
            "sku": product.sku,
            "warehouse_id": inventory.warehouse.id,
            "warehouse_name": inventory.warehouse.name,
            "current_stock": inventory.quantity,
            "threshold": product.low_stock_threshold,
            "days_until_stockout": 10,
            "supplier": supplier
        })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }, 200
