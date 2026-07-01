email = "   alex@gmail.com    "
print (email.strip())


string_url = "https://xyz.com"
if string_url.startswith("https") :
    print (string_url)
else :
    print ("no result found")


log_entry = "[ERROR]===System Crash==="
print (log_entry.rstrip("="))



file_name = ("final_report.pdf")
if file_name.endswith(".pdf") :
    print (file_name)
else :
    print ("error")    


search = "IPHONE"
print (search.lower())

item_price = "450"
print (item_price.rjust(10))


line = "# This is a comment line"
if line.startswith("#") :
    print (line)
else :
    print ("this is not a comment line")    


domain = "www.google.com"
print (domain.lstrip("www."))


score = "75"
print (score.rjust(5, "0"))


title = "blue running shoes"
print (title.replace(" " , "-"))


key = "KEY123XYZ\n"
print (key.strip("\n"))


server = "sub-domain-01"
print (server.upper())


