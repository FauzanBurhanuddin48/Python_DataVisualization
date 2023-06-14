#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

dt = pd.read_csv("data bank.csv")

display(dt.head(10))


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv", delimiter = ',')

plt.scatter(data['marital'], data['balance'])

plt.xlabel('Marital')
plt.ylabel('Balance')

#save jpg
plt.savefig('scatter.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv")

plt.scatter(data['marital'], data['balance'], c=data['day'], s= data['campaign'])


plt.xlabel('Marital')
plt.ylabel('Balance')

#save jpg
plt.savefig('scatter2.jpg', dpi=300, bbox_inches='tight')

plt.colorbar()
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv", delimiter = ',')

plt.plot(data['balance'])
plt.plot(data['duration'])

plt.xlabel('Balance')
plt.ylabel('Duration')

#save jpg
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv", delimiter = ',')

plt.bar(data['education'], data['balance'])

plt.xlabel('Education')
plt.ylabel('Balance')

#save jpg
plt.savefig('barchart.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv", delimiter = ',')

plt.hist(data['age'])

#save jpg
plt.savefig('histogram.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv", delimiter = ',')

job = ['Admin','Technician','Management','Retired', 'Service']
data= [3,2,2,1,2]

plt.pie(data, labels=job)

#save jpg
plt.savefig('Piechart.jpg', dpi=300, bbox_inches='tight')

plt.title("Data Job")
plt.show()


# In[ ]:




