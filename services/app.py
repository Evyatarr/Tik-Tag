
import urllib.parse
name_input = (input("ENTER NAME: "))
phone_input = (input("ENTER PHONE: " ))
choice = ["A"]

def link_generator(name,phone):
    message  = (f"Hello {name}!, I found your luggage in (enter place)! Please contact me so you can take It back! ")
    encoded_message = urllib.parse.quote(message)
    wa_link=(f"https://wa.me/{phone}?text={encoded_message}")
    return wa_link


link_generator(name_input,phone_input)
