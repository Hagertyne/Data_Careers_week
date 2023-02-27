print("Hello world")

inp= int("input your agea")

users = [
 { "id": 0, "name": "Hero" },
 { "id": 1, "name": "Dunn" },
 { "id": 2, "name": "Sue" },
 { "id": 3, "name": "Chi" },
 { "id": 4, "name": "Thor" },
 { "id": 5, "name": "Clive" },
 { "id": 6, "name": "Hicks" },
 { "id": 7, "name": "Devin" },
 { "id": 8, "name": "Kate" },
 { "id": 9, "name": "Klein" }
]


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# create empty list
for user in users:
    user["friends"] = []
    
    for i, j in friendships:
        #user i means user with id i
        user[i]["friends"].append(user[j] ) # add j as friend of i
        user[j]["friends"].append(user[i])



def number_of_friends(user):
    """how many friends does user have?"""
    return len(user["friends"]) #length of friends_id list
total_connections = sum(number_of_friends(user) for user in users) #gives 24
        


num_users = len(users) # length of the users list
avg_connections = total_connections / num_users 


#create a list (user_id,number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
#sort largest to smallest number  each paair is (user_id,num_friends)

# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
sorted(num_friends_by_id, key= lambda (user_id, num_friends , reverse=True):)

def friends_of_friends_ids_bad(user):
     """ foaf stands for friends of a friends"""
     return [foaf["id"] for friend in user["friends"] # for each user in friends
             for foaf in fried["friends"]] # to get each of their friends
     
 #calling this on user[0] (Hero) gives us[0, 2, 3, 0, 1, 3]
 # 0 is included twice since its friends with both a well as 
print([friend["id"] for   friend in user[0]["friends"]])# [1, 2]

print([friend["id"] for   friend in user[0]["friends"]])# [0, 2, 3]
print([friend["id"] for   friend in user[0]["friends"]]) # [0, 1, 3]

#lets import counter since it doesn't imported by default
from collections import counter 
def not_the_same(user, other_user):
    """two users are not hte same if they have different ids"""
    return user["id"] != other_user["id"]
def not_friends(user, other_user):
    """other user is not friend if he's not in user["friends];"""
    """ thats , if he's not the same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"] for friend in user["friends"] # for each of my friends
                   for foaf in friend["friends"]  # count *their* friends
                   if not_the_same((user,foaf) # who aren't me
                                   and not_friends(user,foaf)) # and aren't my friends
                   )
print(friends_of_friend_ids(user[3]))



#another program

interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientsts_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]

#lets build index for interests


from collections import defaultdict
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
 user_ids_by_interest[interest].append(user_id)


#keys are user_ids, values are lists of interests for that user_id
interes_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)


#Iterate over the user’s interests, For each interest, iterate over the other users with that interest,
# Keep count of how many times we see each other user.
def most_common_interests_with(user):
 return Counter(interested_user_id
 for interest in interests_by_user_id[user["id"]]
 for interested_user_id in user_ids_by_interest[interest]
 if interested_user_id != user["id"])
 
 
 #slary and experience
 salary_by_tenure = [(83000, 8.7), (88000, 8.1),(48000,0.7),(76000,6),(69000,6.5),(76000,7.5),
                     
                  (60000, 2.5), (83000, 10),
                  (48000, 1.9), (63000, 4.2)]
 
 # I am gonna continue from here
 # keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
 salary_by_tenure[tenure].append(salary)
# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
 tenure : sum(salaries) / len(salaries)
 for tenure, salaries in salary_by_tenure.items()
}

#It might be more helpful to bucket the tenures:
def tenure_bucket(tenure):
     if tenure < 2:
        return "less than two"
 
     elif tenure < 5:
       return "between two and five"
     else:
         
         return "more than five"
     
#Then group together the salaries corresponding to each bucket:
# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
 bucket = tenure_bucket(tenure)
 salary_by_tenure_bucket[bucket].append(salary)
 
 
 #And finally compute the average salary for each group:
# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
 tenure_bucket : sum(salaries) / len(salaries)
 for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}


interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
#Motivating Hypothetical: DataSciencester | 11
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]



words_and_counts = Counter(word
 for user, interest in interests
 for word in interest.lower().split())
#This makes it easy to list out the words that occur more than once:
for word, count in words_and_counts.most_common():
 if count > 1:
     print (word, count)
     
     

#Python 
#Whitespace Formatting
#Many languages use curly braces to delimit blocks of code. Python uses indentation:
for i in [1, 2, 3, 4, 5]:
     print (i )# first line in "for i" block
for j in [1, 2, 3, 4, 5]:
    print (j) # first line in "for j" block
    print (i + j) # last line in "for j" block
    print (i) # last line in "for i" block
    print ("done looping")

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# readable code

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [ [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9] ]

two_plus_three = 2 + 3

for i in [1, 2, 3, 4, 5]:
 # notice the blank line
 print(i)
 
 # Modules 
 
 # import the module itself:
import re
my_regex = re.compile("[0-9]+", re.I)

# already had a different re in your code you could use an alias:
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)


import matplotlib.pyplot as plt
#Importing specific values from module
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


