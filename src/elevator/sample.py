def concat_ab(a: str, b: str) -> str:
    try:
        result = a + b
    except TypeError:
        print("Must both be strings")
        return None
    return result


print(concat_ab("hello", 1))
