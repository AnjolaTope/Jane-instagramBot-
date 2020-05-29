"""
Automate Instagram using python
"""

#this will allows us to automate the broswer to accomplish task we want it to 
from selenium import webdriver
#Allows us to do some folder manipulation and path manipulation
import os 
#To keep track of time
import time

class Bot:
#this is the constructor of this class that we use to log in to instagram
    def __init__(self,username,password):
        """
                Initialises an instance of the bit class 

                Calls the log in method to authenticate a user in IG

                Args 
                    username(str)--The instagream username
                    password(password))-- the instagram password
                
                Attributes
                    driver: selenium.webdriver.Chrome : The chrome driver used to automate web browser actions
        """
        #sets the username and password 
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        #this is where we will boot up browser when this class is called
        self.driver = webdriver.Chrome('./chromedriver.exe')

        #to login
        self.login()
         
    #to log in to instagram     
    def login(self):
        #this takes us to the intagram log in page
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        # this enables us to acees the username path on the browser and send our username to the browser
        time.sleep(2) 
        self.driver.find_element_by_name('username').send_keys(self.username)

        # this enables us to acees the password path on the browser and send our username to the browser
        time.sleep(2)
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        #this will allow us to click the log in bottun and automatically log in 
        #XPath (XML Path Language) is a query language for selecting nodes from an XML document. In addition, XPath may be used to compute values (e.g., strings, numbers, or Boolean values) from the content of an XML document. 
        time.sleep(2)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()


        time.sleep(2)

    def find_buttons(self, button_text):
        """
        Finds buttons for following and unfollowing users by filtering follow elements for buttons. Defaults to finding follow buttons.
        Args:
            button_text: Text that the desired button(s) has 
        """

        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))

        return buttons

    #this function will navigate to the  profile of the specific user 
    def nav_user(self,user):
        """
          Args user(str)--The instagream username

        """
        self.driver.get('{}/{}/'.format(self.base_url,user))

    #this will follow the user
    def follow_user(self,user,):
        """
          Args user(str)--The instagream username

        """
        self.nav_user(user)

        #to hit the follow button
        time.sleep(2)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
        print(follow_button)
        print("fhfjf")
        for btn in follow_button:
            time.sleep(2)
            btn.click()
       

    def unfollow_user(self, user):
        """
        Unfollows user(s)
        Args:
            user:str: Username of user to unfollow
        """

        self.nav_user(user)
        time.sleep(2)
        unfollow_btns = self.find_buttons('Following')
        time.sleep(2)

        if unfollow_btns:
            for btn in unfollow_btns:
                time.sleep(2)
                btn.click()
                time.sleep(2)
                unfollow_confirmation = self.find_buttons('Unfollow')[0]
                time.sleep(2)
                unfollow_confirmation.click()
                time.sleep(2)
        else:
            print('No {} buttons were found.'.format('Following'))



 

       

# if this file is called, imported or open, the code defined here will be what will be run
if __name__ == '__main__':
      ig_bot = Bot('anjie_babz_77' , "Anjiebabz743")
      ig_bot.nav_user('garyvee')
     # ig_bot.follow_user('brfootball')
      ig_bot.unfollow_user('brfootball')

      


    