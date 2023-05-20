import numpy as np
import pandas as pd

cars = {
    'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus'],
    'Price': [22000, 25000, 27000]
}

df = pd.DataFrame(cars, columns=['Brand', 'Price'])

print(df)
