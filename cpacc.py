from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue','green'])
	cpacc=[0,0,0,0,0,0,0,0,0,0]
	hpacc=[0,0,0,0,0,0,0,0,0,0]

	for i in range(199,len(openingPrice)):
		cpacc.append(CPACC(closingPrice[i:i+10]))
		hpacc.append(CPACC(highestPrice[i:i+10]))

	plot(cpacc)
	plot(hpacc)
	ylabel('Value')
	xlabel('For Different Dates')
	legend(['Closing Price Acceleration','High Price Acceleration'], loc='upper left')
	show()

if __name__ == '__main__':
	main()