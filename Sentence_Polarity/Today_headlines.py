# importing requests package 
import requests  
import pandas as pd
import datetime
import re

def NewsFromBBC(): 
    
    # BBC news api 
    main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=abbf89d492494a68860f2f22e154072f"

    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 

    # getting all articles in a string article 
    article = open_bbc_page["articles"]
    
    # empty list which will 
    # contain all trending news 
    results = [] 
    date = []
    correctDate = []
    headlines = []
    
    for ar in article: 
        results.append(ar["title"])
        date.append(ar["publishedAt"])
        
        
    for i in range(len(results)): 
        
        # printing all trending news 
        #print(i + 1, results[i])
        headlines.append(results[i])
        correctDate.append(date[i])
        correctDate[i] = ''.join(correctDate[i].split('T', 1)[0])[:-3]
        headlines[i] = headlines[i].split(' - ', 1)[0].encode("utf-8")
        headlines[i] = re.sub('[^\x00-\x7f]','', headlines[i])
        
        
        

    df = pd.DataFrame(headlines)
    dfDate = pd.DataFrame(correctDate)
    
    dataFrame = pd.concat([dfDate, df], axis=1)
    dataFrame.columns = ['Date', 'Title']
    print dataFrame
    
    dataFrame.to_csv("Today_Headlines.csv", sep=',', encoding='utf-8')
    
# Driver Code 
if __name__ == '__main__': 
    
    # function call 
    NewsFromBBC() 
