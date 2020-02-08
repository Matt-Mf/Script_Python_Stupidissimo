# Convertitore di valute internazionali

EUR_to_GBP = 0.88   #Tasso odierno da Euro a sterlina
EUR_to_USD = 1.16    #Tasso odierno da Euro a dollaro
EUR_to_JPY = 132.4   #Tasso odierno da Euro a yen
EUR_to_INR = 75.5   #Tasso odierno da Euro a rupia indiana

GBP_sign = '\u00A3'
EUR_sign = '\u20AC'
JPY_sign = '\u00A5'
INR_sign = '\u20B9'
USD_sign = '\u0024'

euri = input('Inserisci il valore in Euro da convertire: ') # Gli Euro da convertire
e = float(euri)

pounds = e * EUR_to_GBP  #Calcoli di conversione
dollars = e * EUR_to_USD
yen = e * EUR_to_JPY
rupees = e * EUR_to_INR

print('Oggi, €' + str(e)) #Stampa i risultati
print('valgono ' + GBP_sign + str(pounds))
print('valgono ' + JPY_sign + str(yen))
print('valgono ' + INR_sign + str(rupees))
print('valgono ' + USD_sign + str(dollars))

input('Premere un tasto per chiudere la finestra')