#DAY 10 EXERCISES
1.#Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):print(number)
1.2#Iterate 10 to 0 using for loop, do the same using while loop.
number=0
while number<11:
    print (number)
    number+=1
2.#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
for i in range(1, 8):
    print("#" * i)
3.#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(1,8):
    print("# "*8)
4.#Print the following pattern:
"""0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""
for i in range(1,11):
    print(f"{i}x{i}={i*i}")#DIFÍCIL
5.#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
a=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in a:
    print(i)
6.#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,100,2):
        print(i)
7.#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1,100,2):
    print(i)#ME HA COSTAO
#LEVEL 2
1.#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(0,101):
    sum+=i
    print("Sum: ",sum)#CHATGPT
2.#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum=0;sumodds=0
for i in range(0,101,2):
    sum+=i
for i in range(1,101,2):
    sumodds+=i
print("The sum of the evens is",sum,"and the sum of the odds is",sumodds)#FACILL
#LEVEL 3
1.#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
for country in countries:
    if "land" in country:
        print(country)#ALGO DE AYUDITA
2.#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    print(fruits[-1])
    print(fruits[-2])
    print(fruits[-3])
    print(fruits[-4])
    print("fin")
3.
"""Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world"""#NO SÉ HACERLO



