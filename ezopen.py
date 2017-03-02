import sys
import webbrowser
from subprocess import call

# call(['open', '/Users/danielburke/Documents/gyro_free_baby.csv'])
# sites = {'main':['https://canvas.rice.edu/courses/1229/pages/homework-4'],
#          '1':['https://canvas.rice.edu/courses/1229/assignments/13913','https://www.overleaf.com/8394720zfdrxrqdbphm#/29766093/'],
#          '2':['https://canvas.rice.edu/courses/1229/assignments/13914','https://www.overleaf.com/8394759dstsmcgngpfv'],
#          '3':['https://canvas.rice.edu/courses/1229/assignments/13915','https://www.overleaf.com/8394761qdxzyvnympqn#/29766224/']
#         }

def read_var(filename):
    with open(filename) as f:
        g = eval(f.read())
    return g

def write_var(var, filename):
    with open(filename, 'w') as f:
        f.write(repr(var))

def ask_yes_no(question):
    while True:
        response = raw_input(question)
        if response == 'n':
            said_yes = False
            break
        elif response == 'y':
            said_yes = True
            break
        else:
            print "Couldn't recognize that one! Type 'y' or 'n' (no quotes)."
    return said_yes

sites = {}
files = {}

if 'options' in sys.argv:
    sites = read_var('sites')
    for keyword in sites:
        print keyword

# SETUP MODE
elif 'setup' in sys.argv:
    first_time = False
    if 'firsttime' in sys.argv:
        first_time = True
    print ''
    print '----------------------------------------------------'
    print 'Setup engaged!'
    print ''

    more_keywords = True
    while more_keywords:
        if first_time:
            print '**Enter the keyword that you will use to open certain files and websites.**'
            print ''

        keyword = raw_input('Keyword: ')
        sites[keyword] = set([])
        files[keyword] = set([])

        # get websites
        print '----------------------------------------------------'
        print ''
        print '-- Website entry --'

        if first_time:
            print ''
            print '**In this section, you enter all of the websites that you want typing "', keyword, '" to cause to open, one at a time.**'
            print ''

        while True:
            # check if they want to add a website
            if not ask_yes_no('Add a website? (y/n): '):
                break
            url = raw_input('Site URL: ')
            print ''
            sites[keyword].add(url)

        print '----------------------------------------------------'

        # get files
        print ''
        print '-- File entry --'
        if first_time:
            print ''
            print '**In this section, you enter all of the files that you want typing "', keyword, '" to cause to open, one at a time.**'
            print ''
        print '*TIP* Drag and drop files into Terminal window to quickly add path.'
        print ''
        while True:
            if not ask_yes_no('Add a file? (y/n): '):
                break
            path = raw_input('File path: ')
            print ''
            files[keyword].add(path.strip())

        print '----------------------------------------------------'
        print ''
        print 'Keyword complete!'
        print ''
        more_keywords = ask_yes_no('Create another keyword? (y,n): ')
        print ''

    print 'Setup complete!'
    print ''

    if first_time:
        print "You're ready to use ezopen! Once you're in the correct directory in Terminal, type the following:"
        print ''
        print 'python ezopen.py "keyword"'
        print ''
        print '...where "keyword" is the desired keyword (without quotes).'
        print ''


    # write these dictionaries so they can we used again
    write_var(sites, 'sites')
    write_var(files, 'files')

# EDIT MODE
# elif 'edit' in sys.argv:
#     raw_input('What do you want to change? OPTIONS -- ("new keyword", "edit keyword")')

# OPEN THINGS MODE
else:
    preferences_saved = True

    try:
        sites = read_var('sites')
        files = read_var('files')
    except:
        preferences_saved = False
        print 'No options saved. Run setup.'
    if preferences_saved:
        for keyword in sites:
            if keyword in sys.argv:
                for site in sites[keyword]:
                    webbrowser.open(site)

        for keyword in files:
            if keyword in sys.argv:
                for file_path in files[keyword]:
                    if call(['open', file_path]) == 1:
                        print 'Make sure file paths have no spaces and are correct. May require name changes to directory and/or file name.'
