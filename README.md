# Prophet-Stock-Prediction 📈

Stock prediction web app made with [streamlit](https://streamlit.io/) and [fbprophet](https://facebook.github.io/prophet/)



https://user-images.githubusercontent.com/55437218/129449805-99b7b36c-128f-4b2d-ad7c-ace1e632c03b.mp4


(Note : Listed stocks are top 30 stocks taken from https://in.finance.yahoo.com/quote/%5ENSEI/components/ )


## Want to check live demo ❔
[click here](https://share.streamlit.io/pathikg/prophet-stock-prediction/main)

## Features to be added 🤔 : 
* Forecasting with ARIMA
* Forecasting with Deep Learning using LSTM

## Installation :

* create and activate a virtual environment 
```
$ python -m venv venv
$ .\venv\scripts\activate
```

* Inside Virtual Environment
```
(venv) $ git clone https://github.com/pathikg/Prophet-Stock-Prediction.git
(venv) $ cd Prophet-Stock-Prediction
(venv) $ pip install -r requirements.txt
(venv) $ streamlit run steamlit_app.py
```

* if requirements.txt doesn't work (this happened with me for fbprophet)
* 
Try :
```
conda remove pystan fbprophet
conda install pystan=2.19.0.0
conda install -c conda-forge fbprophet=0.6.0
```


References :
* https://www.youtube.com/watch?v=0E_31WqVzCY&t=351s
* https://www.youtube.com/watch?v=ng2o98k983k
* https://streamlit.io/sharing

(Note : I am NOT a SEBI registered advisor or a financial adviser. Any of my investment or trade advise I share are provided for educational purposes only and do not constitute specific financial, trading or investment advice.)
