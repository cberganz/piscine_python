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
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))
