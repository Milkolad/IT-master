from metro import Metro


def main(filepath):
    metro = Metro(filepath)
    #metro.print()
    return 0
    
if __name__ == "__main__":
    main('./list_of_moscow_metro_stations.tsv')