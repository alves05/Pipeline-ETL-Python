import random

import pandas as pd
from faker import Faker

faker = Faker()


def cria_database(numero_rows):
    quantidade_linhas = numero_rows
    id_usuario = [ids for ids in range(1, quantidade_linhas + 1)]
    nome_usuario = [faker.name() for _ in range(quantidade_linhas)]
    idade_usuario = [random.randint(18, 50) for _ in range(quantidade_linhas)]
    agencia_usuario = ['1001' for _ in range(quantidade_linhas)]
    conta_usuario = [
        random.sample(range(10**5), quantidade_linhas)
        for _ in range(quantidade_linhas)
    ]
    saldo_conta_usuario = [
        round(random.uniform(500, 2000), 2) for _ in range(quantidade_linhas)
    ]
    numero_cartao_usuario = [
        ('**** **** **** ' + str(random.randint(0, 9999)).zfill(4))
        for _ in range(quantidade_linhas)
    ]
    limite_cartao_usuario = [
        round(random.uniform(200, 1000), 2) for _ in range(quantidade_linhas)
    ]
    data = {
        'Id': id_usuario,
        'Nome': nome_usuario,
        'Idade': idade_usuario,
        'Agencia': agencia_usuario,
        'Conta': conta_usuario[0],
        'Saldo': saldo_conta_usuario,
        'Cartao': numero_cartao_usuario,
        'Limite': limite_cartao_usuario,
    }
    dataset = pd.DataFrame(data)
    return dataset.to_csv('database.csv', index=False)


if __name__ == '__main__':
    total_linhas = int(input('Insira a quantidade de linhas para a base: '))
    cria_database(total_linhas)
