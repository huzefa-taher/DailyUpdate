import smtplib

#sends the email with information as content
def sendReport(information):

    #email information
    fromEmail = ''
    fromPass = ''
    toEmail = ''

    server = 'smtp.gmail.com'

    #creating message
    header = 'To: Good Morning!\nFrom: Daily Update\n' + 'Subject: Daily Update\n'

    message = header + '\n' + information + '\n'

    #sending email
    try:
        SERVER = smtplib.SMTP(server, 587)
        SERVER.ehlo()
        SERVER.starttls()
        SERVER.login(fromEmail, fromPass)
        SERVER.sendmail(fromEmail, toEmail, message)
    except Exception as e:
        print(e)
    finally:
        SERVER.quit()

#external libraries
import weatherLib as weather
import newsLib as news
import greetingsLib as greetings

spacer = '---------------------------------------------\n\n'

#creating content for email
content = 'Current Weather in Ann Arbor:\n' + weather.weatherReport()+ '\n\n' + spacer
content += 'Current World News:\n' + news.NewsFromBBC() + spacer
content += greetings.Goodbye()

# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    print(content)
    sendReport(content)
    print('Done')

