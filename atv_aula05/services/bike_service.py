from repositories.bike_repository import BikeRepository

class BikeService:

    def add_bike(self, model, category, price, status="Disponível"):
        # if price < 100:
        #     raise ValueError("O preço deve ser no mínimo R$ 100,00!")
        BikeRepository.add_bike(model, category, price, status)

    def get_all_bikes(self):
        return BikeRepository.get_all_bikes()

    def sell_bike(self, bake_id):
        BikeRepository.sell_bike(bake_id)

    def delete_bike(self, bake_id):
        BikeRepository.delete_bike(bake_id)

    def get_total_price(self):
        bikes = self.get_all_bikes()
        total_price = sum(bike.price for bike in bikes if bike.status == "Vendida")
        return total_price