import pandas as pd   #panda as pd is standard

my_dataset = {
  'stocks': ['Tesla', 'Nvidia', 'Rheinmetall'],
  'price': [312, 145, 120]
}

my_var = pd.DataFrame(my_dataset)

print(my_var)
