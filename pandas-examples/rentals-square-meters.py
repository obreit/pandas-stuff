# add another column to your dataframe that represents the "square meter rent" for each apartment
# rentals['Rent'] / rentals['Space'] 
# --> here you divide each value from the 'Rent' column with the corresponding value of the 'Space' column
# --> this gives you back a 'Series' object
# the .round() function then basically just rounds each number in the series to the decimal places you specify 
rentals['m2_rent'] = (rentals['Rent'] / rentals['Space']).round(decimals=2)

# create groups for each region
region_groups = rentals.groupby(['Region'])

# compute the average square meter rent for each region 
# the reset_index() is not necessary but good practice to "flatten" your dataframe 
square_meter_avg_rent = region_groups[['m2_rent']].mean().reset_index().sort_values(by=['m2_rent'])
print(square_meter_avg_rent)

# compute the average absolut rent for each region
absolute_avg_rent = region_groups[['Rent']].mean().reset_index().sort_values(by=['Rent'])
print(absolute_avg_rent)

# notice the differences!

# a bit more fancy stuff. notice that both average computations are very similar. 
# you can think of a small helper function that will make it easier to compute this "repeated" computation
def sorted_mean(grouped_dataframe, column, ascending=True):
  return grouped_dataframe[[column]].mean().reset_index().sort_values(by=[column], ascending=ascending)

# you can then call it like this (it does the same as before, just a bit simpler)
# if you want the output from highest to lowest you can pass ascending=False
square_meter_avg_rent = sorted_mean(region_groups, 'm2_rent')
absolute_avg_rent = sorted_mean(region_groups, 'Rent')
print(square_meter_avg_rent)
print(absolute_avg_rent)

# to see the differences a bit clearer, it would be nice to combine the 2 dataframes
# while keeping the original "order" of the rows (so just a row-by-row merge). 
# result would be sth like
# Region_absolute, Rent, Region_m2, m2_rent
# Wedding, 847.13, Köpenick, 15.63
# ...
# but i haven't found a trivial way to do that