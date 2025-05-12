# dictionaries


band = {
    "vocals": "a",
    "guitar": "Page"
}

# both are the same above and below
band2 = dict(vocals="a", guitar="Page")
print(band)
print(band2)
print(len(band))
print(type(band))
# access
# both the same
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())
print(band.values())
# list of key and values
print(band.items())
# key is present
print("guitar" in band)
print("bac" in band)

# change values
band["vocals"] = 'abcd'
print(band)
band.update({"abc": 'ABC'})
print(band)

# remove item
# band["vocals"]=''
# print(band)
print(band.pop("abc"))
print(band)
# tuple
print(band.popitem())  # returns as tuple ('guitar', 'Page')
print(band)

# delete
band["drums"] = 'lal'
band["drums1"] = 'lal'
band["drums2"] = 'lal'
print(band)
del band["drums"]
print(band)
# delete al items
# band.clear()
# print(band)

# del band2
# print(band)

# copy dictionaries
# band2=band #create a reference
# #if u edit band2 then band get affected
# band2["guitar"]='ginny'
# print(band)

band2 = band.copy()
print(band2)
band2["guitar"] = 'ginny'
print(band2)
print(band)

# nested dictionaries
member1 = {
    'class': 'a',
    'section': 'c',
    'classroom': 'vocals'
}
member2 = {
    'class': 'b',
    'section': 'x',
    'classroom': 'ground'
}
school = {
    'member1': member1,
    'member2': member2,
}
print(school)
print(school['member1'])
# print(school[][][]..) of that dic with that item
print(school['member1']['section'])
print(school.pop('member1'))
print(school)

# sets
nums = {1, 2, 3, 4, 3}
nums1 = set(nums)
print(nums1)
# True ==1 False ==0
nummy = {1, True, 2, 3, False, 0}
print(nummy)  # o/p {False, 1, 2, 3}  false means 0

print(2 in nummy)
# add a new element
nummy.add(23)
print(nummy)
# u can use update to add tuple,list and dict to set
nummy.update(nums)
print(nummy)

# merge 2 sets
one = {1, 2, 4, 6, 4}
two = {7, 8, 9, 10}
print(one.union(two))
print(one)
# all elements that are in this set but not the others
one.difference(two)
print(one)

# keep everything except duplicate
three = {1, 2, 3, 4, 5}
four = {4, 5, 3, 6, 7}
three.symmetric_difference(four)
print(three)  # {1, 2, 3, 4, 5}
