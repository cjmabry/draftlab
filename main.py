import json, csv, nflgame, nfldb, urllib, scrapy, time
from scrapy.crawler import CrawlerProcess
from scrapy.xlib.pydispatch import dispatcher
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy import log, signals
from xml.etree import ElementTree
from collections import OrderedDict
from pprint import pprint

#TODO build a list of all needed stats not yet implemented
#TODO implement excel export
#TODO refactor
#TODO command line arguments
#TODO GUI (kivy)?

dk_file = urllib.URLopener()
dk_file.retrieve('https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=21&draftGroupId=7315', 'week4/DKSalaries.csv')

csvfile = open('week4/DKSalaries.csv', 'rb')

db = nfldb.connect()
q = nfldb.Query(db)

def scrape_fantasy_pros():
    players = {
        "QB":{},
        "RB":{},
        "WR":{},
        "TE":{},
        "DST":{}
    }

    class QBProjectionsItem(Item):
        name = Field()
        proj = Field()
        floor = Field()
        cieling = Field()
        # pa_att = Field()
        # pa_cmp = Field()
        # pa_yds = Field()
        # pa_tds = Field()
        # ints = Field()
        # ru_att = Field()
        # ru_yds = Field()
        # ru_tds = Field()
        # fl = Field()

    class RBProjectionsItem(Item):
        name = Field()
        proj = Field()
        floor = Field()
        cieling = Field()
        # ru_att = Field()
        # ru_yds = Field()
        # ru_tds = Field()
        # rec = Field()
        # rec_yds = Field()
        # rec_tds = Field()
        # fl = Field()

    class WRProjectionsItem(Item):
        name = Field()
        proj = Field()
        floor = Field()
        cieling = Field()
        # ru_att = Field()
        # ru_yds = Field()
        # ru_tds = Field()
        # rec = Field()
        # rec_yds = Field()
        # rec_tds = Field()
        # fl = Field()

    class TEProjectionsItem(Item):
        name = Field()
        proj = Field()
        floor = Field()
        cieling = Field()
        # rec = Field()
        # rec_yds = Field()
        # rec_tds = Field()
        # fl = Field()

    class QBProjectionsSpider(scrapy.Spider):
        name = 'QB Projections'
        allowed_domains = ['fantasypros.com']
        start_urls = [
            'http://www.fantasypros.com/nfl/projections/qb.php?max-yes=true&min-yes=true'
        ]

        def parse(self, response):
            rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")

            for row in rows:
                data = QBProjectionsItem()
                name = row.xpath("td/a/text()").extract()
                # data['pa_att'] = row.xpath("td[2]/text()").extract()[0]
                # data['pa_cmp'] = row.xpath("td[3]/text()").extract()[0]
                # data['pa_yds'] = row.xpath("td[4]/text()").extract()[0]
                # data['pa_tds'] = row.xpath("td[5]/text()").extract()[0]
                # data['ints'] = row.xpath("td[6]/text()").extract()[0]
                # data['ru_att'] = row.xpath("td[7]/text()").extract()[0]
                # data['ru_yds'] = row.xpath("td[8]/text()").extract()[0]
                # data['ru_tds'] = row.xpath("td[9]/text()").extract()[0]
                # data['fl'] = row.xpath("td[10]/text()").extract()[0]
                data['proj'] = row.xpath("td[11]/text()").extract()[0]
                data['cieling'] = row.xpath("td[11]/div/text()").extract()[0]
                data['floor'] = row.xpath("td[11]/div[2]/text()").extract()[0]


                players['QB'][name[0]] = data

    class RBProjectionsSpider(scrapy.Spider):
        name = 'RB Projections'
        allowed_domains = ['fantasypros.com']
        start_urls = [
            'http://www.fantasypros.com/nfl/projections/rb.php?max-yes=true&min-yes=true'
        ]

        def parse(self, response):
            rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")

            for row in rows:
                data = RBProjectionsItem()
                name = row.xpath("td/a/text()").extract()
                # data['ru_att'] = row.xpath("td[2]/text()").extract()[0]
                # data['ru_yds'] = row.xpath("td[3]/text()").extract()[0]
                # data['ru_tds'] = row.xpath("td[4]/text()").extract()[0]
                # data['rec'] = row.xpath("td[5]/text()").extract()[0]
                # data['rec_yds'] = row.xpath("td[6]/text()").extract()[0]
                # data['rec_tds'] = row.xpath("td[7]/text()").extract()[0]
                # data['fl'] = row.xpath("td[8]/text()").extract()[0]
                data['proj'] = row.xpath("td[9]/text()").extract()[0]
                data['cieling'] = row.xpath("td[9]/div/text()").extract()[0]
                data['floor'] = row.xpath("td[9]/div[2]/text()").extract()[0]

                players['RB'][name[0]] = data

    class WRProjectionsSpider(scrapy.Spider):
        name = 'WR Projections'
        allowed_domains = ['fantasypros.com']
        start_urls = [
            'http://www.fantasypros.com/nfl/projections/wr.php?max-yes=true&min-yes=true'
        ]

        def parse(self, response):
            rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")

            for row in rows:
                data = WRProjectionsItem()
                name = row.xpath("td/a/text()").extract()
                # data['ru_att'] = row.xpath("td[2]/text()").extract()[0]
                # data['ru_yds'] = row.xpath("td[3]/text()").extract()[0]
                # data['ru_tds'] = row.xpath("td[4]/text()").extract()[0]
                # data['rec'] = row.xpath("td[5]/text()").extract()[0]
                # data['rec_yds'] = row.xpath("td[6]/text()").extract()[0]
                # data['rec_tds'] = row.xpath("td[7]/text()").extract()[0]
                # data['fl'] = row.xpath("td[8]/text()").extract()[0]
                data['proj'] = row.xpath("td[9]/text()").extract()[0]
                data['cieling'] = row.xpath("td[9]/div/text()").extract()[0]
                data['floor'] = row.xpath("td[9]/div[2]/text()").extract()[0]

                players['WR'][name[0]] = data

    class TEProjectionsSpider(scrapy.Spider):
        name = 'TE Projections'
        allowed_domains = ['fantasypros.com']
        start_urls = [
            'http://www.fantasypros.com/nfl/projections/te.php?max-yes=true&min-yes=true'
        ]

        def parse(self, response):
            rows = response.xpath("//div[@class='mobile-table']//table/tbody/tr")

            for row in rows:
                data = TEProjectionsItem()
                name = row.xpath("td/a/text()").extract()
                # data['rec'] = row.xpath("td[2]/text()").extract()[0]
                # data['rec_yds'] = row.xpath("td[3]/text()").extract()[0]
                # data['rec_tds'] = row.xpath("td[4]/text()").extract()[0]
                # data['fl'] = row.xpath("td[5]/text()").extract()[0]
                data['proj'] = row.xpath("td[6]/text()").extract()[0]
                data['cieling'] = row.xpath("td[6]/div/text()").extract()[0]
                data['floor'] = row.xpath("td[6]/div[2]/text()").extract()[0]

                players['TE'][name[0]] = data

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    def stop_reactor():
        process.stop()

    dispatcher.connect(stop_reactor, signal=signals.spider_closed)

    process.crawl(QBProjectionsSpider)
    process.crawl(RBProjectionsSpider)
    process.crawl(WRProjectionsSpider)
    process.crawl(TEProjectionsSpider)
    process.start() # the script will block here until the crawling is finished

    log.msg('Reactor stopped.')
    return players

def split_csv_by_position(csvfile):
    reader = csv.reader(csvfile)
    head = next(reader)

    data = OrderedDict()

    for row in reader:
        position = row[0]
        name = row[1]
        salary = int(row[2])
        game_info = row[3]
        fppg = float(row[4])
        team = nflgame.standard_team(row[5])
        value = round(fppg/salary*1000,2)

        if '@' in game_info:
            home_team = nflgame.standard_team(game_info.split('@')[1].split(' ')[0])
            away_team = nflgame.standard_team(game_info.split('@')[0])
        else:
            home_team = None
            away_team = None

        if team == home_team:
            opponent = away_team
            site = 'Home'
        elif team == away_team:
            opponent = home_team
            site = 'Away'
        else:
            opponent = None
            site = None

        if position not in data:
            data[position] = OrderedDict()

        data[position][name] = OrderedDict()
        data[position][name]['salary'] = salary
        data[position][name]['fppg'] = fppg
        data[position][name]['value'] = value
        data[position][name]['team'] = team
        data[position][name]['opponent'] = opponent
        data[position][name]['floor'] = None
        data[position][name]['proj'] = None
        data[position][name]['cieling'] = None
        data[position][name]['proj value'] = None
        data[position][name]['site'] = site
        data[position][name]['spread'] = None
        data[position][name]['opp pa yds all'] = None
        data[position][name]['opp pa yds all/game'] = None
        data[position][name]['opp pa tds all'] = None
        data[position][name]['opp pa tds all/game'] = None
        data[position][name]['opp ru yds all'] = None
        data[position][name]['opp ru yds all/game'] = None
        data[position][name]['opp ru tds all'] = None
        data[position][name]['opp ru tds all/game'] = None
        # data[position][name]['player pa yds'] = None
        # data[position][name]['player pa yds/game'] = None
        # data[position][name]['player pa tds'] = None
        # data[position][name]['player pa tds/game'] = None
        # data[position][name]['player ru yds'] = None
        # data[position][name]['player ru yds/game'] = None
        # data[position][name]['player ru tds'] = None
        # data[position][name]['player ru tds/game'] = None
        # data[position][name]['player rec yds'] = None
        # data[position][name]['player rec yds/game'] = None
        # data[position][name]['player rec tds'] = None
        # data[position][name]['player rec tds/game'] = None
        data[position][name]['game info'] = game_info

    data = insert_projections(data)
    data = insert_spread(data)
    return data

def insert_projections(data):
    projections = scrape_fantasy_pros()

    for key, value in data.iteritems():
        position = key
        for key, value in value.iteritems():
            if key in projections[position]:
                data[position][key]['floor'] = projections[position][key]['floor']
                data[position][key]['proj'] = projections[position][key]['proj']
                data[position][key]['cieling'] = projections[position][key]['cieling']
                data[position][key]['proj value'] = round(float(data[position][key]['proj'])/int(data[position][key]['salary'])*1000,2)

    return data

def insert_spread(data):

    vegas_file = urllib.URLopener()
    vegas_file.retrieve('http://xml.pinnaclesports.com/pinnaclefeed.aspx?sporttype=Football&sportsubtype=nfl','week4/vegasodds.xml')
    tree = ElementTree.parse('week4/vegasodds.xml')

    for key, value in data.iteritems():

        for key, value in value.iteritems():

            # print key

            # odds
            root = tree.getroot()

            events = root[3]

            events = root.findall("./events/event")

            for event in events:

                participants = event.findall("./participants/participant/participant_name")

                for participant in participants:

                    current_team_name = nflgame.standard_team(participant.text)

                    if value['team'] == current_team_name:

                        if value['site'] == 'Home':

                            if event.find("./periods/period/spread/spread_home") is not None:
                                value['spread'] = event.find("./periods/period/spread/spread_home").text
                            else:
                                value['spread'] = 'Not posted'
                        elif value['site'] == 'Away':

                            if event.find("./periods/period/spread/spread_visiting") is not None:
                                value['spread'] = event.find("./periods/period/spread/spread_visiting").text
                            else:
                                value['spread']= 'Not posted'

    return data

def insert_nflgame_data(data):
    i = 0

    for key, value in data.iteritems():
        position = key

        for key, value in value.iteritems():
            name = key
            games = nflgame.games(2015, kind ='REG', home=value['opponent'], away=value['opponent'])

            opp_pa_yds_all = 0
            opp_pa_tds_all = 0
            opp_ru_yds_all = 0
            opp_ru_tds_all = 0

            for game in games:
                if value['opponent'] == game.home:
                    stats = game.stats_away
                    opp_pa_yds_all += stats.passing_yds
                    opp_ru_yds_all += stats.rushing_yds
                elif value['opponent'] == game.away:
                    stats = game.stats_home
                    opp_pa_yds_all += stats.passing_yds
                    opp_ru_yds_all += stats.rushing_yds

            data[position][name]['opp pa yds all'] = opp_pa_yds_all
            data[position][name]['opp ru yds all'] = opp_ru_yds_all

            i += 1
            print i
            # players = nflgame.combine_play_stats(games)
            #
            # for p in players:
            #     if p.name.split('.')[1] == name.split(' ')[1]:
            #         if 'passing_yds' in p.__dict__:
            #             tot_pa_yds = p.passing_yds
            #             print p.name
            #             print 'passing_yds'
            #             print tot_pa_yds
            #         else:
            #             tot_pa_yds = 0
            #
            #         if 'passing_tds' in p.__dict__:
            #             tot_pa_tds = p.passing_tds
            #             print p.name
            #             print 'passing_tds'
            #             print tot_pa_tds
            #         else:
            #             tot_pa_tds = 0
            #
            #         if 'rushing_yds' in p.__dict__:
            #             tot_ru_yds = p.rushing_yds
            #             print p.name
            #             print 'rushing_yds'
            #             print tot_ru_yds
            #         else:
            #             tot_ru_yds = 0
            #
            #         if 'rushing_tds' in p.__dict__:
            #             tot_ru_tds = p.rushing_tds
            #             print p.name
            #             print 'rushing_tds'
            #             print tot_ru_tds
            #         else:
            #             tot_ru_tds = 0
            # # print key

    return data

def write_csv(data):

    for key, value in data.iteritems():
        csvfile = open(key + '.csv', 'w+')
        writer = csv.writer(csvfile)

        for key, val in value.iteritems():
            head = ['position']

            for key, val in val.iteritems():
                head.append(key)

        writer.writerow(head)

        for key, value in value.iteritems():
            name = key
            row = [name]

            for key, value in value.iteritems():
                # print key
                row.append(value)

            writer.writerow(row)

    # print head

data = split_csv_by_position(csvfile)
final = insert_nflgame_data(data)
write_csv(final)
