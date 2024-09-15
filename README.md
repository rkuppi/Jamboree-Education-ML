# Jamboree-Education
Jamboree has helped thousands of students like you make it to top colleges abroad. Be it GMAT, GRE or SAT, their unique problem-solving methods ensure maximum scores with minimum effort. They recently launched a feature where students/learners can come to their website and check their probability of getting into the IVY league college. This feature estimates the chances of graduate admission from an Indian perspective.

# Problem
Help Jamboree in understanding what factors are important in graduate admissions and how these factors are interrelated among themselves. It will also help predict one's chances of admission given the rest of the variables.

# EDA
- Univarient and bivarient analysis were performed to understand the data better and determine best features
- Determined factors that are important in graduate admissions

# Logistic Regression Model
- Implemented Logistic Regression model using slkearn, OLS method, best R-squared was found to be 0.83
- Stastical summary
  - R-squared of 0.817 suggests that the model explains 81.7% of the variance in the dependent variable.
  - F-statistic of 250.3 suggests that the model is highly statistically significant. It means that the independent variables in the model collectively explain a substantial amount of the variation in the dependent variable
  - Prob (F-statistic) of 2.27e-140 this confirms that the overall model is statistically significant at any conventional significance level (e.g., 0.05 or even 0.01)
  - Skew of -1.139 suggests that the residuals are negatively skewed, meaning that the left tail (smaller values)
  - Prob(JB): 2.51e-44 suggest that the null hypothesis of normally distributed residuals can be rejected. This suggests that the residuals are not normally distributed
  - Cond. No. of 5.86 is relatively low, indicating that multicollinearity is not a concern in your model. Generally, condition numbers above 30 might suggest multicollinearity, so this value is within a safe range.
- Verified the assumptions of Linear Regression
  - Linearity
  - Multi Collinear (VIF)
  - Normality of residuals
  - Homoscedasticity
- Model was packaged into a pickle object which will be used for the deployments

# Deployment
- Jamboree_app.py is used to take the realtime input from the user and predict the chance of getting an admit
- This was done using streamlit

# Recomendations
- SOP, LOR, University Rating methods are not doing well, improve the the quality of the measurements that are made
- Along with exam scores it would be good to take other performance measures like mock intertview, any relevant experience
- It would be good if we can collect the features like stream for which student is applying for as chance of admin will depend on it
- Greaduation year and university will also be a good featues to add
