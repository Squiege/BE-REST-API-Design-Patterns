from flask import Blueprint
from controllers.orderController import save

order_blueprint = Blueprint('order_bp', __name__)

order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/<int:order_id>', methods=['GET'])(save)
order_blueprint.route('/orders', methods=['GET'])(save)