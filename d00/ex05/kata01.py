# Put this at the top of your kata01.py file
kata = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
    for k in kata.keys():
        print(k + " was created by " + kata[k])
