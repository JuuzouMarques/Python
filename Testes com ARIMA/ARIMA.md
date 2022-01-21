#**ARIMA**

Método estatístico que utiliza autoregressão e médias móveis para previsão de séries temporais. Um modelo linear é construído incluindo um número especificado de termos e os dados são preparados por um nível de diferenciação afim de tornar este estacionário.

Podemos usar um valor 'y' para desligar um parâmetro, dessa forma, aquela função em questão não será feita, por exemplo, se no parâmetro d definirmos 'y' não será realizada uma diferenciação nos dados. Neste exemplo teríamos um modelo ARMA.

##

    **AR:** _Autoregression:_ Um modelo que usa a relação dependende entre uma observação e alguns lags.

    **I:** _Integrated:_ Uso de diferenciação nas observações brutas, exemplo: subtração do valor de uma observação com sua observação anterior. O objetivo é transformar a série temporal em estacionária.

    **MA:** _Moving Average:_ Um modelo que usa a dependência entre a observação e o erro residual a partir de um modelo de média móvel aplicado a lags.

    ```
    residual error = expected − predicted
    ```

    * Isso é diferente de Moving Average Smoothing.
    * Erros residuais contém estruturas temporais que podem ser modeladas.
    * Existem sinais complexos nos erros residuais.
    * Um modelo que prever o erro residual pode ser usado para ajustar os próximos erros e melhorar um modelo que aprende com o histórico.

##

O modelo arima contém alguns parâmetros
```
ARIMA(p,d,q)
```
* p: O número de lags que foram devem ser incluídos no modelo.
* d: O número de vezes que as observações serão diferenciadas.
* q: O tamanho de uma janela de média móvel. Também chamada de ordem de média móvel.
* 