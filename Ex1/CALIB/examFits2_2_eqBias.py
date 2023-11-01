import dfitspy

dataList = dfitspy.get_files(['all'])
keys = ['NAXIS1', 'NAXIS2', 'CDELT1', 'CDELT2']
grep = ['2.0', '2.0', '1030', '1030']
fits = dfitspy.dfitsort(dataList, keys, grepping=grep, exact=False)
print(len(fits), ' lines')
dfitspy.dfitsort_view(fits)
print('\n')

# ------- write a list of filenames
print('the list of the file names: ')
# resultList = open("bias.list", 'x')
resultList = open("bias.list", 'w')
for filename, values in fits.items():
    resultList.write('%s' % filename)
    resultList.write('\n')
# print(fits.keys())

resultList.close()

resultList = open("bias.list", 'r')
print(resultList.read())
resultList.close()


