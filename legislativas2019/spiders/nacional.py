# -*- coding: utf-8 -*-
import scrapy
import json

from legislativas2019.items import ResultItem

class NacionalSpider(scrapy.Spider):
    name = 'nacional'
    allowed_domains = ['legislativas2019.mai.gov.pt']
    start_urls = ['https://www.legislativas2019.mai.gov.pt/frontend/data/TerritoryChildren?territoryKey=LOCAL-500000']
    
    def parse(self, response):
        # get district ids
        self.districts = json.loads(response.body)

        for district in self.districts:
            # fetch city ids
            yield scrapy.Request("https://www.legislativas2019.mai.gov.pt/frontend/data/TerritoryChildren?territoryKey={district}".format(district=district['territoryKey']), # &electionId=AR&ts={}
                callback=self.parse_cities,
                meta={"district":district})

    def parse_cities(self, response):
        self.cities = json.loads(response.body)
        
        for city in self.cities:
            # fetch city ids
            yield scrapy.Request("https://www.legislativas2019.mai.gov.pt/frontend/data/TerritoryChildren?territoryKey={city}".format(city=city['territoryKey']), # &electionId=AR&ts={}
                callback=self.parse_parishes,
                meta={
                "district": response.meta['district'],
                "city":city
            })


    def parse_parishes(self, response):
        self.parishes = json.loads(response.body)
        
        for parish in self.parishes:
            # fetch results
            yield scrapy.Request("https://www.legislativas2019.mai.gov.pt/frontend/data/TerritoryResults?territoryKey={parish}&electionId=AR".format(parish=parish['territoryKey']), # &electionId=AR&ts={}
                callback=self.parse_results_by_town,
                meta={
                    "district": response.meta['district'],
                    "city":response.meta['city'],
                    "parish": parish
                })

    def parse_results_by_town(self, response):
        results = json.loads(response.body)

        for partyResult in results["currentResults"]["resultsParty"]:
            yield ResultItem(
                district=response.meta['district']['name'],
                city=response.meta['city']['name'],
                parish=response.meta['parish']['name'],

                date='2019-10-06',

                availableMandates=results["currentResults"]["availableMandates"],
                blankVotes=results["currentResults"]["blankVotes"],
                blankVotesPercentage=results["currentResults"]["blankVotesPercentage"],
                displayMessage=results["currentResults"]["displayMessage"],
                electronicVotersPercentage=results["currentResults"]["electronicVotersPercentage"],
                hasNoVoting=results["currentResults"]["hasNoVoting"],
                nullVotes=results["currentResults"]["nullVotes"],
                nullVotesPercentage=results["currentResults"]["nullVotesPercentage"],
                numberParishes=results["currentResults"]["numberParishes"],
                numberVoters=results["currentResults"]["numberVoters"],
                percentageVoters=results["currentResults"]["percentageVoters"],
                # by party flattening
                absoluteMajority=partyResult["absoluteMajority"],
                party=partyResult["acronym"],
                constituencyCounter=partyResult["constituenctyCounter"],
                mandates=partyResult["mandates"],
                percentage=partyResult["percentage"],
                presidents=partyResult["presidents"],
                validVotesPercentage=partyResult["validVotesPercentage"],
                votes=partyResult["votes"],
            )

        for partyResult in results["previousResults"]["resultsParty"]:
            yield ResultItem(
                district=response.meta['district']['name'],
                city=response.meta['city']['name'],
                parish=response.meta['parish']['name'],

                date='2015-10-04',

                blankVotes=results["previousResults"]["blankVotes"],
                blankVotesPercentage=results["previousResults"]["blankVotesPercentage"],
                displayMessage=results["previousResults"]["displayMessage"],
                nullVotes=results["previousResults"]["nullVotes"],
                nullVotesPercentage=results["previousResults"]["nullVotesPercentage"],
                percentageVoters=results["previousResults"]["percentageVoters"],

                # by party flattening
                absoluteMajority=partyResult["absoluteMajority"],
                party=partyResult["acronym"],
                constituencyCounter=partyResult["constituenctyCounter"],
                mandates=partyResult["mandates"],
                percentage=partyResult["percentage"],
                presidents=partyResult["presidents"],
                validVotesPercentage=partyResult["validVotesPercentage"],
                votes=partyResult["votes"]
            )
        