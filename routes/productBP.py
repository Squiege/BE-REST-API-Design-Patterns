from flask import Blueprint
from controllers.productController import save

product_blueprint = Blueprint('product_bp', __name__)

product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/<int:product_id>', methods=['GET'])(save)
product_blueprint.route('/products', methods=['GET'])(save)