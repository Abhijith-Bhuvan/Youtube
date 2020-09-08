from youtube_dl import YoutubeDL as youtube

link = input('Please enter the link :')

opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
youtube(opts).download([link])
