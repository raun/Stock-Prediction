from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue','green'])
	plot(openingPrice[199:])

	# Calculate SMA10
	SMAlst=[]
	for i in range(199,len(openingPrice)):
		SMAlst.append(SimpleMovingAverage(openingPrice[i:i+10]))
	plot(SMAlst)

	# Calculate EMA10
	EMAlst=[SMAlst[0]]
	for i in range(199,len(openingPrice)-10):
		EMAlst.append(ExponentialMovingAverage(EMAlst[i-199],closingPrice[i],SMAlst[i-198]))
	plot(EMAlst)
	legend(['Opening Price','Simple Moving Average','Exponential Moving Average'], loc='upper left')
	show()

if __name__ == '__main__':
	main()