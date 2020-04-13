IN_PREFIXES = {
    'BA',
    'BS',
    'BUS MS',
    'Certificate',
    'Graduate Certificate',
    'MA',
    'Master of Arts',
    'Master\'s',
    'MBA/MA',
    'ME Certificate',
    'ME MD/PhD Program',
    'ME Program',
    'MS',
    'P.B.C.',
    'Post Bacc Certificate',
    'Post Baccalaureate Certificate',
    'Post Master\'s Cert',
    'Post-Baccalaureate Certificate',
    'Post-Masters Certificate'
}

# the order of this list matters!
# the algorithm removes the *first* matching prefix, so if "MBA" appears before
# "MBA Global", for example, then the major "MBA Global Finance" will become
# "Global Finance" and not "Finance"
SPACE_PREFIXES = [
    'BS',
    'BUS MBA Global -',
    'BUS MBA',
    'DRPH-PT,',
    'EDU M.Ed.',
    'EDU MS',
    'EDU PMC',
    'EN',
    'GC',
    'MA',
    'MBA Global -',
    'MBA',
    'MBA/MPH',
    'ME MA',
    'ME MS',
    'ME PhD',
    'MED',
    'ME',
    'MPH,',
    'MPH/MSW,',
    'MPH-PTIB,',
    'MPH-RES,',
    'MS,',
    'MS'
]
