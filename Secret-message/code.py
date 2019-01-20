# --------------
##File path for the file 
file_path 

#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    
    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence


#Calling the function to read file
sample_message=read_file(file_path)

#Printing the line of the file
print(sample_message)

#Code ends here

#Code starts here


# --------------
#Code starts here
##File path for the file 
file_path_1, file_path_2 

#Code starts here

#Function to read file
def read_file1(file1):
    
    #Opening of the file located in the path in 'read' mode
    file1 = open(file_path_1, 'r')
    #Reading of the first line of the file and storing it in a variable
    sentence1=file1.readline()
    
    #Closing of the file
    file1.close()
    
    #Returning the first line of the file
    return sentence1
def read_file2(file2):
    file2 = open(file_path_2,'r')
    sentence2=file2.readline()
    file2.close()
    return sentence2


#Calling the function to read file
message_1=str(read_file1(file_path_1))
message_2=str(read_file2(file_path_2))


#Code ends here
def fuse_msg(message_a,message_b):
    quotient=(int(message_b)//int(message_a))
    return str(quotient)
secret_msg_1=fuse_msg(message_1,message_2)
#Code starts here






# --------------
#Code starts here
file_path_3

#Code starts here

#Function to read file
def read_file(file3):
    
    #Opening of the file located in the path in 'read' mode
    file3 = open(file_path_3, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence3=file3.readline()
    
    #Closing of the file
    file3.close()
    
    #Returning the first line of the file
    return sentence3


#Calling the function to read file
message_3=read_file(file_path_3)
#Printing the line of the file
print(message_3)

def substitute_msg(message_c):
    if message_c =='Red':
        sub=('Army General')
    elif message_c == 'Green':
        sub=('Data Scientist')
    elif message_c == 'Blue':
        sub=('Marine Biologist')     
    return sub  
      
secret_msg_2=substitute_msg(message_3)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

def compare_msg(message_d,message_e):
    a_list=message_d.split(' ')
    b_list=message_e.split(' ')
    c_list=[i for i in a_list if i not in b_list]
    final_msg=" ".join(c_list)
    return final_msg
#Code starts here

message_4='I hope you are good now'
message_5='I hope good things happen in your life.'
print(message_4)
print(message_5)

secret_msg_3='you are now'


# --------------
#Code starts here
file_path_6

file6= open(file_path_6,'r')
message_6= file6.readline()
print(message_6)

def extract_msg(message_f):
    a_list= message_f.split()
    even_word = lambda message_f:  len(message_f)%2==0
    b_list=filter(even_word,a_list)
    final_msg=' '.join(b_list)
    return final_msg
secret_msg_4=extract_msg(message_6)
secret_msg_4 = str(secret_msg_4)
secret_msg_4








# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = ' '.join(message_parts)
print(secret_msg)

final_path= user_data_dir + '/secret_message.txt'

#Code starts here
def write_file(secret_msg,path):
    g = open(final_path,'a+')
    g.write(secret_msg)
    g.close()
write_file(secret_msg,final_path)


