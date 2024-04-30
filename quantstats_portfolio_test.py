# No presente código é apresentado o módulo de análise financeira "quantstats"
# Esse módulo é extremamente útil para geração de relatórios estatísticos sobre investimentos individuais e portfólios
# Essa biblioteca foi criada por Ran Aroussi, o mesmo criador da "yfinance", de forma que essa biblioteca já está incluída na "quantstats"

#Mas e se quisermos um portfolio de ações e não apenas uma individual?
#Nesse caso utilizamos a função .make_index do utils.
#Vou usar como exemplo um portfolio construído com base no Índice de Ações Cearenses da Universidade de Fortaleza: https://www.unifor.br/en/nupe/indice-de-acoes-cearense-iac
# O portfólio, como de praxe, será construído com base em pesos atribuídos a determinado conjunto de ações; no aqui analisado pesos iguais

import quantstats as qs

acoes = ['PGMN3.SA', 'BNBR3.SA', 'COCE3.SA', 'GRND3.SA','HAPV3.SA','MDIA3.SA','AERI3.SA']

retorno_das_acoes = qs.utils.download_returns(acoes,period='10y').dropna()

qs.reports.html(retorno_das_acoes,"^BVSP",title="IAC vs Ibovespa",output='iacbvp.html')

#O arquivo HTML será salvo no seu diretório de projetos. Basta clicar e abrir no navegador de preferência


#Se você desejar plotar gráficos em separado basta utilizar a função "plot" ou gerar o report em "full"
#TODAVIA, existe uma pegadinha: você não pode rodar esse código em uma IDE como o Pycharm
#Preferencialmente, você deve rodar o código abaixo no Jupyter Notebook

qs.reports.full(retorno_das_acoes,'^BVSP')


