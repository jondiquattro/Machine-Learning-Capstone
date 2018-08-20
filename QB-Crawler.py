from bs4 import BeautifulSoup
import requests
import csv


address = 'http://www.nfl.com/stats/categorystats?archive=true&conference=null&statisticCategory=PASSING&season=1980&seasonType=REG&tabSeq=0&qualified=true&Submit=Go'


def QBscraper(web, file):

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

        team = anchor[1].text
        name = anchor[0].text
        # print(name)

        completions = str(divs2[0].text)
        attempts =str(divs2[1].text)

       
        attemptsPerGame =str(divs2[3].text)
        yards = str(divs2[4].text)
        avgYardsGame = str(divs2[6].text)
        
        TDs = str(divs2[7].text)

        
        # str.strip(yards.replace(',',''))
        csv_writer.writerow([name, team, str.strip(completions), str.strip(attempts),str.strip(yards.replace(',','')),str.strip(attemptsPerGame), str.strip(avgYardsGame), str.strip(TDs)])




def InnerpageCrawler(url, season, file): #this function populates urlArray with urls to crawl
    year =season
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    csv_file = file

    LinkClass = soup.find(class_='linkNavigation floatRight')
    linkCount = LinkClass.find_all('a')
    
    
    for i in range(len(linkCount)-1):
                
        Innerlink = linkCount[i]
        InnernextLink ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+year+'&seasonType=REG&d-447263-p='+Innerlink.text+'&statisticPositionCategory=QUARTERBACK&qualified=true'
        #                http://www.nfl.com/stats/categorystats?tabSeq=1&season='+year+'&seasonType=REG&d-447263-p='+Innerlink.text+'&statisticPositionCategory=QUARTERBACK&qualified=true'
  
        #call scrape and pass InnernextLink

        QBscraper(InnernextLink, csv_file)
        # print("innernextLink = ", InnernextLink)

def pageCrawler(year, finish): #this function populates urlArray with urls to crawl
    

    year = year
    finish = finish + 1
  
    for year in range(year, finish):
        #open file here with name of year.csv


        name = str(year)
        print('file opens' )
        csv_file = open('QB_'+ name +'.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name', 'Team','Completions','Attempts', 'Yards', 'AttempsPerGame', 'YardsPerGame','TDs']) #writes header
        
        link = str(year)
                   
        nextLink = 'http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=QUARTERBACK&qualified=true&season='+link+'&seasonType=REG'
        # hrefArray.append(nextLink)
        year +=1
        # yearArray.append(year)
        # print(year)

        #call scrape function and pass next link
        QBscraper(nextLink, csv_file)

        InnerpageCrawler(nextLink, link, csv_file)  #this function gets each inner page
        # print("next link", nextLink)
        csv_file.close()
        



def main():
    
    # to scrape change the start year to whatever you want
    start = 1980
    finish = 2017

    pageCrawler(start, finish)  

    # csv_file.close()
    
        
main()