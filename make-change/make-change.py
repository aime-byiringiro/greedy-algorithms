def make_change(money, coins):
    n = len(coins)  # number of coins or notes you have
    answers = []  # initialized the results

    i = n - 1
    while i >= 0:
        while money >= coins[i]:
            money = money - coins[i]
            answers.append(coins[i])
        i = i - 1

    for i in range(len(answers)):
        print(answers[i], end=" ")


def main():
    ni = 93
    cash = [2, 5, 10, 50]
    print("Exchange for", ni, "is : ", end="")
    make_change(ni, cash)


if __name__ == '__main__':
    main()
