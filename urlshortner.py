import hashlib

class url:
    long_url=0
    short_url=0

    def __init__(self,link):
        self.long_url=link
        self.short_url="https://bia.url/"

#save the url in file
    def saveUrl(self):
        
        file=open("longurl.txt","a")
        file.write(self.long_url)
        file.write("\n")
        file.close()

        file1=open("shortUrl.txt","a")
        file1.write(self.short_url)
        file1.write("\n")
        file1.close()
#find the url
    def findUrl(self,link):
        
        file1=file1=open("shortUrl.txt","r")
        list_short=file1.readlines()
        file1.close()
        file2=file2=open("longUrl.txt","r")
        list_long=file2.readlines()
        file2.close()
        print(list_long)
        link+="\n"
        index=list_long.index(link)
        print(list_short[index])


        return   
        
# setter for short_url
 
    def set_short(self,link):
        self.set_short=+link
        
    def urlshortner(self):

        base_62="HELLOWorldabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        hash_value=hash(self.long_url)
        string_value=''
        while hash_value !=0 :
             
            string_value=base_62[hash_value%62]+string_value

            hash_value=hash_value // 62
            if(hash_value==-1):
                break

        self.short_url += string_value


obj=url("https://www.google.com/search?q=how+to+add+colors+of+bootstrap+in+html+tags&source=lmns&bih=657&biw=1366&rlz=1C1UEAD_enPK1019PK1019&hl=en&sa=X&ved=2ahUKEwiRzqfuiMD9AhW7pCcCHfkzC1QQ_AUoAHoECAEQAA")
obj.urlshortner()
obj.saveUrl()
obj.findUrl("https://www.google.com/search?q=how+to+add+colors+of+bootstrap+in+html+tags&source=lmns&bih=657&biw=1366&rlz=1C1UEAD_enPK1019PK1019&hl=en&sa=X&ved=2ahUKEwiRzqfuiMD9AhW7pCcCHfkzC1QQ_AUoAHoECAEQAA")

