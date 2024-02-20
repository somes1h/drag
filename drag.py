import matplotlib.pyplot as plt
import math as mt
import numpy as np
import streamlit as st

D = st.number_input("enter the drag force")
m = st.number_input("enter the mass")
g = 9.8
#V0 = 0
"""Y0 = 0
Y = [Y0]"""
Y=[0]
t1=0
t2=10
n = 10000
h = (t2-t1)/n

t = [t1]
Vy = [0]
def f1(v):
    value =g-(D/m)*v**2
    return value
i = 0
while i<=n:
    t.append(t[i]+h)
    Vy.append(Vy[i]+h*f1(Vy[i]))
    i+=1
plt.plot(t,Vy)
plt.savefig('graph.jpg')
st.image('graph.jpg')