from readCsv import *
def main():
	filename = str(raw_input("Enter the filename with extention:"))
	openingPrice,highestPrice,lowestPrice,closingPrice = FetchData(filename)
	
	figure(0)
	gca().set_color_cycle(['red','blue','green'])

	procLst=[0,0,0,0,0,0,0,0,0,0]
	for i in range(199,len(openingPrice)):
		procLst.append(PROC(closingPrice[i:i+10]))
	plot(procLst)
	legend(['Price Rate Change'], loc='upper left')
	show()

if __name__ == '__main__':
	main()