import instaloader
import pywhatkit

class Insta_info:

    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.loader.context,self.username)


    def Login(self):
        login = self.loader.load_session_from_file(self.username)
        return login

    #followers list
    def get_my_followers(self):

        for followers in self.profile.get_followers():
            with open("followers.txt","a+") as f:
                file = f.write(followers.username+'\n')

    #followees list
    def get_my_followees(self):
    
        for followees in self.profile.get_followees():
            with open("followees.txt","a+") as f:
                file = f.write(followees.username+'\n')

    #unfollowers list
    def get_my_unfollowers(self):
    
        followers_file = set(open("followers.txt").readlines())
        followees_file = set(open("followees.txt").readlines())

        unfollowers_set = followees_file.difference(followers_file)
            
        for unfollowers in unfollowers_set:
            with open("unfollowers.txt","a+") as f:
                file = f.write(unfollowers)

    #mutual friends list
    def get_my_mutual_friends(self):

        followers_file = set(open("followers.txt").readlines())
        followees_file = set(open("followees.txt").readlines())

        mutual_set = followees_file.intersection(followers_file)

        for mutuals in mutual_set:
            with open("mutualfollowers.txt","a+") as f:
                file = f.write(mutuals)


insta_info = Insta_info("insta_username")
insta_info.Login()

# send whatsapp msg with list of unfollowers at 13:36
def send_whatsapp_msg():
    #country code for india +91
    num = '+91'+str(int(input("Enter Whatsapp Number")))

    list_of_unfollowers = open("unfollowers.txt","r+")
    names = list_of_unfollowers.read()
    list_of_unfollowers.close()

    pywhatkit.sendwhatmsg(str(num),"List of Unfollowers"+"\n"+names,13, 36)

insta_info.get_my_followers()
insta_info.get_my_followees()
insta_info.get_my_unfollowers()
insta_info.get_my_mutual_friends()
send_whatsapp_msg()
