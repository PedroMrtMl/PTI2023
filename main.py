from geo import PHARMACIES, get_nearby_pharmacies

def main():
    fecap_location = input("Digite seu CEP: ")  # Nome da localização
    radius_km = float(input("Raio em KM: ")) #Raio em km

    pharmacies = get_nearby_pharmacies(fecap_location, radius_km, PHARMACIES)

    if pharmacies:
        print("Farmácias encontradas dentro do raio:")
        for idx, pharmacy in enumerate(pharmacies, start=1):
            print(f"{idx}. {pharmacy['name']} - Distância: {pharmacy['distance']:.2f} km")

    else:
        print("Nenhuma farmácia encontrada dentro do raio.")

if __name__ == "__main__":
    main()