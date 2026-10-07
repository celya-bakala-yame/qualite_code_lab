def somme(a: int | float, b: int | float) -> float:
    a, b = float(a), float(b)
    return a + b


def main() -> None:
    print(somme(2, 3))
    print(somme(2.5, 3))


if __name__ == "__main__":
    main()