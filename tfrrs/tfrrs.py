#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import csv
import argparse

class tfrrs:

    def download_meet(self,meet_number):
        url = "https://xc.tfrrs.org/printable/xc_" + meet_number
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
        site = requests.get(url,headers=header).text
        site = BeautifulSoup(site,"html.parser" ).get_text().replace(u'\xa0', u' ').split("\n")
        site = [i for i in site if i != u'']
        site = site[::-1]
        data = [] 
        gender = ''
        while site != []:
            p = site.pop()
            if 'women' in p.lower():
                gender = 'women'
            elif 'men' in p.lower():
                gender = 'men'
            if 'table{border: 0 none;}' == p:
            
                table = []
                table.append(gender)
                labels = []
                while site != [] and (site[-1] != '1' or len(site[-2])<3):
                    labels.append(site.pop())
                if len(labels)>8:
                    table.append('team')
                else:
                    table.append('individual')
                table.append(labels)
                while len(site)>= len(labels):
                    athlete = []
                    for i in range(len(labels)):
                        athlete.append(site.pop())
                    if 'table{border: 0 none;}' in athlete:
                        while athlete != []:
                            site.append(athlete.pop())
                        break
                    table.append(athlete)
                data.append(table)
        return data


    def filter_meet_data(self,meet_data,men,women,individual,team):
        keep = []
        if men and women and individual and team:
            return meet_data
        if individual:
            if women:
                keep += [table for table in meet_data if table[0] == "women" and table[1] == "individual"]
            if men:
                keep += [table for table in meet_data if table[0] == "men" and table[1] == "individual"]
        if team:
            if women:
                keep += [table for table in meet_data if table[0] == "women" and table[1] == "team"]
            if men:
                keep += [table for table in meet_data if table[0] == "men" and table[1] == "team"]
        return keep 

    def write_meet(self,meet_data,meet_name):
        for table in range(len(meet_data)):
            print(str(table+1) + " file(s) have been downloaded.")
            with open("table"+str(table)+"_"+meet_name +"_" +meet_data[table][0]+"_"+ meet_data[table][1]+".csv","wb") as csvfile:
                writer = csv.writer(csvfile)
                for i in meet_data[table][2:]:
                    writer.writerow(i)

    def read_input_file(self,filename,men,women,individual,team):
        with open(filename,"r") as inputfile:
            for i in inputfile:
                i = str(i).split(',')
                data = self.download_meet(i[1].strip('\n'))
                data = self.filter_meet_data(data,men,women,individual,team)
                self.write_meet(data,i[0])




