# Uma Breve Introdução ao QuantStats
Como gerar um relatório de estatísticas financeiras completo utilizando apenas um pacote e menos de 5 linhas de código?

No presente código é apresentado o pacote de análise financeira "quantstats. Esse pacote é extremamente útil para geração de relatórios estatísticos sobre investimentos individuais e portfólios. Essa biblioteca foi criada por Ran Aroussi, o mesmo criador da "yfinance",um pacote de Python extremamente utilizando para realizar scrapping de dados do Yahoo Finance. Dessa forma, esse pacote já está incluído na "quantstats. Além do "yfinance", tabém estão incluídos pacotes famosos como Matplotlib e Seaborn. 

No código irei realizar a análise de um conjunto de ações contra um benchmark. Vou usar como exemplo um portfolio construído com base no Índice de Ações Cearenses da Universidade de Fortaleza: https://www.unifor.br/en/nupe/indice-de-acoes-cearense-iac. Irei fazer isso por meio da função "quantstats.reports"; gerando um relatório em uma página web por meio da conversão do código em HTML. Se você desejar plotar gráficos em separado basta utilizar a função "plot" ou gerar o report em "full. TODAVIA, existe uma pegadinha: você não pode rodar esse código em uma IDE como o Pycharm. Preferencialmente, você deve rodar o código abaixo no Jupyter Notebook.

Mas e se quisermos um portfolio de ações e não apenas uma individual? Nesse caso utilizamos a função .make_index do utils. Contudo, infelizmente essa função está apresentando issues de soma de strings com floats na geração de eixos. Ainda estamos esperando atualizações de Ran Aroussi com relação a esse problema. 
