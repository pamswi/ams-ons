# import the app and the db from app.py
from relationships import db, app, Products, Orders, prodOrder


with app.app_context():
    db.drop_all()
    db.create_all()

    # create some sample products
    testproduct = Products(product_name="Milk")
    testproduct2 = Products(product_name="Bread")
    testproduct3 = Products(product_name="Tea")
    db.session.add(testproduct)
    db.session.add(testproduct2)
    db.session.add(testproduct3)
    db.session.commit()

 
    order1 = Orders()
    order2 = Orders()
        
    # associate products with orders through the prodOrder junction table
    prod_order1 = prodOrder(order=order1, product=testproduct)
    prod_order2 = prodOrder(order=order1, product=testproduct2)
    prod_order3 = prodOrder(order=order1, product=testproduct3)
    prod_order4 = prodOrder(order=order2, product=testproduct3)
        
    db.session.add_all([order1, order2, prod_order1, prod_order2, prod_order3, prod_order4])
    db.session.commit()

    testitem = Products.query.filter_by(id=2).first()
    print(testitem.product_name)