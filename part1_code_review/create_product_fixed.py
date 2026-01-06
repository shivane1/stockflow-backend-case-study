from decimal import Decimal
from sqlalchemy.exc import IntegrityError

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON payload"}, 400

    required_fields = ['name', 'sku', 'price', 'warehouse_id']
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}, 400

    try:
        if Product.query.filter_by(sku=data['sku']).first():
            return {"error": "SKU already exists"}, 409

        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )

        inventory = Inventory(
            product=product,
            warehouse_id=data['warehouse_id'],
            quantity=data.get('initial_quantity', 0)
        )

        db.session.add_all([product, inventory])
        db.session.commit()

        return {
            "message": "Product created successfully",
            "product_id": product.id
        }, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "Database integrity error"}, 500

    except Exception:
        db.session.rollback()
        return {"error": "Unexpected server error"}, 500
