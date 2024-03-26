import matplotlib.pyplot as plt
import csv
import seaborn as sns

f = open('EMP.csv', 'r')
job = []
data = f.readline()

while data:
    data = f.readline()
    if not data:
        break
    job.append(data.split(',')[2])

jobname = list(set(job))
cnt = [job.count(i) for i in jobname]

print('jobname:', jobname)
print('cnt:', cnt)

plt.pie(cnt, labels=jobname, autopct='%.1f%%')
plt.show()
"""
iris=sns.load_dataset('iris')

setosa=iris[iris['species']=='setosa']['sepal_length']
virginica=iris[iris['species']=='virginica']['sepal_length']
versicolor=iris[iris['species']=='versicolor']['sepal_length']

data=[setosa,virginica,versicolor]
name=['setosa','virginica','versicolor']

plt.boxplot(data,labels=name)
plt.show()
"""
