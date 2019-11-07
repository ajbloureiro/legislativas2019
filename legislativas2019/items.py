# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# ResultItem
class ResultItem(scrapy.Item):
    district = scrapy.Field()
    city = scrapy.Field()
    parish = scrapy.Field()

    date = scrapy.Field()

    availableMandates = scrapy.Field()
    blankVotes = scrapy.Field()
    blankVotesPercentage = scrapy.Field()
    displayMessage = scrapy.Field()
    electronicVotersPercentage = scrapy.Field()
    hasNoVoting = scrapy.Field()
    nullVotes = scrapy.Field()
    nullVotesPercentage = scrapy.Field()
    numberParishes = scrapy.Field()
    numberVoters = scrapy.Field()
    percentageVoters = scrapy.Field()
    resultsParty = scrapy.Field()
    absoluteMajority = scrapy.Field()
    party = scrapy.Field()
    constituencyCounter = scrapy.Field()
    mandates = scrapy.Field()
    percentage = scrapy.Field()
    presidents = scrapy.Field()
    validVotesPercentage = scrapy.Field()
    votes = scrapy.Field()