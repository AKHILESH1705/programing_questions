word_list = ['Emma','Woodhouse','father','Taylor','Miss','been','she','her','Akhi']
    #i'm using this example text in place of the file you are using
text = 'This is an example text. It will contain words you are looking for, like Emma, Emma, Emma, Woodhouse, Woodhouse, Father, Father, Taylor,Miss,been,she,her,her,her,akhi. I made them repeat to show that the code works.'
text = text.replace(',',' ') #these statements remove irrelevant punctuation
text = text.replace('.','')
text = text.lower() #this makes all the words lowercase, so that capitalization wont affect the frequency measurement
for repeatedword in word_list:
        counter = 0 #counter starts at 0
        for word in text.split():
            if repeatedword.lower() == word:
                counter = counter + 1 #add 1 every time there is a match in the list
        print(repeatedword,':', counter) #prints the word from 'word_list' and its frequency
