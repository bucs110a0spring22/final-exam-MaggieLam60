import requests
from pprint import pprint

class NewsData:
  def __init__(self):
    '''
    desc: initializes the program
    arg= self
    return= none
    '''
    self.results= results
    
  def __str__():
    '''
    desc: finds the link to the api, then prints out the resulting news articles
    arg= none
    return= none
    '''

    api_url = "https://newsdata.io/api/1/news?"


    question = input("Want Current News?(yes/no): ")
    if question == "yes":
      params = {
        
        'apikey': 'pub_744498d05bb68985cbffce8aeb2f7ebdaff3', 
        'country': 'us',
        'category': 'top',
        'language': 'en'
        }
    
      res = requests.get(api_url, params=params)
      
      data = res.json()
      #pprint(data)
      #results= data["results"]
      
      title = data['results'][0]['title']
      creator= data['results'][0]['creator']
      keywords= data['results'][0]['keywords']
      desc= data['results'][0]['description']
      cont= data['results'][0]['content']
      link = data['results'][0]['link']
    
      print('')
      print('')
      print('')
      print('┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑')
      print("         Current News")
      print('└────────────────────────────┘')
      print('')
      print("TITLE")
      print(title)
      print("")
      
      print("Link: ",link)
      print("KEYWORDS: ",keywords)
      print("Creator: ",creator)
      print("Description: ",desc)
      print('')
      print("FULL CONTENT")
      print("")
      print(cont)

          
      
      print ("") 
    elif question == "no":
      print("Choose yes next time")