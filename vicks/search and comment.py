import ytc
from youtube_search import YoutubeSearch

# url = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk'
# url = 'tom and jerry'
url = input('\nEnter Video Title or URL : ')

s = url.split('/')
max_res = 1

while True:
    if s[0] != 'https:':
        vid = YoutubeSearch(s[0], max_results = max_res).to_dict()[-1]['id']
    else:
        if s[2] == 'www.youtube.com':
            vid = s[3].split('=')[1].split('?')[0]
        elif s[2] == 'youtu.be':
            vid = s[3].split('?')[0]
        else:
            vid = 'Cpc_rHf1U6g'
            print("Sorry... Code couldn't be extracted !!!")
    try:
        com = ytc.comments(vid)
        print(com)
        break
    except Exception as e:
        max_res += 1
        print(max_res)

print(vid, max_res)
