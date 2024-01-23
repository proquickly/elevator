def get_model_data():
    model_name = input("Name of model: ")
    author = input("Author name: ")
    return {
        'model_name': model_name,
        'author': author
    }
