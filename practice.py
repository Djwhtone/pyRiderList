from practiceClass import ItemName


def name():
    names = (ItemName(name='Bugs', price=55),
             ItemName(name='Bunnny', price=60))

    for x in names:
        print(x)


def main():
    name()


if __name__ == '__main__':
    main()
