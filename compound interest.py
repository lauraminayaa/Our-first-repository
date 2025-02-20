#El usuario decide el intial principle (la inversion)
def calculatereturn(rate = 0, time = 0):
   principle = 1000

   gain = principle * pow((1 + rate / 100), time) - principle
   print(f"Principle: {principle} rate: {rate} Balance after {time} year/s: ${gain:.2f}")
calculatereturn(rate = 2, time = 10)
calculatereturn(rate = 2, time = 20)
calculatereturn(rate = 2, time = 40)
calculatereturn(rate = 10, time = 10)
calculatereturn(rate = 10, time = 20)
calculatereturn(rate = 10, time = 40)
calculatereturn(rate = 20, time = 20)
calculatereturn(rate = 20, time = 40)
#Bank 2: Stock market
calculatereturn(rate = 20, time = 1)


