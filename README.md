# [A Fine Windy Day: HackerEarth Machine Learning challenge](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-windmill-power/)
This was the challenge on Hackerearth and in this repository I have shared my approach towards this regression 
challenge.

## ABOUT THE CHALLENGE
<b>Problem statement</b>
<br>
<p>It is the year 2021 and we are at the verge of a massive climatic change. With global warming at its peak and fossil
 fuels inching towards its extinction, it is the need of the hour to step up and take responsibility for our planet
 . Developing countries all over the world are making a shift towards a cleaner energy source and are looking at ways
  to expand their global energy source power.</p> 

<p>Switching to renewable energy sources is a great way to reduce dependency on imported fuels and increase cost
 efficiency. It is time we move towards a low-carbon future by embracing solar, hydro, geothermal energy and so on
 , to protect mother nature.</p>

<p>An efficient energy source that has been gaining popularity around the world is wind turbines. Wind turbines
 generate power by capturing the kinetic energy of the wind. Factors such as temperature, wind direction, turbine
  status, weather, blade length, and so on influence the amount of power generated.</p>

<b>Task</b>

<p>You are appointed by an environmentalist for their Non Government Organization as a climate warrior who comes to the
 rescue. Your task is to build a sophisticated Machine Learning model that predicts the power that is generated (in
  KW/h) based on the various features provided in the dataset.</p>

<b>Dataset</b>

<p>The dataset consists of parameters such as the temperature, wind direction, turbine status, weather, blade length
, and the like. The dataset contains the records from Oct,2018 - Sept,2019</p>

## Results from EDA

### Data Distribution
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/DataDistribution.png"><br>

### Power Genration Across the Year
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Power%20Generation%20in%20each%20Trimonth.png"><br>
<b>Maximum Power is Generated in the months December to March</b>

### Max Power in Each Month
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Max%20Power%20Generated.png"><br>
<b>Max Power is generated is much higher in Nov to Feb than in any other month</b>

### Avg. Power Generated depending on the Cloud levels
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Avg%20Power%20Cloud%20Levels.png"><br>
<b>When Cloud Level is Low or Medium, the avg. power generated is much higher then, Extremely Low Cloud level</b>

### Relationship between Features and Targets
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Relationship%20between%20Features%20and%20Targets.png"><br>
<b>No Feature has a Linear Relationship with the target</b>

### Correlation Heatmap
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Correlation%20Heatmap.png"><br>

## Comparing Performance of Randm Forest, XGBoost and CatBoost
### R2-Scores

| Model| Train Score | Test Score |
| --- | ----------- | ----------- |
| Random Forest | 0.99 | 0.95 |
| XGBoost | 0.99 | 0.96 |
| CatBoost | 0.98 | 0.96 |

### Residual Analysis
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Residuals.png"><br>
<b>Random Forest's distribution of residuals is narrower compared to other model's residuals</b>

### Homoscedestic Test
<img src="https://github.com/Mohan-Gupta/A-Fine-windy-Day/blob/main/Plots/Homoscedestic.png"><br>
<b>All the models gave similar performance for the test set, where as for Random Forest on train set, had some noise 
towards the end.</b>

#### However, Catboost was not hypertuned for the given data it gave similar performance as hypertuned XGBoost.

<b> In the Notebooks you can find the code and detailed explanation of this project.</b>





