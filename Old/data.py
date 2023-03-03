def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)


with open('jerry.txt') as jf:
    date=jf.readline()
jf_date=date.strip().split(',')

with open('justin.txt') as jsf:
    date=jsf.readline()
jsf_date=date.strip().split(',')

new_jf=[]
new_jsf=[]

for each_t in jf_date:
    new_jf.append(sanitize(each_t))
for each_t in jsf_date:
    new_jsf.append(sanitize(each_t))


print(sorted(new_jf))
print(sorted(new_jsf))



