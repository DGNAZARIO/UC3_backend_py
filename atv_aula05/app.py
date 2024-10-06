from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bikes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Necessário para usar flash messages
db = SQLAlchemy(app)


# Modelo da bicicleta
class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False, unique=True)  # Modelo único
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Disponível')


# Cria o banco de dados
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    bikes = Bike.query.all()
    return render_template('bike_list.html', bikes=bikes)


@app.route('/add', methods=['GET', 'POST'])
def add_bike():
    if request.method == 'POST':
        model = request.form['model']
        category = request.form['category']
        price = request.form['price']

        # Validação do preço
        if float(price) < 100:
            flash('O preço mínimo de uma bicicleta é R$ 100,00.')
            return redirect(url_for('add_bike'))

        # Verificar se a bicicleta já existe
        if Bike.query.filter_by(model=model).first():
            flash('Uma bicicleta com este modelo já está cadastrada.')
            return redirect(url_for('add_bike'))

        new_bike = Bike(model=model, category=category, price=float(price))
        db.session.add(new_bike)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_bike.html')


@app.route('/sell/<int:bike_id>')
def sell_bike(bike_id):
    bike = Bike.query.get(bike_id)
    if bike and bike.status == 'Disponível':
        bike.status = 'Vendida'
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/remove/<int:bike_id>')
def remove_bike(bike_id):
    bike = Bike.query.get(bike_id)
    if bike and bike.status == 'Disponível':
        db.session.delete(bike)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/bike/<int:bike_id>')
def view_bike(bike_id):
    bike = Bike.query.get(bike_id)
    return render_template('view_bike.html', bike=bike)


if __name__ == '__main__':
    app.run(debug=True)
