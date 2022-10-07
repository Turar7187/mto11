

def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x < 7:
        y = (2*a*b*x) / ((a+b)**2)
    else:
        y = x*(x**2 + 4*b)

    print("y = %.1f" % y)



if __name__ == '__main__':
    main()