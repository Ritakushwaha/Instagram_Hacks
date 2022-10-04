# Instagram_Hacks

1. Run the command in terminal - 
```
instaloader --login <your_insta_username>
```

2. Run the command in terminal - 
```
python insta_unfollowers.py
```

This will generate threee .txt files with name followers.txt, followees.txt, unfollowers.txt

# Scheduling Python Scripts on Linux

```
crontab -e
```

```
* * * * * /usr/bin/env python3 /home/amninder/Desktop/Geeks/cron/schedule.py >> /home/amninder/Desktop/Geeks/cron/output.txt
```

Check logs :
```
sudo tail -f /var/log/syslog
```

This will delete the current cron jobs:
```
crontab -r
```  
