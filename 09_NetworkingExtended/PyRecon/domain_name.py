#from tld import get_tld # this gives the com ending and usually gave the full google.com 
from tld import get_fld # new way to get the full google.com

def get_domain_name(url):
	
    #domain_name = get_tld(url) # tld is the old way. 
    domain_name = get_fld(url)
    return domain_name

print(get_domain_name('https://www.google.com'))


