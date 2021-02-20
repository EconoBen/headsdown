from rumps import *
import subprocess
import os
import csv
from pathlib import Path

# to do:
## add optionality to close_apps() function, record for reopening after session
## explicitly apps in close_apps()?

def block_websites(response:rumps.Response):
    """ Temporarily block websites to reduce distraction.

    Args:
        response (rumps.Response): Response object, 1 or 0, sent from Rumps Menu item
    """
    sites_to_block = Path('block_sites.csv').read_text().split()

    MacOs_host = '/private/etc/hosts'
    redirect = "127.0.0.1"
    
    if response == 1: 
        with open(MacOs_host, 'r+') as hostfile:
            hosts = hostfile.read()
            for site in sites_to_block:
                if site not in hosts:
                    hostfile.write(redirect+' '+site+'\n')
    else:
        with open(MacOs_host, 'r+') as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in sites_to_block):
                    hostfile.write(host)
            hostfile.truncate()

def close_apps():
    """
    closes potentially distracting apps
    """
    pids = subprocess.check_output(["ps aux | grep -v grep |grep -i Slack.app | awk '{print $2;}'"],
                                    shell=True, text=True).split("\n")[:-1]
    if isinstance(pids, list):
        for pid in pids:
            os.system(f"kill {pid}")
    else:
        os.system(f"kill {pids}")

def open_apps():
    """Opens apps that were closed upon invoking heads_down()
    """
    os.system("open /Applications/Slack.app")

class HeadsDownApp(object):
    def __init__(self):
        self.config = {
                        "app_name": "Heads Down App",
                        "start": "Heads Down",
                        "end": "Heads Up",
                        "blocklist": "Block Sites",
                        "quit": "Clean Quit",
                    }
        self.app = rumps.App("Heads Down", quit_button=None)
        self.app.title = "🙇‍♂️"
        self.start = rumps.MenuItem(title=self.config['start'], callback=self.heads_down)
        self.end = rumps.MenuItem(title=self.config['end'], callback=None)
        self.blocklist = rumps.MenuItem(title=self.config['blocklist'], callback=self.blocklist)
        self.app.menu = [self.start, self.end, None, self.blocklist, None]

    @rumps.clicked("Clean Quit")
    def clean_up_before_quit(_):
        """ Ensure wiping blocked sites before quitting application
        """
        block_websites(response=0)
        print("Clean Quit Activated")
        rumps.quit_application()
    
 #   @rumps.clicked('Heads Down')
    def heads_down(self, sender: rumps.Response):
        """ Block websites, close applications that will be distracting

        Args:
            sender (rumps.Response): Response object, 1 or 0, sent from Rumps Menu item
        """
        block_websites(1) # block websites
        close_apps()
        sender.set_callback(None)
        self.end.set_callback(self.heads_up)

   # @rumps.clicked('Heads Up')
    def heads_up(self, sender):
        """ Unblock websites, reopen applications that were be distracting

        Args:
            sender (rumps.Response): Response object, 1 or 0, sent from Rumps Menu item
        """
        block_websites(0)
        open_apps()
        sender.set_callback(None)
        self.start.set_callback(self.heads_down)
    
   # @rumps.clicked('Block Sites')
    def blocklist(_, __):
        """
        Write websites to CSV for blocking when invoking heads_down()
        """

        response = rumps.Window(message="Write your comma-delimited websites to block here.",
                               title="Sites to Block",
                               default_text="",
                               cancel=True,
                               dimensions=(320,160)).run()
        if response.clicked:                       
            with open('block_sites.csv','a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                sites = response.text
                if ", " in sites: 
                    sites = sites.split(', ')
                    for block in sites:
                        csvwriter.writerow([])
                        csvwriter.writerow([block])
                else:
                    csvwriter.writerow([])
                    csvwriter.writerow([sites])
        else:
            pass

    def run(self):
        """
        Run application
        """
        self.app.run()

if __name__ == '__main__':
    app = HeadsDownApp()
    rumps.debug_mode(True)
    app.run()
