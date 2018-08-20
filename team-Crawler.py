from bs4 import BeautifulSoup
import requests
import csv


address = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&role=TM&offensiveStatisticCategory=RUSHING&defensiveStatisticCategory=null&season=1980&seasonType=REG&tabSeq=2&qualified=false&Submit=Go'


def WRscraper(web, file):

    source = requests.get(web).text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = file
    csv_writer = csv.writer(csv_file) #decides what file to write to

    body = soup.find('tbody')

    # anchor = body.a #gets names and is working

    rowes = body.find_all('tr')
    # divs = rowes.find('td', class_="sorted right")   #gets receptions and is working


    for i in range(len(rowes)):

        # divs = rowes[i].find_all('td', class_="sorted right")
        divs2 = rowes[i].find_all('td', class_="right")
        anchor = rowes[i].find_all('a')

        team = anchor[0].text
        # print(name)

        attempts =str(divs2[0].text)
        attemptePerGame =str(divs2[1].text)
        yards =str(divs2[2].text)
        avgYards = str(divs2[3].text)
        yardsGame = str(divs2[4].text)
        TDs = str(divs2[5].text)


        # str.strip(yards.replace(',',''))
        csv_writer.writerow([team, str.strip(attempts),str.strip(yards.replace(',','')),str.strip(attemptePerGame), str.strip(avgYards),str.strip(yardsGame), str.strip(TDs) ])




def InnerpageCrawler(url, season, file): #this function populates urlArray with urls to crawl
    year =season
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    csv_file = file

    LinkClass = soup.find(class_='linkNavigation floatRight')
    linkCount = LinkClass.find_all('a')
    
    
    for i in range(len(linkCount)-1):
                
        Innerlink = linkCount[i]
        InnernextLink = 'http://www.nfl.com/stats/categorystats?tabSeq=0&season='+year+'&seasonType=REG&Submit=Go&archive=true&d-447263-p='+Innerlink.text+'&statisticCategory=RECEIVING&conference=null&qualified=true'
        
  
        #call scrape and pass InnernextLink

        WRscraper(InnernextLink, csv_file)
        # print("innernextLink = ", InnernextLink)

def pageCrawler(year, finish): #this function populates urlArray with urls to crawl
    

    year = year
    finish = finish + 1
  
    for year in range(year, finish):
        #open file here with name of year.csv


        name = str(year)
        # print('file opens' )
        csv_file = open('TEAM_'+ name +'.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Team','Attempts','Yards', 'AttemptsPerGame', 'AYardsPerCarry', 'YardsPerGame','TDs']) #writes header
        
        link = str(year)
            
        nextLink = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&role=TM&offensiveStatisticCategory=RUSHING&defensiveStatisticCategory=null&season='+link+'&seasonType=REG&tabSeq=2&qualified=false&Submit=Go'
        # hrefArray.append(nextLink)
        year +=1
        # yearArray.append(year)
        # print(year)

        #call scrape function and pass next link
        WRscraper(nextLink, csv_file)

        # InnerpageCrawler(nextLink, link, csv_file)  #this function gets each inner page
        # print("next link", nextLink)
        csv_file.close()
        



def main():
    
    # to scrape change the start year to whatever you want
    start = 1980
    finish = 2017

    pageCrawler(start, finish)  

    # csv_file.close()
    
        
main()