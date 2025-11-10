# Hello Forgetful People!

This is just simple little python script that you could use 
to log your end of the day at work. 

## How to run!

### Steps

1. Open a crontab editor by with the command below:
`crontab -e`


2. Add the copy/paste line below if you want the cron job to be executed 16:45 hours

```sh

45 16 * * * /usr/bin/python3 /path/to/main.py
```

3. Save and exit


Hope it is of any use. 
