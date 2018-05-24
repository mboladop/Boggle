List Comprehension Challenges
Example:
Question 
                range(10) 
                -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Answer
                [n * 2 for i in range(10)]
1. range(5) 
-> ["*", "*", "*", "*", "*"]
([i=* for i in range(5)])

2. ["Hi", "There", "Everyone"] 
-> [2, 5, 8]
([len(i) for i in range l])

3. range(8) 
-> [0, 1, 4, 9, 16, 25, 36, 49]
([ i*i  for i in range 8])

4. range(5) 
-> [(0,1), (1,2), (2,3), (3,4), (4,5)]
([ (i,i+1) for i in range(5)])

5. 'woohoo' 
-> ['w', 'o', 'o', 'h', 'o', 'o']
([list(i)])

6. ['car', 'cat', 'maps', 'if', 'level'] 
-> [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
([(i, len(i)) for i in l])

7. [(False, False), (False, True), (True, False), (True, True)]
->[False, False, False, True]
([ (i[0] and i[1] ) for i in range l])

8. [(False, False), (False, True), (True, False), (True, True)]
->[False, True, True, True]
([ (i[0] or i[1]) for i in l])

1. ['Hi', 'There', 'Everyone'] 
-> {'Hi':2, 'There':5, 'Everyone':8}

2. 'code'
-> {'c': 99, 'e': 101, 'd': 100, 'o': 111}

3. ['car', 'cat', 'maps', 'if', 'level'] 
-> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}