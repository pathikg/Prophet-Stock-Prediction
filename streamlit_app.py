import streamlit as st
from datetime import date
from webscrap import GetTicker

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# conda remove pystan fbprophet
# conda install pystan=2.19.0.0
# conda install -c conda-forge fbprophet=0.6.0
# if requirements.txt doesn' t work
START = "2017-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App using Prophet model')

url = "https://in.finance.yahoo.com/quote/%5ENSEI/components/"
tickerObj = GetTicker(url)
tickers = tickerObj.get_tickers()
selected_stock = st.selectbox('Select dataset for prediction', tickers)

# tickers = ('RELIANCE.NS', 'WIPRO.NS', 'INFY.NS', 'TATAPOWER.NS', 'TCS.NS')
# html_string = '<p style="font-size:0.8rem">top 30 stocks as per the <a href= "https://in.finance.yahoo.com/quote/%5ENSEI/components/" style="text-decoration:none"; target="_blank"> yahoo finance</a></p>'	
# st.markdown(html_string, unsafe_allow_html=True)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")
    return data

	
# data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
# data_load_state.text('Loading data... done!')

st.subheader('Latest data')
st.write(data.tail().iloc[::-1])

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Open price"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close price"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
		
plot_raw_data()

n_years = st.slider('Years of prediction:', 1, 5)
period = n_years * 365

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# just taking date, forcast and its lower and upper bounds
results = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
results.columns = ['Date', 'forecast', 'lower Bound', 'upper bound']
results["Date"] = results["Date"].dt.strftime("%Y-%m-%d")


# Show and plot forecast
st.subheader('Forecast data')
st.write(results.tail().iloc[::-1])
    
if n_years == 1 :
	st.subheader(f'Forecast plot for {n_years} year')	
else :
	st.subheader(f'Forecast plot for {n_years} years')	
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


html_string = '<p style="font-size:1rem">made with ❤ by <a href= "https://github.com/Patrickbro13" style="text-decoration:none"; target="_blank">Pathik Ghugare</a></p>'	
st.markdown(html_string, unsafe_allow_html=True)
