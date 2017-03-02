import sys
import webbrowser
from subprocess import call

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
        elif response == 'exit':
            sys.exit()
        else:
            print "Couldn't recognize that one! Type 'y' or 'n' (no quotes)."
    return said_yes

sites = {}
files = {}

# list available keywords
if 'options' in sys.argv:
    sites = read_var('sites')
    keywords = set([])
    for keyword in sites:
        keywords.add(keyword)

# SETUP MODE
elif 'setup' in sys.argv:
    first_time = False
    if 'firsttime' in sys.argv:
        first_time = True
    print '\n----------------------------------------------------'
    print 'Setup engaged!\n'

    more_keywords = True

    # loop while user still has keywords to create
    while more_keywords:
        if first_time:
            print '**Enter the keyword that you will use to open certain files and websites.**\n'

        keyword = raw_input('Keyword: ')
        if keyword == 'exit':
            sys.exit()

        sites[keyword] = set([])
        files[keyword] = set([])

        # get websites
        print '----------------------------------------------------\n'
        print '-- Website entry --'

        if first_time:
            print '\n**In this section, you enter all of the websites that you want typing "', keyword, '" to cause to open, one at a time.**\n'

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
            print '\n**In this section, you enter all of the files that you want typing "', keyword, '" to cause to open, one at a time.**\n'
        print '*TIP* Drag and drop files into Terminal window to quickly add path.\n'
        while True:
            if not ask_yes_no('Add a file? (y/n): '):
                break
            path = raw_input('File path: ')
            print ''
            files[keyword].add(path.strip())

        print '----------------------------------------------------\n'

        print 'Keyword complete!\n'
        more_keywords = ask_yes_no('Create another keyword? (y,n): \n')

    if ask_yes_no('\nSave setup? This will override any previous setups. (y/n) :'):
        # write these dictionaries so they can we used again
        write_var(sites, 'sites')
        write_var(files, 'files')

        print 'Setup complete!\n'


        if first_time:
            print "You're ready to use ezopen! Once you're in the correct directory in Terminal, type the following:\n"
            print 'python ezopen.py "keyword"\n'
            print '...where "keyword" is the desired keyword (without quotes).\n'
    else:
        print '\n----------------------------------------------------'
        print '\nSetup complete, no changes saved.\n'



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
                        print 'Make sure file path is correct.'
