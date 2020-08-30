import requests

chunk_size = 256


url = "http://s18.uptofiles.net//files/Tamil%20Dubbed%20Movies/Shutter%20Island%20(2010)/Mp4%20HD%20(640x360)/Shutter%20Island%20(2010)%20Single%20Part%20(640x360).mp4"
r=requests.get(url, stream=True)
print("getteed")

with open('hacked.mp4','wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)




print("finished")