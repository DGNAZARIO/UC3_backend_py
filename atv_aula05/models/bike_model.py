from configurations.database import db

class bike(db.Model):
    __tablename__ = 'bikes'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(80), nullable=False, default="Disponível")

    def __str__(self):
        return f"Bike: {self.model}, Completa: {self.category}, Prioridade: {self.price}"

    def sell(self):
        self.sell = "Vendida"