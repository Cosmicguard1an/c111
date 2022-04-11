import csv
import plotly.figure_factory as ff   
import pandas as pd 
import random
import statistics
import plotly.graph_objects as go  

df = pd.read_csv('mathScore3.csv')
data = df['Math_score'].tolist()
# fig = ff.create_distplot([data],['Math Score'],show_hist = False)
# fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print('Mean of pop is:',mean,'St Dev of pop is:',stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    #show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation = statistics.stdev(mean_list)
print("Standard deviation of sampling distribution:- ", std_deviation)

# fig = ff.create_distplot([mean_list], ["Studnet marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.2], mode="lines", name="MEAN"))
# fig.show()

#standard_deviation()
setup()

stDev1_start, stDev1_end = mean - std_deviation, mean + std_deviation
stDev2_start, stDev2_end = mean - (2*std_deviation), mean + (2*std_deviation)
stDev3_start, stDev3_end = mean - (3*std_deviation), mean + (3*std_deviation)

print('Std dev 1:',stDev1_start,stDev1_end)
print('Std dev 2:',stDev2_start,stDev2_end)
print('Std dev 3:',stDev3_start,stDev3_end)

fig = ff.create_distplot([mean_list], ["Student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[stDev1_start,stDev1_start], y=[0,0.17],mode='lines',name="Standad Dev 1 start"))
fig.add_trace(go.Scatter(x=[stDev1_end,stDev1_end], y=[0,0.17],mode='lines',name="Standad Dev 1 end "))

fig.add_trace(go.Scatter(x=[stDev2_start,stDev2_start], y=[0,0.17],mode='lines',name="Standad Dev 2 start"))
fig.add_trace(go.Scatter(x=[stDev2_end,stDev2_end], y=[0,0.17],mode='lines',name="Standad Dev 2 end "))

fig.add_trace(go.Scatter(x=[stDev3_start,stDev3_start], y=[0,0.17],mode='lines',name="Standad Dev 3 start"))
fig.add_trace(go.Scatter(x=[stDev3_end,stDev3_end], y=[0,0.17],mode='lines',name="Standad Dev 3 end "))


fig.show()


