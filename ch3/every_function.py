languages = ['Spanish', 'French', 'Italian',
             'Turkish', 'English', 'German']

print(languages)
languages.append('Chinese')
print(languages)
languages.insert(4, 'Hindi')
print(languages)
languages.remove('Italian')
print(languages)
chinese = languages.pop(-1)
print(languages)

print(sorted(languages))

languages.reverse()
print(languages)
languages.reverse()
print(languages)

languages.sort()
print(languages)

print(len(languages))
