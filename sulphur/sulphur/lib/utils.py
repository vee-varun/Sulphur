def first_word(str):
    return str.split(' ')[0]
    
def link_to_slug(string):
    if string[:4]=='http' or string[:5]=='https':
        return (string.split('/',3))[3]
    else:
        return (string.split('/',1))[1]