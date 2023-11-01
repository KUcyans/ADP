import dfitspy

dataList = dfitspy.get_files(['all'])
keys = ['OBJECT', 'NAXIS1', 'NAXIS2']
fits = dfitspy.dfitsort(dataList, keys, grepping=['BIAS'])
print(len(fits), ' lines')
dfitspy.dfitsort_view(fits)
