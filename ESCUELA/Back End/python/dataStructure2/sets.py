# Sets
# unique collections of items
# cant have duplicates values
# makiings sets

from this import d


languages = {'javascript', 'python', 'ruby'}

voted_languages = ['ruby', 'python3', 'javascript', 'python3']

set_voted = set(voted_languages)

set('$%#*')  # {'$','%','#','*'}

# methods
'ruby' in languages  # True

languages.add('scala')  # add it

languages.pop()  # random item is removed and return

languages.remove('ruby')  # removes ruby
languages.add('java')


moods = {'happy', 'sad', 'grumpy'}

dwarfs = {'happy', 'grumpy', 'doc'}

moods | dwarfs


lemon = {
    'sour', 'yellow', 'fruit', 'bumpy'
}
banana = {
    'fruit', 'smooth', 'sweet', 'yellow'}
