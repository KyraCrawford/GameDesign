
strVar = "Here are the instructions to install Drivers:\n1. After the download is completed go to where you saved the folder.(By default everything you download from the Internet is saved to the Downloads folder)\n2. Right click on the folder and choose 'Extract All' and then choose 'Extract' again.\n3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:\n*setup application\n*Asussetup\n*pnpinstal64\n*pnputil\n*Igxpin\n5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."

print(len(strVar))

WordDriverCount = strVar.count('Drivers')
print(WordDriverCount)

strVar= strVar.replace('Extract','EXTRACT')
strVar= strVar.replace('setup','SETUP')
print(strVar)

four = strVar.find('4')
print(four)

FirstEnter = strVar.find('\n')
print('The first enter is located at:', FirstEnter)
print('\n')

#step 1 only
print(strVar[46:202])

#step 2 only
print(strVar[202:289])

#step 3 only
print(strVar[289:389])

#step 4 only
print(strVar[389:546])

#step 5 only
print(strVar[546:678])
