def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (m,s)=time_string.split(splitter)
    return(m,s)


print(sanitize('3-12'))


