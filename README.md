# Letter to Legislator 

## About

let2leg, otherwise known as Letter to Legislator, is a program that takes a user's personal information as input and seamlessly utilizes Lob's powerful API service to send a letter to his or her state and/or country's legislator. (Future versions to come: Customize by entering the position and rank of legislator of your choice as a parameter)

### Prerequisites

You will need Python 2.7 or later to run let2leg. However, you can have multiple Python versions (2.x and 3.x) installed on the same system without problems!

```
sudo apt-get install python 
```

### Usage

Please read. This is a very important syntax note to prevent errors. 

To make use of let2leg, users must provide three separate textfiles created on an editor of your choice as input, in the following order and content form:

1) First Name Last name
2) Addressline City State Zipcode
3) The message you would like to get through to your legislator. (Please keep it to 500 characters or less)
```
./let2leg nameFile addressFile messageFile

Output: A link to the PDF that displays what you just sent to your legislator
`

## Built With

* [Lob](http://www.dropwizard.io/1.0.2/docs/) - The physical mailing framework used
* [Google](https://developers.google.com/civic-information/) - Used to generate politician mailing addresses in the correct areas 
* [Homebrew](https://brew.sh/) - For upgrading and installing various packages on the fly 

## Authors

* **Haejin Jo** 

## Acknowledgments

* Hat tip to stackoverflow for teaching me Python and API usage in a couple hours
* Thank you to Lob for inadvertently throwing me into a code sprint in between classes 
