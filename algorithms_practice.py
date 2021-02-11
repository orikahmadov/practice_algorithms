###################################################################################################################################################################
#Linear Search Algorithm runs in Linear Complexity
def linear_search(list, item):
    found = False
    for i in range(len(list)):
        if list[i] == item:
            found = True
    return found
###################################################################################################################################################################

#NOTE THAT THIS ALGORITHM WORKS ONLY IF THE INPUT LIST IN SORTED 
#Binary Search
def binary_search(list, item):
    start = 0
    end  =  len(list) - 1
    while start <= end:
        middle =  (start +  end) // 2
        if list[middle] == item:
            return middle
        elif item >  list[middle]:
            start =  middle + 1
        else:
            end =  middle - 1
    return None


#Recursive binary_search
def binary_search(list, target, low, high):
    if low > high:
        return False
    else:
        mid =  (low + high) //2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            return binary_search(list, target, low, mid - 1)
        else:
            return binary_search(list, target,mid +1 , high )
###################################################################################################################################################################

def QuickSort(list):
    #length of list
    length_list =  len(list)
    #if there is less than 1 item in list return list
    if length_list <=  1:
        return list
    #define pivot
    else:
        pivot =  list.pop() #Last item as pivot

    #2 Lists which will hold the values of compared elements
    itemsLower = []
    itemsGreater = []
    #iterate through  list
    for item in list:
        if item < pivot:
            itemsLower.append(item)
        else:
            itemsGreater.append(item)
    #recursively return the function
    return QuickSort(itemsLower) + [pivot] + QuickSort(itemsGreater)

###################################################################################################################################################################
#Finding Characters frequency in a string
string =  "Today the weather is so beautiful,therefore I want to go for walk!"
def chars_frequency(list):
    chars = {}   #Start
    for i in list:
        if i not in chars:
            chars[i] = 0
        chars[i] +=1
    return chars

#Finding Word frequency in a string basically same algorithm except you split the string and convert it to list
string =  "Today the weather is so beautiful,therefore I want to go for walk and walking is so healthy !"
def word_frequency(string):
    words = {}   #Start
    for i in string.split():
        if i not in chars:
            words[i] = 0
        words[i] +=1
    return words
###################################################################################################################################################################
#Comparing 2 strings and finding how many times a single character of one string occurs in another

def str_frequency(a,b):
    str =  a + b
    characters =  {}
    for i in str:
        if i not in characters:
            characters[i] = 0
        characters[i] +=1
    return characters

###################################################################################################################################################################

#Recursion
def is_array_sorted(array):
    if len(array) == 1:
        return True
    else:
        return array[0] <= array[1]  and is_array_sorted(array[1:])


###################################################################################################################################################################
def prefix_average(s):
    n =  len(s)
    a =  [0] *n     #n times of zeros in a list
    for j in range(n):  #traverse the list s
        total = 0               
        for i in range(j + 1):  #traverse the list but start from one item forward from J (first iteration)
            total += s[i]       
        else:
            a[j] =  total / (j + 1)
    return a
  ###################################################################################################################################################################
    def find_duplicate():
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] == list[i]:
                return True
    return False
###################################################################################################################################################################

        
def download_file(filename):
    req = requests.get(link)
    content =  req.content
    if not req:
        raise Exception("Bad request has been sent")
    else:
        with open("data.csv", "wb") as file:
            file.write(content)

#send email 
       
with open("systeminfo.txt", "r") as file:
    lines = file.read()
    string_message += lines
    liness =  file.readlines()
    with SMTP_SSL(host =  "smtp.gmail.com", port =  465) as server:
        server.login(user =  "orkhan.ahmadov28@gmail.com", password=os.getenv("PASSWORD"))
        server.sendmail(msg=string_message, from_addr=os.getenv("EMAIL_ADDRESS"), to_addrs=os.getenv("EMAIL_ADDRESS"))
###################################################################################################################################################################

#COMPUTE AVERAGE TIME

def compute_average(list):
    n =  len(list)
    start =  time()
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[j],list[i]  = list[i], list[j]
    end =  time()
    return (end - start) / n
###################################################################################################################################################################
#Find the time of execution

def linear_search(list, item):
    found =  True
    start =  datetime.now()
    for i in list:
        if i == item:
            found =  True
    end =  datetime.now()
    elapsed_time =  (end -  start)
    return f"{found} Time Elapsed  Seconds: {elapsed_time.seconds} Micro Seconds: {elapsed_time.microseconds}"


###################################################################################################################################################################
#Download a file if it does not exist
def download_file(url,path, filename):
    with open("config.json", "r") as json_:
        file_json =  json.load(json_)
        if file_json["downloaded"] == True and file_json["url"] ==  url and os.path.exists(f"{filename}.csv"):
                print("File has been already downloaded")
        else:
            request =  requests.get(url)
            if request.status_code != 200:
                print("Bad request")
            else:
                if os.path.exists(path):
                    p= os.chdir(path)
                    config_file["file_name"] =  filename
                    config_file["url"] += url
                    content_tile =  request.content
                    with open(f"{filename}.csv", "wb") as file_write:
                        file_write.write(content_tile)
                    with open("config.json", "w")as json_write:
                        config_file["downloaded"] = True
                        current_time = datetime.date.today()
                        formatted_time = datetime.date.strftime(current_time, "%y %B %d")
                        json_file = json.dumps(config_file, indent=4)
                        config_file["downloaded_time"] =  formatted_time
                        config_file["path"] = path
                        json_write.write(json_file)
                        print("File has been successfully downloaded")
                else:
                    raise Exception("Path does not exist")







###################################################################################################################################################################

