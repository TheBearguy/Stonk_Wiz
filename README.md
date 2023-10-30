<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Stock Data Visualization with MongoDB 📈</h1>
    <p>This repository contains a Python script to fetch stock data from an API and store it in a MongoDB database.<br>Additionally, it includes Jupyter Notebook files for data analysis and visualization, which will help you explore and understand the stock market trends.</p>
    <h2>📌 Pre-requisites</h2>
    <ul>
        <li> Python 3</li>
        <li> Jupyter Notebook</li>
        <li> MongoDB</li>
    </ul>
    <p>You can install Python packages using <code>pip</code>:</p>
    <pre>
pip install -r requirements.txt
    </pre>
    <h2>Getting Started✨</h2>
    <ol>
        <li>Clone the repository to your local machine:</li>
    </ol>
    <pre>
git clone https://github.com/yourusername/stock-data-visualization.git
cd stock-data-visualization
    </pre>
    <ol start="2">
        <li>Create a MongoDB database to store the stock data. Make sure to update the MongoDB connection settings in the script if necessary.</li>
        <li>Run the Python script <code>fetch_stock_data.py</code> to fetch stock data from the API and store it in the MongoDB database:</li>
    </ol>
    <pre>
python fetch_stock_data.py
    </pre>
    <h2>Data Visualization 📊</h2>
    <ul>
        <li><strong>Line charts to track stock prices over time : </strong></li>
        <ul>
            <li>This chart shows the opening, closing, high, and low prices of a stock over a period of time.</li> 
            <li>It can be used to identify trends in the stock market.</li> 
        </ul>
        <li><strong>Candlestick charts for a detailed view of stock price movements : </strong></li>
        <ul>
            <li>This chart is similar to a line chart, but it also includes information about the volume of stock traded during each period.</li> 
            <li>Candlestick charts are often used by technical analysts to identify patterns in stock price movements.</li> 
        </ul>
        <li><strong>Moving averages to identify trends : </strong></li>
        <ul>
            <li>A moving average is a line that is plotted on a stock chart to show the average price of the stock over a period of time.</li> 
            <li>It can be used to identify trends in the stock market and to generate buy and sell signals.</li> 
        </ul>
        <li><strong>Volume analysis to determine trading activity : </strong></li>
        <ul>
            <li>Volume analysis is the study of the volume of stock traded during a period of time.</li> 
            <li>It can be used to identify trading activity and to predict future stock price movements.</li> 
        </ul>
    </ul>
    <p>Feel free to modify and customize these visualizations to suit your needs.</p>
    <h2>📌 Links to other resources</h2>
    <p>If you would like to deep dive more, please refer these resources :</p>
    <ul>
        <li>A Beginner's Guide to Stock Data Analysis-->https://www.investopedia.com/articles/07/stock-data-analysis.asp</li>
        <li>Stock Data Visualization with Python-->https://www.packtpub.com/product/stock-data-visualization-with-python/9781789801747</li>
        <li>Jupyter Notebook Tutorial-->https://jupyter.org/tutorial/</li>
        <li>Magic of Matplotlib-->https://matplotlib.org/stable/contents.html</li>
        <li>NumPy - an essesntial Tool-->https://numpy.org/doc/stable/</li>
    </ul>
    <h2>Contributing 🚀</h2>
    <p>If you would like to contribute to this project, please follow these steps:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch for your changes: <code>git checkout -b feature/your-feature</code>.</li>
        <li>Commit your changes: <code>git commit -m 'Add your feature'</code>.</li>
        <li>Push the branch to your fork: <code>git push origin feature/your-feature</code>.</li>
        <li>Create a pull request.</li>
    </ol>
    <p><strong>Happy Stock Data Analysis and Visualization!🤗</strong></p>
</body>
</html>
