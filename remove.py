punctations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str="hello! it's me......................&%$$$$#$%^^ your;s frined"
no_punct=""
for char in my_str:
    if char not in punctations:
       no_punct=no_punct+char

print no_punct
