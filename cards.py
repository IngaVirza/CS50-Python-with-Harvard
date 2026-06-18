import random
cards = ["jack", "queen", "king"]


def main():
    # print(random.choices(cards, k=2))
    # print(random.sample(cards, k=2))

    # print(random.choices(cards, weights=[50, 20, 100], k=3))

    random.seed(1)
    print(random.choices(cards, k=2))
main()