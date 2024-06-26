import pandas as pd
from scipy.stats import ttest_rel, f_oneway, wilcoxon


# Dados da frequencia cardiaca pré-jogo e pós-jogo para cada jogo
data_pre_jogo_inside = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [80, 88, 67, 74, 77, 81, 71, 79, 82, 80, 79, 81, 87, 107, 74, 77, 83, 72, 73, 86]
}

data_pos_jogo_inside = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [79, 94, 85, 82, 100, 86, 73, 86, 90, 88, 87, 93, 91, 85, 75, 87, 80, 81, 79, 111]
}

data_pre_jogo_phasmophobia = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [84, 81, 63, 68, 86, 82, 60, 78, 82, 72, 86, 77, 79, 67, 75, 87, 80, 83, 71, 111]
}

data_pos_jogo_phasmophobia = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [88, 89, 75, 91, 102, 94, 73, 86, 82, 89, 86, 90, 84, 95, 73, 111, 87, 78, 71, 94]
}

data_pre_jogo_rocketleague = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [86,87,74,66,82,75,89,74,87,80,86,80,81,68,71,92,103,73,69,82]
}

data_pos_jogo_rocketleague = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [93,109,83,86,103,101,71,97,85,89,94,95,92,74,86,87,85,65,73,94]
}

data_pre_jogo_valorant = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [72,81,69,68,92,95,64,91,76,77,83,83,79,67,80,92,72,86,76,84]
}

data_pos_jogo_valorant = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'fq': [90,105,104,82,110,95,83,95,95,86,102,111,88,83,81,88,103,92,92,98]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo_inside = pd.DataFrame(data_pre_jogo_inside)
df_pos_jogo_inside = pd.DataFrame(data_pos_jogo_inside)
df_pre_jogo_phasmophobia = pd.DataFrame(data_pre_jogo_phasmophobia)
df_pos_jogo_phasmophobia = pd.DataFrame(data_pos_jogo_phasmophobia)
df_pre_jogo_rocketleague = pd.DataFrame(data_pre_jogo_rocketleague)
df_pos_jogo_rocketleague = pd.DataFrame(data_pos_jogo_rocketleague)
df_pre_jogo_valorant = pd.DataFrame(data_pre_jogo_valorant)
df_pos_jogo_valorant = pd.DataFrame(data_pos_jogo_valorant)

# Calculando média e desvio padrão do pré/pós jogo para cada frequência
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para pré/pós jogo
stats_pre_jogo_inside = calcular_stats(df_pre_jogo_inside)
stats_pos_jogo_inside = calcular_stats(df_pos_jogo_inside)
stats_pre_jogo_phasmophobia = calcular_stats(df_pre_jogo_phasmophobia)
stats_pos_jogo_phasmophobia = calcular_stats(df_pos_jogo_phasmophobia)
stats_pre_jogo_rocketleague = calcular_stats(df_pre_jogo_rocketleague)
stats_pos_jogo_rocketleague = calcular_stats(df_pos_jogo_rocketleague)
stats_pre_jogo_valorant = calcular_stats(df_pre_jogo_valorant)
stats_pos_jogo_valorant = calcular_stats(df_pos_jogo_valorant)

# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-Inside:")
print(stats_pre_jogo_inside)
print("Estatísticas descritivas para Pós-Inside:")
print(stats_pos_jogo_inside)

print("Estatísticas descritivas para Pré-Phasmophobia:")
print(stats_pre_jogo_phasmophobia)
print("Estatísticas descritivas para Pós-Phasmophobia:")
print(stats_pos_jogo_phasmophobia)

print("Estatísticas descritivas para Pré-Rocket League:")
print(stats_pre_jogo_rocketleague)
print("Estatísticas descritivas para Pós-Rocket League:")
print(stats_pos_jogo_rocketleague)

print("Estatísticas descritivas para Pré-Valorant:")
print(stats_pre_jogo_valorant)
print("Estatísticas descritivas para Pós-Valorant:")
print(stats_pos_jogo_valorant)

# Função para calcular o teste de Shapiro-Wilk para normalidade
def calcular_teste_normalidade(dataframe):
    resultados_normalidade = {}
    for coluna in dataframe.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = shapiro(dataframe[coluna])
        resultados_normalidade[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_normalidade).transpose()

# Calculando teste de normalidade para cada jogo
resultado_normalidade_pre_inside = calcular_teste_normalidade(df_pre_jogo_inside)
resultado_normalidade_pos_inside = calcular_teste_normalidade(df_pos_jogo_inside)
resultado_normalidade_pre_phasmophobia = calcular_teste_normalidade(df_pre_jogo_phasmophobia)
resultado_normalidade_pos_phasmophobia = calcular_teste_normalidade(df_pos_jogo_phasmophobia)
resultado_normalidade_pre_rocketleague = calcular_teste_normalidade(df_pre_jogo_rocketleague)
resultado_normalidade_pos_rocketleague = calcular_teste_normalidade(df_pos_jogo_rocketleague)
resultado_normalidade_pre_valorant = calcular_teste_normalidade(df_pre_jogo_valorant)
resultado_normalidade_pos_valorant = calcular_teste_normalidade(df_pos_jogo_valorant)

print("Resultado do teste de normalidade para Pré-Inside:")
print(resultado_normalidade_pre_inside)
print("\n")

print("Resultado do teste de normalidade para Pós-Inside:")
print(resultado_normalidade_pos_inside)
print("\n")

print("Resultado do teste de normalidade para Pré-Phasmophobia:")
print(resultado_normalidade_pre_phasmophobia)
print("\n")

print("Resultado do teste de normalidade para Pós-Phasmophobia:")
print(resultado_normalidade_pos_phasmophobia)
print("\n")

print("Resultado do teste de normalidade para Pré-Rocket League:")
print(resultado_normalidade_pre_rocketleague)
print("\n")

print("Resultado do teste de normalidade para Pós-Rocket League:")
print(resultado_normalidade_pos_rocketleague)
print("\n")

print("Resultado do teste de normalidade para Pré-Valorant:")
print(resultado_normalidade_pre_valorant)
print("\n")

print("Resultado do teste de normalidade para Pós-Valorant:")
print(resultado_normalidade_pos_valorant)
print("\n")

# Função para calcular o teste de Wilcoxon pareado
def calcular_teste_wilcoxon_pareado(df_pre, df_pos):
    resultados_wilcoxon_pareado = {}
    for coluna in df_pre.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        stat, p_valor = wilcoxon(df_pre[coluna], df_pos[coluna])
        resultados_wilcoxon_pareado[coluna] = {'W-statistic': stat, 'p_valor': p_valor}
    return pd.DataFrame(resultados_wilcoxon_pareado).transpose()

# Calculando teste de Wilcoxon pareado para cada jogo
resultado_wilcoxon_inside = calcular_teste_wilcoxon_pareado(df_pre_jogo_inside, df_pos_jogo_inside)
resultado_wilcoxon_phasmophobia = calcular_teste_wilcoxon_pareado(df_pre_jogo_phasmophobia, df_pos_jogo_phasmophobia)
resultado_wilcoxon_rocketleague = calcular_teste_wilcoxon_pareado(df_pre_jogo_rocketleague, df_pos_jogo_rocketleague)
resultado_wilcoxon_valorant = calcular_teste_wilcoxon_pareado(df_pre_jogo_valorant, df_pos_jogo_valorant)


print("Resultado do teste de Wilcoxon pareado para Inside:")
print(resultado_wilcoxon_inside)
print("\n")

print("Resultado do teste de Wilcoxon pareado para Phasmophobia:")
print(resultado_wilcoxon_phasmophobia)
print("\n")

print("Resultado do teste de Wilcoxon pareado para Rocket League:")
print(resultado_wilcoxon_rocketleague)
print("\n")

print("Resultado do teste de Wilcoxon pareado para Valorant:")
print(resultado_wilcoxon_valorant)
print("\n")
