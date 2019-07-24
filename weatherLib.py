# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json, smtplib 

def kelToFar(temp):
    temp = temp - 273
    temp = (9/5)*temp
    temp += 32
    return temp

def weatherReport():

    #Api key
    api_key = "88725df365be113ce47eaf534f5089c3"
      
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?" 
     
    # complete url address
    complete_url = base_url + 'zip=48104,us&appid=' + api_key 
      
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
      
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
      
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
      
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
      
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
      
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
      
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
      
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
      
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"]

        temp = kelToFar(current_temperature)
        temp = round(temp, 2)

        information = ''
        
        
      
        # print following values 
        information = "  Temperature (in fahrenheit unit) = " + str(temp)
        information +=  "\n\n  atmospheric pressure (in hPa unit) = " + str(current_pressure)
        information += "\n\n  humidity (in percentage) = " + str(current_humidiy)
        information += "\n\n  description = " + str(weather_description)
        
        return information  
    else: 
        return " City Not Found "
