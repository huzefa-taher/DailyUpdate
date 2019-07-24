# importing requests package 
import requests      

key = '771bfa3cc61d4f8d9906b7233ac0694a'

def NewsFromBBC(): 

    content = ''
    
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=771bfa3cc61d4f8d9906b7233ac0694a"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        #print(i + 1, results[i])
        content += (str(i + 1) + ' ' + str(results[i]) + '\n\n')

    return content


