class Evaluator:
    def invalid_argument(coefs,words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return True
        if sum(1 for coef in coefs if not isinstance(coef, (int, float))):
            return True
        if sum(1 for word in words if not isinstance(word, str)):
            return True
        if len(coefs) != len(words):
            return True
        return False

    def zip_evaluate(coefs, words):
        if Evaluator.invalid_argument(coefs, words):
            return -1
        score = 0
        for item in zip(coefs, words):
            score += item[0] * len(item[1])
        return score

    def enumerate_evaluate(coefs, words):
        if Evaluator.invalid_argument(coefs, words):
            return -1
        score = 0
        for count, value in enumerate(words):
            score += len(value) * coefs[count]
        return score

if __name__ == '__main__':

    # Normal usage
    print("\n1. Normal usage")

    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

    print("\n1.1 zip_evaluate()")
    print(Evaluator.zip_evaluate(coefs, words))

    print("\n1.2 enumerate_evaluate()")
    print(Evaluator.enumerate_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "est", "complexe", "?"]
    coefs = [-42.42424242, 1642, -0, 4, -4242, 21.212121]

    print("\n1.3 zip_evaluate()")
    print(Evaluator.zip_evaluate(coefs, words))

    print("\n1.4 enumerate_evaluate()")
    print(Evaluator.enumerate_evaluate(coefs, words))

    # Error management
    print("\n2. Error management")

    print("\n2.1 Invalid argument 'coefs' (not a list)")
    print(Evaluator.zip_evaluate(1.0, words))

    print("\n2.2 Invalid argument 'words' (not a list)")
    print(Evaluator.zip_evaluate(coefs, "word"))

    print("\n2.3 Invalid argument 'coefs' (list with a non int or float)")
    print(Evaluator.zip_evaluate([1.0, 1, 42.42, "42", 42], words))

    print("\n2.4 Invalid argument 'words' (list with a non str)")
    print(Evaluator.zip_evaluate(coefs, ["word", "word", 2.0, "word"]))

    print("\n2.5 Lists of different sizes")
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.zip_evaluate(coefs, words))

    print()
