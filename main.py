import operaciones_basicas


def main():

    sum = operaciones_basicas.sumar(5,4)
    print('El resultado de la suma es: ', sum)

    rest = operaciones_basicas.restar(10,5)
    print('El resultado de la resta es: ', rest)

    multi = operaciones_basicas.multiplicar(10,20)
    print('El resultado de la multiplicación es: ', multi)

    div = operaciones_basicas.dividir(100,5)
    print('El resultado de la división es: ', round(div))


if __name__ == '__main__':

    main()