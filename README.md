# Ehsan Data science project

## Team Members

* Hamad Alruways
* Kawther al jubran
* Suliman alghanmi
* Sultan

## Introduction

Driven by a keen interest in understanding the projects of the Ehsan platform, particularly during the heightened charitable activity of Ramadan, our team embarked on a data analysis data available in their website , uncover key insights about these projects, buld ML model that help to make prediction about  some charctersitc of these project.

## Dataset Synopsis and Origin

To achieve our objectives, we utilized web scraping to collect data directly from the Ehsan website. Our dataset comprises detailed information on each project, including:

* Case Number
* Project Names
* Amount
* Date
* Beneficiaries
* Beneficiary Type
* Number of Donations
* Partner
* Details URL



## Methodology

Our analysis involved a structured approach, encompassing feature engineering, model selection, and hyperparameter optimization.

*Feature Engineering:*

* We create new feature 'Project Month,' to enhance our analysis of temporal trends.
* Categorical features were transformed using label encoding to facilitate their integration into our models.

*Model Selection:*

* For cluster analysis, we explored both K-means and DBSCAN algorithms.
* We trained two K-means models and two DBSCAN models, evaluating their performance using the silhouette average score to select the optimal models.

*Hyperparameter Optimization:*

* Hyperparameter optimization was crucial for maximizing model performance.
* For K-means, we systematically tested various 'k' values and 'max_iter' values.
* For DBSCAN, we experimented with different 'epsilon' and 'minimum samples' values.
* Our final model selections were based on achieving the highest silhouette average score, ensuring robust and reliable clustering results.

## Performance Metrics

Performance was primarily assessed using the silhouette average score, which provided a measure of cluster cohesion and separation
*
