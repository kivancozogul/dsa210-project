
# Effect of 3 Point Shot Attempts on Total Game Score

## Project Overview

In this project, effect of the amount of three point shots taken during the game by evaluating average three point shots taken and average game scores throughout years also this project aims to see if positional 3 point shot attempts have an effect on total game.

### Motivation

This project's motivation is to conduct a research about NBA's 3 point revolution.There is a fact that games' scores are much higher than prior years and Center players are taking more 3 point shots comparing to 2010's.I would like to see that if this situation affects the games' total score.



### Datasets

The datas will be collected from NBA API Library and basketballreference.com.

In the project the collected datas will be:

- **Years in which the stats are trackable**
- **Average three pointer attempts per year for each team**
- **Average three pointer made per year for each team**
- **Average points per game for each team**
- **Average three pointer attempts by positions**

### Research Questions:
**Does the evolution of positional play correlate with higher total game scores over the last decade in NBA? (2010-2025)?**

**To what extent has the traditional definition of the "Center" position blurred into "Forward" roles due to the increase in shooting volume?**

**Do 3 point shot attempts have correlation with higher game scores between 2010-2025?**


## Hypothesis Testing

**Null Hypothesis ($H_0$):**
There is no statistically significant relationship between the increase in 3-point shot attempts by various positions and the total game scores recorded between 1980 and 2025.

**Alternative Hypothesis ($H_1$):**
There is a significant positive correlation between the volume of 3-point shots taken by non-guard positions and the total game scores, suggesting that the "positional revolution" has fundamentally inflated game outcomes over the decades.


Since **P-Score**<0.001 and Correlation Rate = 0.85, we can successfully reject the Null Hypothesis.


**Chi-Square Test** results with value of 314.23 between game score and 3 point shot attempts which is extremely high.This result is also enough to reject the Null Hypothesis.


## Machine Learning Results

**First Graph: Linear Regression Objective**

📈 Model Outputs and Interpretation

The trained model achieved an R^2 =0.69 success score on the test data. This value proves that 69% of the variation in game scores can be explained solely by the number of 3-pointers attempted.

The mathematical equation derived by the model is as follows:

**Score=83.56+(1.39×3-Point Attempts)**

Analytical Inference: The analysis reveals a strong positive correlation between the variables. The coefficient analysis deterministically indicates that every extra 3-point shot attempted by an NBA team contributes an average of +1.4 points to the total game score. This finding confirms that the score increase in the modern NBA is not coincidental, but rather a strategic choice based on the mathematics of the game (3 > 2).


**Second Graph: Random Forest Classifier Objective**

🤖 Model Performance and Confusion Matrix

Upon examining the model's "Feature Importance," it was observed that the most dominant factor determining a player's position is "3-Point Attempt Volume," with a weight of over 60%.

Analytical Inference: The Confusion Matrix indicates that the model struggles specifically when classifying players in the "Center" position.

Traditional Era (2010-2015): The model can label players with low shooting volume as "Center" with 95%+ accuracy.

Modern Era (2016-Present): As the shooting volume of Pivot players increased, the model began to incorrectly classify these players as "Forward" or "Guard."

Conclusion: This "error" is actually the strongest evidence supporting the project's hypothesis. Statistically, Centers have become indistinguishable from Guards in terms of shooting profiles. This proves that the era of "Positionless Basketball" has begun in the NBA and that the traditional definition of a pivot has lost its validity in the dataset.

📝 **General Conclusion**

The Machine Learning analyses performed have data-driven proof that 3-point shots have irreversibly changed not only the scoreboard but also player roles and the fundamental geometry of the game.
