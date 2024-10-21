from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from supabase import create_client, Client
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

supabase: Client = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

@app.route('/')
def index():
    response = supabase.table("bikes").select("*").execute()
    bikes = response.data
    return render_template('bike_list.html', bikes=bikes)

@app.route('/add', methods=['GET', 'POST'])
def add_bike():
    if request.method == 'POST':
        model = request.form['model']
        category = request.form['category']
        price = request.form['price']

        if float(price) < 100:
            flash('O preço mínimo de uma bicicleta é R$ 100,00.')
            return redirect(url_for('add_bike'))

        existing_bike = supabase.table("bikes").select("*").eq("model", model).execute()
        if existing_bike.data:
            flash('Uma bicicleta com este modelo já está cadastrada.')
            return redirect(url_for('add_bike'))

        new_bike = {"model": model, "category": category, "price": float(price), "status": "Disponível"}
        supabase.table("bikes").insert(new_bike).execute()
        return redirect(url_for('index'))

    return render_template('add_bike.html')

@app.route('/sell/<int:bike_id>')
def sell_bike(bike_id):
    response = supabase.table("bikes").select("*").eq("id", bike_id).execute()
    bike = response.data[0] if response.data else None
    if bike and bike['status'] == 'Disponível':
        supabase.table("bikes").update({"status": "Vendida"}).eq("id", bike_id).execute()
    return redirect(url_for('index'))

@app.route('/remove/<int:bike_id>')
def remove_bike(bike_id):
    response = supabase.table("bikes").select("*").eq("id", bike_id).execute()
    bike = response.data[0] if response.data else None
    if bike and bike['status'] == 'Disponível':
        supabase.table("bikes").delete().eq("id", bike_id).execute()
    return redirect(url_for('index'))

@app.route('/bike/<int:bike_id>')
def view_bike(bike_id):
    response = supabase.table("bikes").select("*").eq("id", bike_id).execute()
    bike = response.data[0] if response.data else None
    return render_template('view_bike.html', bike=bike)

if __name__ == '__main__':
    app.run(debug=True)
