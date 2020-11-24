# it3038c-scripts
Javascript code block

Hello

It's me, a Networking student!

Lab 2

#!/bin/bash
#This script email user, IP, date, and hostname
    
content="User $USER"
    
emailaddress="panditpgmail.uc.edu"
    
today=$(date +"%H:%M:%S")
    
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
    
content="ip $ip, User $USER, date $today, host $HOSTNAME, machine $MACHTYPE"

echo $content

mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)

### Lab 7
hi
Here's how I can run a Python script as being created that uses a plugin named Pillow. At first, let me create a virtual env known as scripts. I can call it as I like.
```bash
virtualenv ~/venv/pillow
source ~/venv/scripts/bin/activate
pip install pillow

```
Let me find an image as I prefer to apply here. It can be literally anything. If I'm smart I can do it from the command like I guess. So let me download an image from the internet and save it to my hard drive. Here in Python, let's run the following command code
```python
from PILL import Image, ImageFilter
myImage = Image.open('/full/path/to/image.jpg')
myImage.load
```
The syntax above will load the image. Let's now run several commands against it to get format and size, and even show the image.

