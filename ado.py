from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue'])
	# Calculate ADO
	ADOlst=[]
	for i in range(199,len(openingPrice)):
		a= ADO(closingPrice[i],highestPrice[i],lowestPrice[i])
		if a==None:
			#print i,closingPrice[i],highestPrice[i],lowestPrice[i]
			ADOlst.append(0)
		else:
			ADOlst.append(a)
	plot(ADOlst)
	ylabel('Value')
	xlabel('For Different Dates')
	legend(['Accumulation/Distribution Oscillator'],loc='upper left')
	show()

if __name__ == '__main__':
	main()