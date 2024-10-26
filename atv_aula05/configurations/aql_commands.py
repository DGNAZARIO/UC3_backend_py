from  sqlalchemy import text


def create_table_bike(app, db):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS bikes (
        id SERIAL PRIMARY KEY,
        model VARCHAR(80) NOT NULL,
        category VARCHAR(80) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        status VARCHAR(80) DEFAULT 'Disponível'               
    );"""

    with app.app_context():
        db.session.execute(text(create_table_sql))
        db.session.commit()
        print("Tabela 'bikes' criada com sucesso!")