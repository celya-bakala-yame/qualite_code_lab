from collections.abc import Iterator

#avec le e typage, on a précisé ce que la fonction attend et ce qu’elle fournit
def fib(n: int) -> Iterator[int]:
    """
    >>> list(fib(10))
    [0, 1, 1, 2, 3, 5, 8]
    >>> list(fib(1))
    [0]
    >>> list(fib(0))
    []
    """
    
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def main() -> None:
    for nombre in fib(10):
        print(nombre)


if __name__ == "__main__":
    main()
    
#cmd : uv run mypy --strict typing_exemples.py
#Les annotations ne convertissent pas les valeurs et ne sont pas imposées par Python. 
#Mypy les vérifie ; son message de réussite signifie qu’il n’a trouvé aucune incohérence 
#de typage dans ce fichier,