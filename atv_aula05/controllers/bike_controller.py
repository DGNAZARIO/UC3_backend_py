from flask import Blueprint, render_template, request, redirect, url_for
from services.bike_service import BikeService

bike_blueprint = Blueprint('bike', __name__)
bike_service = BikeService()


@bike_blueprint.route('/')
def index():
    bikes = bike_service.get_all_bikes()
    total_price = bike_service.get_total_price()
    return render_template('index.html', bikes=bikes, total_price=total_price)


@bike_blueprint.route('/add', methods=['POST'])
def add_bike():
    model = request.form.get("model")
    category = request.form.get("category")
    price = float(request.form.get("price"))

    try:
        bike_service.add_bike(model, category, price)
    except ValueError as e:
        return str(e), 400

    return redirect(url_for('bike.index'))


@bike_blueprint.route('/sell/<int:bake_id>', methods=['POST'])
def sell_bike(bake_id):

    try:
        bike_service.sell_bike(bake_id)
    except Exception as e:
        return str(e), 400

    return redirect(url_for('bike.index'))


@bike_blueprint.route('/delete/<int:bake_id>', methods=['POST'])
def delete_bike(bake_id):

    try:
        bike_service.delete_bike(bake_id)
    except Exception as e:
        return str(e), 400

    return redirect(url_for('bike.index'))

def get_total_price(self):
    bikes = self.get_all_bikes()
    total_price = sum(bike.price for bike in bikes if bike.status == "Vendida")
    return total_price