def morseToEnglish(val): 
    for key, value in morseCode.items(): 
         if val == " ": 
             return ""
         elif val==value:
             return key
morseCode={"a":"•-","b":"-•••","c":"-•-•","d":"-••","e":"•","f":"••-•","g":"--•","h":"••••","i":"••",
           "j":"•---","k":"-•-","l":"•-••","m":"--","n":"-•","o":"---","p":"•--•","q":"---","r":"•-•",
           "s":"•••","t":"-","u":"••-","v":"•••-","w":"•--","x":"-••-","y":"-•--","z":"--••"," ":"   ",
           "!":"  "}
choice=input("1.English to Morse(or)2.Morse to English")
if(choice=="1"):
    word=input("Enter Words: ").lower()
    print("Entered Text is, , ",word)
    for i in word:
        print(morseCode[i],end=' ')
else:
    code=input("Enter code:(note enter'!' in order to represent space between words:) ) ").split()
    
    for i in code:
        
        print(morseToEnglish(i),end="")
