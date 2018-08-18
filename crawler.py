from bs4 import BeautifulSoup
import requests
import csv


address = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticPositionCategory=RUNNING_BACK&season=1980&seasonType=REG&tabSeq=1&qualified=false&Submit=Go'
# url = requests.get('http://www.nfl.com/players/search?category=position&filter=runningback&conferenceAbbr=null&playerType=current&conference=ALL').text

url = requests.get(address).text

# csv_writer.writerow(['Name','Attempts', 'Attempts per Game','Total Yards', 'Yards Per Carry','Yards Per Game', 'TDS']) #writes header

def scraper(web, file):
    
    
    source = requests.get(web).text #takes a url and turn into bs4 obj
    soup = BeautifulSoup(source, 'lxml')
    csv_file = file
    csv_writer = csv.writer(csv_file) #decides what file to write to
    

    body = soup.find('tbody') #returns tbody element with all the rows I need
    playerRow = body.find_all('tr') #returns list of all rows
    
    for i in range(len(playerRow)):
        right = playerRow[i].find_all('td', class_='right')#gets class
        sortedRight = playerRow[i].find_all('td', class_='sorted right')#gets class
        # name = playerRow[i].find('a').text
        anchor = playerRow[i].find_all('a')

        name = anchor[0].text
        
        attempts = str(right[0].text)

        attemptsPerGame =str(right[1].text)
        totalYards =str(right[2].text)

        
        yardsPerCarry =str(right[3].text)
        
        yardsPerGame= str(sortedRight[0].text)

        touchDownsAllYear = str(right[5].text)


        team = str(anchor[1].text)
        
        
    

        csv_writer.writerow([name, str.strip(team), str.strip(attempts),str.strip(attemptsPerGame),str.strip(totalYards.replace(',','')), str.strip(yardsPerCarry), str.strip(yardsPerGame), str.strip(touchDownsAllYear)])
        

def InnerpageCrawler(url, season, file): #this function populates urlArray with urls to crawl
    year =season
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    csv_file = file

    LinkClass = soup.find(class_='linkNavigation floatRight')
    linkCount = LinkClass.find_all('a')
    
    
    for i in range(len(linkCount)-1):
                
        Innerlink = linkCount[i]
        InnernextLink = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season='+year+'&seasonType=REG&Submit=Go&archive=true&d-447263-p='+Innerlink.text+'&conference=null&statisticPositionCategory=RUNNING_BACK&qualified=false'
        # hrefArray.append(InnernextLink)
        #call scrape and pass InnernextLink

        scraper(InnernextLink, csv_file)
        # print("scraper on inner")
        
def pageCrawler(year, finish): #this function populates urlArray with urls to crawl
    

    year = year
    finish = finish + 1
  
    for year in range(year, finish):
        #open file here with name of year.csv

        name = str(year)
        # print('file opens' )
        csv_file = open(name +'.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name','Team','Attempts', 'Attempts per Game','Total Yards', 'Yards Per Carry','Yards Per Game', 'TDS']) #writes header
        
        link = str(year)
            
        nextLink = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticPositionCategory=RUNNING_BACK&season='+link+'&seasonType=REG&tabSeq=1&qualified=false&Submit=Go'
    
        # hrefArray.append(nextLink)
        year +=1
        # yearArray.append(year)
        # print(year)

        #call scrape function and pass next link
        scraper(nextLink, csv_file)

        InnerpageCrawler(nextLink, link, csv_file)  #this function gets each inner page
        # print("file closes")
        csv_file.close()
        # print(link)





def main():
    
    # to scrape change the start year to whatever you want
    start = 1980
    finish = 1982

    pageCrawler(start, finish)  #populates array with urls including inner pages

    # csv_file.close()
    
        
main()



