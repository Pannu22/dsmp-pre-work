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


# --------------
#Code starts here

#Opening files:
file_1 = open(file_path_1)
file_2 = open(file_path_2)

#Reading & Printing messages:
message_1 = read_file(file_path_1)
print(message_1)
message_2 = read_file(file_path_2)
print(message_2)

#Declaring a function fuse_msg():
def fuse_msg(message_a, message_b):
    int_message_a = int(message_a)
    int_message_b = int(message_b)
    quotient = (int_message_b//int_message_a)
    return str(quotient)

#Calling the function fuse_msg():    
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)



# --------------
#Code starts here

#Opening file:
file_3 = open(file_path_3)

#Reading file:
message_3 = read_file(file_path_3)

print(message_3)

#Defining a function substitute_msg():
def substitute_msg(message_c):
    sub = ''
    if  str(message_c) == 'Red':
        sub = 'Army General'
    elif str(message_c) == 'Green':
        sub = 'Data Scientist'
    elif str(message_c) == 'Blue':
        sub = 'Marine Biologist'
    return str(sub)

#Calling function substitute_msg():
secret_msg_2 = substitute_msg(message_3)


# --------------
# Opening files:
file_4 = open(file_path_4)
file_5 = open(file_path_5)

# Reading files:
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

print(message_4)
print(message_5)

# Declaring function compare_msg():
def compare_msg(message_d, message_e):
    a_list = message_d.split(' ')
    b_list = message_e.split(' ')
    c_list = [i for i in a_list + b_list if i not in b_list]
    final_msg = ' '.join(c_list)
    return final_msg

# Calling function compare_msg():
secret_msg_3 = compare_msg(message_4, message_5)
        
#Code starts here







# --------------
#Code starts here

#Opening file:
file_6 = open(file_path_6)

#Reading file:
message_6 = read_file(file_path_6)
print(message_6)

#Declaring function extract_msg():
def extract_msg(message_f):
    a_list = message_f.split(' ')
    even_word = lambda x : (len(x)%2 == 0)
    b_list = filter(even_word, a_list)
    final_msg = ' '.join(b_list)
    return str(final_msg)

#Calling function extract_msg():
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = ' '.join(message_parts)
print(secret_msg)

#Declaraing function write_file():
def write_file(secret_msg, path):
    file_final = open(path, mode='a+')
    file_final.write(' '.join(secret_msg))
    file_final.close()

#Calling function write_file():
ans = write_file(secret_msg, final_path)
print(ans)



