#!/usr/bin/env python
# coding: utf-8

# In[24]:


import plotly
plotly.__version__
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
import numpy as np
import math
from operator import add
import functools
from random import random, randint
random()


# In[25]:


import random


# In[46]:


nodes = 15


# In[47]:


x = [random.randint(0,100) for x in range(nodes)]
y = [random.randint(0,100) for x in range(nodes)]


# In[48]:


print(x)
print(y)


# In[49]:


trace = go.Scatter(
    x = x,
    y = y,
    mode = 'markers'
)


# In[50]:


data = [trace]


# In[51]:


plotly.offline.iplot(data)


# In[52]:


for i in range(len(x)):
  print((x[i], y[i], i))


# In[53]:


from itertools import combinations, permutations


# In[54]:


def individual():
  return random.sample(range(0, nodes), nodes)

ind = individual()


# In[55]:


def plotind(order):
  x_m = [x[i] for i in order]
  y_m = [y[i] for i in order]
  
  x_m.append(x[order[0]])
  y_m.append(y[order[0]])
  
  trace = go.Scatter(
    x = x_m,
    y = y_m
  )
  return iplot([trace])


plotind(ind)


# In[56]:


# Fitmess Function
def fitness(order):
#   print(order)
  distance = []
  x_m = [x[i] for i in order]
  y_m = [y[i] for i in order]
  for i in range(len(order)-1):
#     print(order[i], order[i+1])
    li = math.sqrt(math.pow((x_m[i+1] - x_m[i]), 2) + math.pow((y_m[i+1] - y_m[i]), 2))
    distance.append(int(li))
  return sum(distance)

fitness(ind)


# In[57]:


def population(length):
  return [individual() for i in range(length)]

pop1 = population(10*nodes)


# In[58]:


def grade(pop):
  summed = sum([fitness(x) for x in pop])
  return summed / len(pop)
grade(pop1)


# In[59]:


# Evolution of GA

def evolve(pop, retain=0.2, random_select=0.5, mutate=0.01):
  graded = [(fitness(x), x) for x in pop]
  graded = [ x[1] for x in sorted(graded)]
  retain_length = int(len(graded) * retain)
  parents = graded[:retain_length]
  
  #  Randomly add other individuals to promote genetic diversity
  for individual in graded[retain_length:]:
    if random_select > random.random():
      parents.append(individual)

  #  Mutate some individual
  for individual in parents:
    if mutate > random.random():
      pos_to_mutate = randint(1, len(individual)-1)
      x = individual[pos_to_mutate]
      individual[pos_to_mutate] = individual[0]
      individual[0] = x
      
      
  #  Crossover parents to create children
  parents_length = len(parents)
  desired_length = len(pop) - parents_length
  children = []
  
  
  while len(children) < desired_length:
    male = randint(0, parents_length-1)
    female = randint(0, parents_length-1)
    if male != female:
      male = parents[male]
      female = parents[female]
      half = int(len(male)/2)
      vals = male[half:]
      ch1 = []
      ch2 = []
      for x in female:
        if x in vals:
          ch1.append(x)
        elif x not in vals:
          ch2.append(x)
      child = ch1 + ch2
      children.append(child)
      
  parents.extend(children)
  return parents


# In[60]:


fitness_history = [grade(pop1)]


# In[61]:


fitness_history


# In[62]:


for i in range(0, nodes*20):
  pop1 = evolve(pop1)
  fitness_history.append(grade(pop1))


# In[63]:


fitness_history


# In[64]:


best = pop1[0]
for i in pop1:
  if fitness(i) < fitness(best):
    best = i
best


# In[65]:


fitness(best)


# In[66]:


plotind(best)


# In[ ]:




