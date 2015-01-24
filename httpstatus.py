from BaseHTTPServer import BaseHTTPRequestHandler

responses = BaseHTTPRequestHandler.responses

def find_statuses(status=''):
    '''Find all http status that start with specified status
    
    >>> find_statuses(200)
    [200]
    >>> find_statuses(20) # doctest:+ELLIPSIS
    [200, 201, ..., 206]
    >>> find_statuses(2)  # doctest:+ELLIPSIS
    [200, 201, ..., 206]
    >>> find_statuses()   # doctest:+ELLIPSIS
    [200, 201, ..., 505]
    '''

    status = str(status)
    return [s for s in responses if str(s).startswith(status)]

def build_message(status, left_width):
    r'''Build string represents http status

    >>> build_message(200, 7) # doctest:+ELLIPSIS
    '200 OK  | Request...'
    '''
    status = int(status)
    res = responses[status]
    return '{0} {1}{2} | {3}'.format(
        status,
        res[0],
        ' ' * (left_width - (len('xxx ') + len(res[0]))),
        res[1]
    )

def httpstatuses(status=''):
    ''' Get http statutses
    
    >>> httpstatuses(200) # doctest:+ELLIPSIS
    ['200...']
    >>> httpstatuses(20)  # doctest:+ELLIPSIS
    ['200...', ..., '206...']
    >>> httpstatuses(2)   # doctest:+ELLIPSIS
    ['200...', ..., '206...']
    >>> httpstatuses()    # doctest:+ELLIPSIS
    ['200...', ..., '505...']
    '''
    statuses = find_statuses(status)
    # left_width is len('xxx most_long_summary')
    left_width = len('xxx ') + max(map(lambda x: len(responses[x][0]), statuses))
    return [build_message(s, left_width) for s in statuses]

def print_httpstatuses(status=''):
    print('\n'.join(httpstatuses(status)))
