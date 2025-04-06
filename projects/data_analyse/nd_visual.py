from normal_distribution import N_D
import matplotlib.pyplot as plt
import plotly.express as px

nd = N_D(20,20000)
nd.fill_walk()
i = -20
x_value=[]
y_value=[]
while i < 21:
    x_value.append(i)
    j = nd.result.count(i)
    y_value.append(j)
    i += 1
plt.style.use('classic')
fig = px.bar(x=x_value,y=y_value)
fig.show()
print(x_value)
print(y_value)