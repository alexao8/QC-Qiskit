#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries
from qiskit import *
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import *
from ibm_quantum_widgets import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[2]:


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)


# In[3]:


circuit.draw(output = 'mpl')


# In[4]:


circuit.h(qr[0])


# In[5]:


circuit.draw(output = 'mpl')


# In[6]:


circuit.cx(qr[0], qr[1])


# In[7]:


circuit.measure(qr,cr)


# In[8]:


circuit.draw(output = 'mpl')


# In[9]:


simulator = Aer.get_backend('qasm_simulator')


# In[10]:


result = execute(circuit, backend = simulator).result()


# In[11]:


plot_histogram(result.get_counts(circuit))


# In[12]:


provider = IBMQ.get_provider('ibm-q')


# In[14]:


qcomp = provider.get_backend('ibmq_16_melbourne')


# In[15]:


job = execute(circuit, backend = qcomp)


# In[ ]:


job_monitor(job)

