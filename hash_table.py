#creating a value from a string using a mathematical formula ie...guid
#a hash function maps a key to a character value of a certain length
#good hash
#1) easy to produce
#2) consistent / uniform distribution
#3) low collision
#example
#a: 0
#b: 1
#c: 2
#d: 3
#key for abcd would be 0123

#collision handling
#collision occurs when an existing key maps to an already occupied spot in the hash table
#one strategy is chaining which means each value in the hash table points to a linked list
#a linked list is a list object with multiple nodes
#but time complexity is O(n)
#ie...single key points to a linked list with n nodes
#open addressing
#values stored into the hash table itself - if the key is available just insert the value corresponding to that key
#linear probing
#seeking the key that corresponds to the hashed value
#when a collision occurs put the value into the next available slot in the list of keys
#comparison - chaining and open addressing
#chaining
#simple to implement
#key tables never get full
#performace is poor
#space is unknown because it can grow
#best when the number of keys is unknown

#open addressing
#harder to implement
#hash tables can get full
#good performance
#no extra space required
#used when the number of keys is known





