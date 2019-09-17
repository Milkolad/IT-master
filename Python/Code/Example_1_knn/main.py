import numpy as np
from knn import Knn
from metro import Metro, Line, Station


def main():
    metro = Metro("list_of_moscow_metro_stations.csv", "list_of_moscow_metro_stations_changes.csv")

    print([station.name for station in metro.get_line('Сокольническая').stations])
    print(metro.get_line('D3'))

    knn = Knn(metro, ['Окружная', 'Кофе'])
    print(knn.compute('Окружная'))
    print(metro.get_line('Замоскворецкая').get_length('Ховрино', 'Сокол'))
    
if __name__ == "__main__":
    main()