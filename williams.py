from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue','green'])
	williams=[]
	for i in range(199,len(openingPrice)-10):
		williams.append(WILLIAMS(highestPrice[i:i+10],closingPrice[i+10],lowestPrice[i:i+10]))
	plot(williams)
	legend(['Williams'], loc='upper left')
	show()
	
if __name__ == '__main__':
	main()