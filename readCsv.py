import csv
from  pylab import *
def FetchData(filename):
	'''This function takes a filename and returns various parameters as list
	INPUT : filename of type str
	OUTPUT : openingPrice of type list containing the opening price of each day
			highestPrice of type list containing the highest price of each day
			lowestPrice of type list containing the lowest price of each day
			closingPrice of type list containing the closing price of each day
	'''
	openingPrice=[]
	highestPrice=[]
	lowestPrice=[]
	closingPrice=[]
	with open(filename,'rb') as csvfile:
		spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
		for row in spamreader:
			lt = row[0].split(",",9)
			if lt[1] != 'Open':
				openingPrice.append(float(lt[1]))
				highestPrice.append(float(lt[2]))
				lowestPrice.append(float(lt[3]))
				closingPrice.append(float(lt[4]))
	return openingPrice,highestPrice,lowestPrice,closingPrice

def SimpleMovingAverage(lst):
	'''This function takes a list of numbers and find the Simple Moving Average
	INPUT : lst of type list of numbers
	OUTPUT : returns the Simple Moving Average as float
	'''
	SMA = 0
	n = len(lst)
	for value in lst:
		SMA = SMA +value
	return float(SMA/n)

def ExponentialMovingAverage(preEMA,closingPrice,SMA):
	'''This function takes a list of numbers and find the Exponential Moving Average
	INPUT: lst of type list of numbers
		preEMA of type float which is previous day EMA
		closingPrice of type float which is previous day closing price
	OUTPUT : returns the Exponential Moving Average as float'''
	multiplier = 0.1818
	EMA = (closingPrice - preEMA)*multiplier + preEMA
	return EMA

def ADO(closingPrice,highestPrice,lowestPrice):
	'''Finds Accumulation/Distribution Oscillator
	INPUT : closingPrice is a list of closing price of last n days
		highestPrice is a list of highest price of last n days
		lowestPrice is a list of lowest price of last n days
	OUTPUT : returns the Accumulator/Distribution Oscillator
	'''
	if highestPrice - lowestPrice == 0:
		return None
	return (((closingPrice-lowestPrice)-(highestPrice-closingPrice))/(highestPrice - lowestPrice))

def STOC(todaysClose,lowestPrice,highestPrice):
	'''Finds Stochastic Indicator
	INPUT : todaysClose is the closing price of todaysClose
		lowestPrice is the lowest price 
	'''
	return ((todaysClose - min(lowestPrice))*100/(max(highestPrice) - min(lowestPrice)))

def OBV(todaysClose,yesterdayClose,yesterdayOBV,todayVolume):
	'''On Balance Volume (OBV) measures buying and selling pressure 
	as a cumulative indicator that adds volume on up days and 
	subtracts volume on down days
	'''
	if todaysClose > yesterdayClose :
		OBV = yesterdayOBV + todayVolume
	elif todaysClose < yesterdayClose:
		OBV = yesterdayOBV - todayVolume
	else:
		return yesterdayOBV
	return OBV

def WILLIAMS(highestPrice,todaysClose,lowestPrice):
	'''It is a momentum indicator that measures overbought/oversold levels
	'''
	return (max(highestPrice)-todaysClose)* -100 /(max(highestPrice)-min(lowestPrice))

def RSI():
	return NotImplemented

def PROC(closingPrice):
	'''The PROC indicator displays the difference between the current price 
	and closing price x-time periods ago
	'''
	return (closingPrice[-1] - closingPrice[0])*100/closingPrice[0]

def CPACC(closingPrice):
	return (closingPrice[-1] - closingPrice[0])/len(closingPrice)

def main():
	# FETCHING DATA FROM FILE
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue','green','yellow'])
	plot(openingPrice[199:])
	plot(highestPrice[199:])
	plot(lowestPrice[199:])
	plot(closingPrice[199:])
	legend(['Opening Price','Highest Price','Lowest Price','Closing Price'], loc='upper left')
	show()
	
if __name__ == '__main__':
	main()
