# Web scraping of Kalimati data using Selenium
Data Sources: 
1. ```https://kalimatimarket.gov.np/daily-arrivals``` 
2. ```https://kalimatimarket.gov.np/price```



## Setup 
### 1. Install Web Driver for your browser. 
https://googlechromelabs.github.io/chrome-for-testing/
### 2. Extract the zip file and store the exe file `chromedriver.exe` in an appropriate location on your disk. 

### 3. Install Selenium using pip 
```
pip install selenium==3.141.0
```
### 4. Modify the PATH as per the path of your webdriver

```
PATH = "D:\\chromium\\chromedriver"
driver = webdriver.Chrome(PATH)
```
### 5. Specify desired date range

```
start_date = '2024-01-01'
end_date = '2024-06-16'
```

### 6. Run the script 
```
python .\selenium_script.py 
python .\daily-price.py 
```