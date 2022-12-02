# Get WhatsApp's chat link
Here is a simple script to get WhatsApp's chat link without saving number phone to your contacts.

# How to use
```shell
> pip install -r requirements.txt
```
run the script main.py
```shell
> python main.py
```
Enter number with country code but without `+` and press enter.
Example for Russia: `79261234567`
```shell
Enter number: 79261234567
```
Then you will get the chat link.
```shell
Enter number: 79261234567
https://api.whatsapp.com/send/?phone=79243677546&text&type=phone_number&app_absent=0
```
Then you can open this link in your browser to chat with the owner of this phone number 