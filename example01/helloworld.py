import pandas as pd

airquality = pd.read_excel("C:/Users/neoju/Documents/Python/example01/airquality.xlsx")

df = pd.DataFrame(airquality, columns = ['Ozone', 'Solar.R', 'Wind', 'Temp'])
df