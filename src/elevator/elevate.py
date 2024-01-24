def get_model_data():
    model_name = input("Name of model: ")
    author = input("Author name: ")
    floors = input("Number of floors: ")
    width = input("Width (meters): ")
    length = input("Length (meters): ")
    try:
        floors = int(floors)
        width = float(width)
        length = float(length)
    except ValueError:
        raise ValueError("Invalid input: can't convert to int / float")
    return {
        'model_name': model_name,
        'author': author,
        'floors': floors,
        'width': width,
        'length': length
}


if __name__ == "__main__":
    model_data = get_model_data()
