count=0
char=input("Enter Character of the string to be fetched:\n")
file_object=open('sample.txt','r')
file_list=file_object.read()
num_words=file_list.split()

for letter in range(len(num_words)):
    if num_words[letter][0]== char:
        count=count+1
        print("The corresponding string is:",num_words[letter])
        #print(count)
   
#print(file_list)
#print(num_words)
print("\n")
print("The words starting with {} is found {} times in the sample.txt file ".format(char,count))
