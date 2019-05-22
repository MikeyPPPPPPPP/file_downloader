use python 3.4

import requests
s = ('')#enter full url
#ex: https://www.tutorialspoint.com/ethical_hacking/ethical_hacking_tutorial.pdf
#ex: https://www.scrapmaker.com/download/data/wordlists/dictionaries/rockyou.txt
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename
    

download_file(s)
print ('done')

