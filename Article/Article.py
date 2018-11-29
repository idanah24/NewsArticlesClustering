#    Article Class    #

def cutOutString(start, end, content):
    startIndex = content.index(start) + len(start)
    endIndex = content.index(end) - 1
    return content[startIndex:endIndex]
    
        
class Article:
    
    def __init__(self, data):
    
        self.title = cutOutString("\"title\":\"", "\",\"description\"", data)
        self.sourceName = cutOutString(",\"name\":\"",  "\"},\"author\"", data)
        self.url = cutOutString(",\"url\":\"", "\",\"urlToImage", data)
        self.content = self.title + cutOutString(",\"description\":\"", "\",\"url", data) + cutOutString(",\"content\":\"", "[+", data)
        
        
        
        
    def __str__(self):
        return self.title    
        
        
        
