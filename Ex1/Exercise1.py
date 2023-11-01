#!/usr/bin/env python
# coding: utf-8

# In[44]:


import shutil
import os
import dfitspy
from matplotlib import pyplot as plt
import numpy as np


# In[2]:


from astropy.io import fits


# In[53]:


data, header = fits.getdata('m51.fits', header=True)

plt.imshow(data)
plt.imshow(data, vmin=0, vmax=200)

print(np.shape(data))
print('Data for area [200:220, 200:220]')
print('Mean=', np.mean(data[200:220, 200:220]), 'std=', np.std(
    data[200:220, 200:220]), 'median=', np.median(data[200:220, 200:220]))
print('Min=', np.min(data[200:220, 200:220]),
      'Max=', np.max(data[200:220, 200:220]))
print('\n')

print('Data for area [300:320, 300:320]')
print('Mean=', np.mean(data[300:320, 300:320]), 'std=', np.std(
    data[300:320, 300:320]), 'median=', np.median(data[300:320, 300:320]))
print('Min=', np.min(data[300:320, 300:320]),
      'Max=', np.max(data[300:320, 300:320]))
print('\n')

print('Data for area [350:370, 350:370]')
print('Mean=', np.mean(data[350:370, 350:370]), 'std=', np.std(
    data[350:370, 350:370]), 'median=', np.median(data[350:370, 350:370]))
print('Min=', np.min(data[350:370, 350:370]),
      'Max=', np.max(data[350:370, 350:370]))
print('\n')

print('Data for area [250:270, 120:140]')
print('Mean=', np.mean(data[250:270, 120:140]), 'std=', np.std(
    data[250:270, 120:140]), 'median=', np.median(data[250:270, 120:140]))
print('Min=', np.min(data[250:270, 120:140]),
      'Max=', np.max(data[250:270, 120:140]))
print('\n')

print('Data for area [100:120, 430:450]')
print('Mean=', np.mean(data[100:120, 430:450]), 'std=', np.std(
    data[100:120, 430:450]), 'median=', np.median(data[100:120, 430:450]))
print('Min=', np.min(data[100:120, 430:450]),
      'Max=', np.max(data[100:120, 430:450]))


# Pixel density remains the same - in my case it's always `20*20` pixels

# In[4]:


print(header)


# In[64]:


print(np.where(data <= 0))
print(data[3, 76])


# In[5]:

print('A----------------------------------------------------------')

datapath = 'M67/CALIB/'
listfiles = dfitspy.get_files(['all'], dire=datapath)
listkeys = ['OBJECT', 'NAXIS1', 'NAXIS2']

listbias = dfitspy.dfitsort(listfiles, listkeys, grepping=['BIAS'])
dfitspy.dfitsort_view(listbias)


# In[6]:


dpath = 'M67/SCIENCE/'
files = dfitspy.get_files(['all'], dire=dpath)
lkeys = ['OBJECT', 'NAXIS1', 'NAXIS2', 'EXPTIME', 'CDELT1', 'CDELT2']
print('B----------------------------------------------------------')
lbias = dfitspy.dfitsort(files, lkeys, grepping=None)

dfitspy.dfitsort_view(lbias)


# In[7]:


datapath = 'M67/CALIB/'
listfiles = dfitspy.get_files(['all'], dire=datapath)
listkeys = ['OBJECT', 'NAXIS1', 'NAXIS2', 'EXPTIME', 'CDELT1', 'CDELT2']
print('C----------------------------------------------------------')
listbias = dfitspy.dfitsort(listfiles, listkeys, grepping=[
                            'BIAS', '1030', '1030', '2', '2'])

dfitspy.dfitsort_view(listbias)


# In[8]:


result = listbias.items()

data = list(result)

arr = np.array(data)[:, 0].reshape(40, 1)
arra = str(arr).replace('[', '')
array = str(arra).replace(']', '')
array2 = str(array).replace("'", "")
array3 = str(array2).replace(" ", "")

ar = np.char.strip(str(array3), chars=None)

with open('bias.txt', 'w') as fp:
    fp.write(str(ar))


# In[9]:


aba = np.loadtxt('bias.txt', dtype=str)


# In[10]:


for i in range(len(aba)):
    for j in range(len(listfiles)):
        if listfiles[j] == 'M67/CALIB/'+aba[i]:
            shutil.copy2(listfiles[j], 'biasmappe/')


# In[11]:


# In[12]:


dpath = 'biasmappe/'
listfes = dfitspy.get_files(['all'], dire=dpath)


# In[13]:


print(listfes[1])


# In[34]:


meen = []
std = []
for i in range(len(listfes)):
    data, header = fits.getdata(listfes[i], header=True)

    plt.imshow(data)
    plt.imshow(data, vmin=0, vmax=300)
    plt.title(listfes[i])
    plt.show()
    men = np.mean(data[300:330, 300:330])
    st = np.std(data[300:330, 300:330])

    meen.append(men)
    std.append(st)

    print(np.mean(data[300:330, 300:330]))
    print(np.std(data[300:330, 300:330]))


# `EFOSC.2000-12-28T22:11:19.687.fitsEFOSC.2000-12-28T22:11:19.687.fits` deviate a lot from the other measurements with `np.mean = 162.83` and `np.std = 251.85`- I believe it's due to a star in the measured area.
#
# Changing the position of the box I'm looking at, and away from the star, all measurements yield the approximate values of `np.mean = 150` and `np.std = 7`.

# In[39]:


print(np.mean(meen), np.std(meen))
print(np.mean(std), np.std(std))


# Doing the "math" the mean value of the mean values are `148` with std `1.45`
# The mean value of the std values are `7.14`with std `0.19`
#
# By choosing a larger area we're more likely to include a star in our calculations, which make the values differ a lot. Choosing a smaller area makes it easier to compare how the different FITS files describe "darkness".

# In[ ]:
