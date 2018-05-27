import re



text = 'abbaaabbbbaaaaa'

pattern = 'ab'
count = 0

#how many matches
for match in re.findall(pattern, text):
    count += 1
    print('Found {!r}'.format(match))

print("# matches of {!r}". format(pattern), ': ', count)

# return indices of matches
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print('INDEX: ',s,' ', e )
    print('Found {!r} at {}:{}'.format(
    text[s:e], s, e))


# regex "www.*.com"
str_ex = input('ENTER URL: ')
site_check = re.search(r'www.*.com',str_ex)
#assert choice in lst_choice, str(choice) +' IS NOT AN OPTION'

assert site_check is not None,"URL NOT VALID"
