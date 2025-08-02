from flask import Blueprint, jsonify, request
from src.models.product import db, Product, Order, OrderItem
from flask_cors import cross_origin

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
@cross_origin()
def get_products():
    """الحصول على جميع المنتجات"""
    try:
        products = Product.query.all()
        return jsonify({
            'success': True,
            'products': [product.to_dict() for product in products]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@product_bp.route('/products/<int:product_id>', methods=['GET'])
@cross_origin()
def get_product(product_id):
    """الحصول على منتج محدد"""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify({
            'success': True,
            'product': product.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@product_bp.route('/orders', methods=['POST'])
@cross_origin()
def create_order():
    """إنشاء طلب جديد"""
    try:
        data = request.get_json()
        
        # التحقق من البيانات المطلوبة
        required_fields = ['customerName', 'customerEmail', 'customerPhone', 'customerAddress', 'items']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }), 400
        
        # حساب المجموع الإجمالي
        total_amount = 0
        for item in data['items']:
            product = Product.query.get(item['productId'])
            if not product:
                return jsonify({
                    'success': False,
                    'error': f'Product with id {item["productId"]} not found'
                }), 404
            total_amount += product.price * item['quantity']
        
        # إنشاء الطلب
        order = Order(
            customer_name=data['customerName'],
            customer_email=data['customerEmail'],
            customer_phone=data['customerPhone'],
            customer_address=data['customerAddress'],
            total_amount=total_amount
        )
        
        db.session.add(order)
        db.session.flush()  # للحصول على order.id
        
        # إضافة عناصر الطلب
        for item in data['items']:
            product = Product.query.get(item['productId'])
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['productId'],
                quantity=item['quantity'],
                price=product.price
            )
            db.session.add(order_item)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'order': order.to_dict(),
            'message': 'تم إنشاء الطلب بنجاح'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@product_bp.route('/orders', methods=['GET'])
@cross_origin()
def get_orders():
    """الحصول على جميع الطلبات"""
    try:
        orders = Order.query.order_by(Order.created_at.desc()).all()
        return jsonify({
            'success': True,
            'orders': [order.to_dict() for order in orders]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@product_bp.route('/orders/<int:order_id>', methods=['GET'])
@cross_origin()
def get_order(order_id):
    """الحصول على طلب محدد"""
    try:
        order = Order.query.get_or_404(order_id)
        return jsonify({
            'success': True,
            'order': order.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@product_bp.route('/init-data', methods=['POST'])
@cross_origin()
def init_sample_data():
    """إضافة بيانات تجريبية للمنتجات"""
    try:
        # التحقق من وجود منتجات
        if Product.query.count() > 0:
            return jsonify({
                'success': True,
                'message': 'البيانات موجودة بالفعل'
            })
        
        # إضافة منتجات تجريبية
        products = [
            Product(
                name='تمر دقلة نور فاخر',
                description='تمر دقلة نور الجزائري الأصيل، معروف بطعمه الحلو ونكهته المميزة',
                price=2500,
                original_price=3000,
                image='/api/static/dates-product1.jpg',
                weight='1 كيلو',
                rating=4.8,
                reviews=124,
                in_stock=True
            ),
            Product(
                name='تمر مش دقلة مميز',
                description='تمر مش دقلة طبيعي 100% من واحات الجزائر، غني بالفيتامينات والمعادن',
                price=1800,
                original_price=2200,
                image='/api/static/dates-product2.jpg',
                weight='1 كيلو',
                rating=4.6,
                reviews=89,
                in_stock=True
            ),
            Product(
                name='تشكيلة التمور الجزائرية',
                description='تشكيلة متنوعة من أفضل أنواع التمور الجزائرية في علبة واحدة',
                price=3200,
                original_price=3800,
                image='/api/static/dates-variety.jpg',
                weight='1.5 كيلو',
                rating=4.9,
                reviews=156,
                in_stock=True
            )
        ]
        
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'تم إضافة البيانات التجريبية بنجاح'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

