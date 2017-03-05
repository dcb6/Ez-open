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

def add_websites(sites,files,first_time,keyword):
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

def add_files(sites,files,first_time,keyword):
    print '----------------------------------------------------\n'
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

def add_keyword(sites,files,first_time):
    keyword = raw_input('Keyword: ')
    if keyword == 'exit':
        sys.exit()

    sites[keyword] = set([])
    files[keyword] = set([])

    add_websites(sites, files, first_time, keyword)
    add_files(sites, files, first_time, keyword)

def setup():
    sites = {}
    files = {}

    first_time = False
    if 'firsttime' in sys.argv:
        first_time = True
    print '\n----------------------------------------------------'
    print 'Setup engaged!\n'

    more_keywords = True

    # loop while user still has keywords to create
    while more_keywords:
        add_keyword(sites, files, first_time)

        print 'Keyword complete!\n'
        more_keywords = ask_yes_no('Create another keyword? (y,n): \n')

    if ask_yes_no('\nSave setup? This will override any previous setups. (y/n) :'):
        # write these dictionaries so they can we used again
        write_var(sites, 'sites')
        write_var(files, 'files')

        print '\n----------------------------------------------------'
        print 'Setup complete!\n'


        if first_time:
            print "You're ready to use ezopen! Once you're in the correct directory in Terminal, type the following:\n"
            print 'python ezopen.py "keyword"\n'
            print '...where "keyword" is the desired keyword (without quotes).\n'
    else:
        print '\n----------------------------------------------------'
        print '\nSetup complete, no changes saved.\n'

def open_up():
    preferences_saved = True

    try:
        sites = read_var('sites')
        files = read_var('files')
    except:
        preferences_saved = False
        print 'No options saved. Run setup.'

    # open everything for each keyword if there are preferences_saved
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

def list_options():
    sites = read_var('sites')
    keywords = set([])
    for keyword in sites:
        keywords.add(keyword)
    print keywords

def find_keyword(message,sites):
    invalid_keyword = True
    while invalid_keyword:
        keyword = raw_input(message)
        if keyword == 'exit':
            sys.exit()
        if not keyword in sites:
            print 'Keyword does not exist. Try again. '
        else:
            invalid_keyword = False
    return keyword

def edit():
    preferences_saved = True
    try:
        sites = read_var('sites')
        files = read_var('files')
    except:
        preferences_saved = False
        print 'No options saved. Running setup...'
        setup()

    if preferences_saved:
        while ask_yes_no('Delete a keyword? (y/n): '):
            keyword = find_keyword('Enter keyword to be deleted: ', sites)
            sites.pop(keyword)
            files.pop(keyword)

        while ask_yes_no('Add another keyword? (y/n): '):
            add_keyword(sites, files, False)

        while ask_yes_no('Add to existing keyword? (y/n): '):
            keyword = find_keyword('Enter keyword to edit: ', sites)
            add_websites(sites, files, False, keyword)
            add_files(sites, files, False, keyword)

        if ask_yes_no('Save edits? (y/n): '):
            write_var(sites, 'sites')
            write_var(files, 'files')
            print 'Edits saved.'
        else:
            print 'Edits not saved.'

# list available keywords
if 'options' in sys.argv:
    list_options()

# SETUP MODE
elif 'setup' in sys.argv:
    setup()

# EDIT MODE
elif 'edit' in sys.argv:
    edit()

# OPEN THINGS MODE
else:
    open_up()
