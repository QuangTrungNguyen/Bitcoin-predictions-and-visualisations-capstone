# Bitcoin-predictions-and-visualisations-capstone

This project analyses the time-series of Bitcoin process and macro-economic factors that influence Bitcoin Price using data from 2011 to 2018. The datasets contain Bitcoin trading data (high,low,open,close,volume,marketcap) and 33 other features inlcluding Bitcoin technical data, Sentiment (Google Trends), Currency exchange rates, Commodity Prices.

Relevant features are then then applied to train and compare the performance of the 14 models on predicting the latest Bitcoin Price in 2018 using Python libraries: 

Machine Learning (Scikit-learn, XGBoost): 
* Linear: Linear Regression, Lasso, Ridge, Bayesian Ridge, ElasticNet
* Non-linear: KNN, Support Vector Regression
* Tree-based: Gradient Boosting Trees, Extremely Randomised Trees, Decision Trees

Deep Learning (Keras): 
* Recurrent Neural Networks: LSTM, GRU 
* Multilayer Perceptron Network
    
Time-Series (Statsmodels): 
* Autoregressive Integrated Moving Average model 
    
Visualisations for predicted Bitcoin Price and model comparison were developed using Python's plotly, D3.js, Tableu and deployed to Amazon Web Service S3 Buckets at https://s3-ap-southeast-2.amazonaws.com/capstone-bitcoin/prices/index.html#actualprice
