from configurations.database import db
from sqlalchemy import text

class BikeRepository:
    @staticmethod
    def get_all_bikes():
        query = text("SELECT * FROM bikes")
        result = db.session.execute(query)
        return result.fetchall()

    @staticmethod
    def add_bike(model, category, price, status="Dispinível"):
        query = text("""
            INSERT INTO bikes (model, category, price, status)
            VALUES (:model, :category, :price, :status)
        """)

        db.session.execute(query, {
            'model': model,
            'category': category,
            'price': price,
            'status': status
        })

        db.session.commit()

    @staticmethod
    def sell_bike(bake_id):
        print(f'>>>>>>>> {bake_id}')
        query = text("UPDATE bikes SET status = TRUE WHERE id = :id")
        db.session.execute(query, {'id': bake_id})
        db.session.commit()

    @staticmethod
    def delete_bike(bake_id):
        print(f'>>>>>>>> {bake_id}')
        query = text("DELETE FROM bikes WHERE id = :id")
        db.session.execute(query, {'id': bake_id})
        db.session.commit()