import pandas as pd

# Dados de exemplo
data = {
    'Type': ['A', 'B', 'C', 'A', 'B'],
    'id': [1, 2, 3, 4, 5],
    'Source': ['Web', 'App', 'Web', 'Web', 'App'],
    'Aprove': [True, False, True, True, False]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Exibindo o DataFrame
print("DataFrame criado:")
print(df)
