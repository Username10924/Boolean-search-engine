# Boolean-search-engine

A simple boolean search engine

Instructions:  
Use the boolean_search function where the first parameter is your query and the second is the inverse index which was created from the create_index function

Query format:

Spaces indicate OR  
& indicates and  
samsung sony&tv will mean samsung OR (sony AND tv)

samsung&sony tv will mean (samsung AND sony) OR tv
