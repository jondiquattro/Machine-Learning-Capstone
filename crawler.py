from bs4 import BeautifulSoup
import requests
import csv


address = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticPositionCategory=RUNNING_BACK&season=1980&seasonType=REG&tabSeq=1&qualified=false&Submit=Go'
# url = requests.get('http://www.nfl.com/players/search?category=position&filter=runningback&conferenceAbbr=null&playerType=current&conference=ALL').text

url = requests.get(address).text
hrefArray=[] #array of urls
souparray=[]

csv_file = open('1982.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Attempts', 'Attempts per Game','Total Yards', 'Yards Per Carry','Yards Per Game', 'TDS'])

def scraper(web):
    
    source = requests.get(web).text #takes a url and turn into bs4 obj
    soup = BeautifulSoup(source, 'lxml')

#for a csv file we will tell it what the headers are and then pass the scraped variables is values

    body = soup.find('tbody') #returns tbody element with all the rows I need
    playerRow = body.find_all('tr') #returns list of all rows
    



    for i in range(len(playerRow)):
        right = playerRow[i].find_all('td', class_='right')#gets class
        sortedRight = playerRow[i].find_all('td', class_='sorted right')#gets class
        name = playerRow[i].find('a').text
       
        attempts = right[0].text
        attemptsPerGame =right[1].text
        totalYards =right[2].text
        yardsPerCarry =right[3].text
        # touchDownsAllYear =right[5].text
        yardsPerGame= sortedRight[0].text
        touchDownsAllYear =right[4].text

        # print(name)
        # print(attempts)
        # print(attemptsPerGame)
        # print(totalYards)

        # print(yardsPerCarry)
        # print(yardsPerGame)
        # print(touchDownsAllYear)
        csv_writer.writerow([name,attempts,attemptsPerGame, totalYards, yardsPerCarry, yardsPerGame, touchDownsAllYear])
        

def InnerpageCrawler(url, season): #this function populates urlArray with urls to crawl
    year =season
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    LinkClass = soup.find(class_='linkNavigation floatRight')
    linkCount = LinkClass.find_all('a')
    
    
    for i in range(len(linkCount)-1):
                
        Innerlink = linkCount[i]
        InnernextLink = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season='+year+'&seasonType=REG&Submit=Go&archive=true&d-447263-p='+Innerlink.text+'&conference=null&statisticPositionCategory=RUNNING_BACK&qualified=false'
        hrefArray.append(InnernextLink)
        
def pageCrawler(): #this function populates urlArray with urls to crawl
  

    # year = 1981

    # LinkClass = soup.find(class_='linkNavigation floatRight')
    # linkCount = LinkClass.find_all('a')
    

    for year in range(1982, 2018):
        
        
        link = str(year)
            
        nextLink = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticPositionCategory=RUNNING_BACK&season='+link+'&seasonType=REG&tabSeq=1&qualified=false&Submit=Go'
    
        hrefArray.append(nextLink)
        year = year +1
        # print(nextLink)
        InnerpageCrawler(nextLink, link)
 
        # print(link)

def main():
    

    pageCrawler()
    for i in hrefArray:
        scraper(i)
    csv_file.close()
    
        
main()



