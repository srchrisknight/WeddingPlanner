import os,sys,json,pprint

GuestList = {
	'Family':{
		'Knights':{
			'Bob':{'PlusOne':True},
			'Jo Ann':{'PlusOne':False},
			'Brad':{'PlusOne':False},
			'Denise':{'PlusOne':False},
			'Jesse':{'PlusOne':True},
			'Eric':{'PlusOne':True},
		},
		'Qiaos':{
			'Joshua':{'PlusOne':False},
			'Mei':{'PlusOne':False},
			'George':{'PlusOne':True},
		},
		'Sullivans':{
			'James':{'PlusOne':True},
			'Nancy':{'PlusOne':False},
		},
		'Thompsons':{
			'Richard':{'PlusOne':False},
		},
		'Turners':{
			'Matt':{'PlusOne':False},
			'Jenni':{'PlusOne':False},
			'Peter':{'PlusOne':False},
			'Emma':{'PlusOne':False},
		},
		'Blockers':{
			'Colleen':{'PlusOne':False},
			'Danny':{'PlusOne':False},
			'Brenda':{'PlusOne':True},
			'Sean':{'PlusOne':True},
		},
		'Contrerez':{
			'Antonio':{'PlusOne':False},
			'Mari':{'PlusOne':False},
			'Yani':{'PlusOne':True},
			'Yazmina':{'PlusOne':True},
		},
		'Seletzkys':{
			'Dan':{'PlusOne':False},
			'Annette':{'PlusOne':False},
			'Ian':{'PlusOne':False},
			'Jess':{'PlusOne':False},
		},
		'Hueghs':{
			'Mace':{'PlusOne':False},
			'Fiona':{'PlusOne':False},
			'Brennan':{'PlusOne':False},
			'Emilia':{'PlusOne':False},
		},
		'Monas God Parents':{
			'Joe':{'PlusOne':False},
			'Carmel':{'PlusOne':False},
		}
	},
	'Non-Related':{
		'Individuals':{
			'Brigette':{'PlusOne':True},
			'Andy':{'PlusOne':True},
			'Luis':{'PlusOne':True},
			'Robert':{'PlusOne':True},
			'Spencer':{'PlusOne':True},
			'Dan':{'PlusOne':True},
			'Tom':{'PlusOne':True},
			'Nick':{'PlusOne':True},
			'Jared':{'PlusOne':True},
			'Joanna':{'PlusOne':True},
			'Megan':{'PlusOne':True},
			'Aileen':{'PlusOne':True},
			'Michael Hernandez':{'PlusOne':True},
		},
		'Barone':{
			'Alex':{'PlusOne':True},
			'Linda':{'PlusOne':False},
		},
		'Brown':{
			'Greg':{'PlusOne':True},
			'Jessica':{'PlusOne':True},
			'Scott':{'PlusOne':False},
			'Wah':{'PlusOne':False},
		},
		'Mildenberger':{
			'Cathy':{'PlusOne':False},
			'Jeff Sr':{'PlusOne':False},
			'Jeff':{'PlusOne':True},
			'Bobby':{'PlusOne':True},
			'Angel':{'PlusOne':True},
		},
		'Montoya':{
			'Michelle':{'PlusOne':True},
			'Daniel':{'PlusOne':True},
		}
	}
}




def countGuests():
	count = 0
	PlusOnes = 0
	for k in GuestList.keys():
		catagory = GuestList[k]

		for group in catagory.keys():
			count += len(catagory[group].keys())
			for Person in catagory[group].keys():
				if catagory[group][Person]['PlusOne']:
					PlusOnes += 1

	print count
	print count + PlusOnes


def makeList():
	DB = os.path.join(os.path.dirname(__file__),'WeddingInfo.json')
	Count = 0
	PotentialCount = 0
	PlusOnes = 0	
	PotentialPlusOnes = 0

	weddingInfo = {}

	for k in GuestList.keys():
		catagory = GuestList[k]

		for group in catagory.keys():
			for Person in catagory[group].keys():
				PersonData = catagory[group][Person]
				PersonData['Guest_Permission'] = PersonData['PlusOne']
				
				if PersonData['Guest_Permission']:
					PotentialPlusOnes += 1

				if not PersonData['Guest_Permission']:
					PersonData['PlusOne'] = False
				else:
					PersonData['PlusOne'] = None

				PersonData['RSVP'] = None

				if PersonData['RSVP'] is None:
					PotentialCount += 1
				else:
					if PersonData['RSVP']:
						Count += 1

	weddingInfo['GuestList'] = GuestList
	weddingInfo['HeadCount'] = '{},{}'.format(str(Count),str(Count + PlusOnes))
	weddingInfo['PotentialCount'] = '{},{}'.format(str(PotentialCount),str(PotentialCount + PotentialPlusOnes))
	weddingInfo['Expenses'] = {
		'Restrooms':{
			'price':None,
			'estPrice':900.0,
			'note':'estPrice based on quote'
		},
		'TentRental':{
			'price':None,
			'estPrice':500.0,
			'note':'estPrice based on averages'
		},
		'Chairs':{
			'price':None,
			'estPrice':80.0,
			'note':'estPrice based on averages'
		},
		'Tables':{
			'price':None,
			'estPrice':200.0,
			'note':'est includes cloths'
		},
		'cateringTruck':{
			'price':None,
			'estPrice':1350.0,
			'note':'estPrice based on averages'
		},
		'150AmpGeni':{
			'price':None,
			'estPrice':500.0,
			'note':'estPrice based on Spencer'
		}		
	}

	pprint.pprint(weddingInfo, indent = 3)

	with open(DB, 'w') as outFile:
		json.dump(weddingInfo, outFile, indent = 4)



if __name__ == '__main__':
	makeList()
	print bool(1)