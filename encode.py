import wave
song_name=input('enter the name of the wave song')
song_name+='.wav'
sound=wave.open(song_name,'rb')
barr=bytearray(list(sound.readframes(sound.getnframes())))
print('maximum no of characters in your secret message can be,',(len(barr)//8))
sec_msg=input('enter the input string')
while True:
    if (len(sec_msg)*8)>=len(barr):
        sec_msg=input('enter the input string')
    else:
        break
modified_sec_msg=sec_msg+int((len(barr)-(len(sec_msg)*8))/32)*'#@!&'
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in modified_sec_msg])))
frame=[]
for i,bit in enumerate(bits):
    frame.append((barr[i] & 254) | bit)
frame_modified = bytes(frame)
with wave.open('nishant.wav', 'wb') as fd:
    fd.setparams(sound.getparams())
    fd.writeframes(frame_modified)
sound.close()
