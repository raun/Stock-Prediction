from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','green'])
	#plot(openingPrice[199:])
	# Calculate STOC
	STOClst=[]
	for i in range(199,len(openingPrice)-10):
		STOClst.append(STOC(closingPrice[i],lowestPrice[i:i+10],highestPrice[i:i+10]))
	plot(STOClst)
	legend(['Stochastic Oscillator'],loc='upper left')
	show()

if __name__ == '__main__':
	main()