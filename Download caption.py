from pytube import YouTube

link = input('Please enter the link :')
source = YouTube(link)


en_caption = source.captions.get_by_language_code('en')

en_caption_convert_to_srt = (en_caption.generate_srt_captions())

print(en_caption_convert_to_srt)
# save the caption to a file named Output.txt
text_file = open("Caption.txt", "w")
text_file.write(en_caption_convert_to_srt)
text_file.close()
