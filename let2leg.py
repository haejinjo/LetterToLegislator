#! /usr/bin/env python                                                                                                                 

# Author: Haejin Jo                                                                                                                    

import argparse
import json
import lob
import os
import requests
import sys


lob.api_key = os.environ.get('LOB_KEY')
google_civic_api = os.environ.get('SECRET_KEY')
from apiclient.discovery import build



def main():

    parser=argparse.ArgumentParser(description="Send a letter to your legislator and preview the PDF.")
    parser.add_argument('file', type=argparse.FileType('r'), nargs='+') # requires one ore more args or error message gen'd
    args = parser.parse_args()

    inputName = ''
    inputAddress = ''
    inputMessage = ''
    counter = 0

    for f in args.file:
        with f as file:
            if counter == 0:
                inputName = file.read()
            elif counter == 1:
                inputAddress = file.read()
            elif counter == 2:
                inputMessage = file.read()

        counter+=1

    service = build('civicinfo', 'v2', developerKey=google_civic_api)
    collection = service.representatives()
    request = collection.representativeInfoByAddress(address=inputAddress)
    response = request.execute() # python obj built from JSON response sent by APIserver 

    # to make life easier, let's shorten our access lines 
    json_prefix = response['officials'][0]
    sender_prefix = response['normalizedInput']

    politicianName = json_prefix['name'] 
    politicianAddrOne = json_prefix['address'][0]['line1']
    politicianAddrTwo = json_prefix['address'][0]['line2'] 
    politicianCity = json_prefix['address'][0]['city']
    politicianState = json_prefix['address'][0]['state']
    politicanZip = json_prefix['address'][0]['zip']
    politicianFace = json_prefix['photoUrl']

    senderName = inputName
    senderAddrOne = sender_prefix['line1']
    senderCity = sender_prefix['city']
    senderState = sender_prefix['state']
    senderZip = sender_prefix['zip'] 


    letterToSend = lob.Letter.create(
        to_address = {
        'name': politicianName,
        'address_line1': politicianAddrOne,
        'address_line2': politicianAddrTwo,
        'address_city': politicianCity,
        'address_state': politicianState,
        'address_zip': politicanZip,
        },

        from_address = {
          'name': senderName,
          'address_line1': senderAddrOne,
          'address_city': senderCity,
          'address_state': senderState,
          'address_zip': senderZip,
          },

        file = 'tmpl_4a94d31893b90ae',

        merge_variables = {
        'name': politicianName,
        'img': politicianFace,
        'message': inputMessage,
        },

        color = False # Save money and ink 
    )

    # Access the response object's unique ID that gets returned by Lob's creation method
    print letterToSend['url']

if __name__=="__main__":
    main()
