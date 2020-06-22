#Derek Altman
#daltma3
#CS111
#Project 4
#Monday at 4:00pm
#Hiding a text message using steganography

#The purpose of this function is to smooth the last values of a sound so that a sound can be encoded into it
#The vaiable sound is the sound that will be smoothed
#The return value is a sound with the smoothed sample values
def smoothSound(sound):
  #get samples from the sound
  samples = getSamples(sound)
  #loop through samples in sound
  for i in range(0, getLength(sound), 1):
    #get sample values from sample
    sampleVal = getSampleValue(samples[i])
    #use mod 128 to smooth the sound
    smooth = sampleVal % 128
    #create a new value with rhe smoothed value
    newVal = sampleVal - smooth
    #set the sample to the new smoothed value
    setSampleValue (samples[i], newVal)
  
  return sound

#The purpose of this function is to encode a message into a sound file
#The paramenter sound is the sound that will have the message encoded into it
#the return value is the samples with the encoded message
def encode(sound):
  #get the samples from the sound
  samples = getSamples(sound)
  #prompt user to pick a message to encode into the sound
  message = requestString("Type a message to hide in audio file")
  #get length of the message
  length = len(message)
  #loop through the message to encode the message
  for i in range(0, length, 1):
    #make the characters into numbers
    num = ord(message[i])
    #get sample values from the sound
    sampleVal = getSampleValue(samples[i])
    #set the sample values to the values with the encoded message values
    setSampleValue(samples[i], sampleVal + num)
    
  return samples
  
#The purpose of this function is to extract the encoded message from the sound file
#The variable sound is the sound with the encoded message 
def extractMess(sound):
  #get samples from sound
  samples = getSamples(sound)
  #get sampling rate from the sound
  rate = getSamplingRate(sound)
  #determine length of a byte
  byte = getLength(sound)/rate
  #make length of byte 1 to get one character
  length = byte/8
  #create an empty string
  string = ""
  #loop over sound one byte at a time
  for i in range(0, getLength(sound), (byte/8)):
    #determine sample value at each byte
    value = getSampleValueAt(sound, i) % 128
    #if value is over 0 add to string
    if (value > 0):
       letter = chr(value)
       string = string + letter
    #if value is less than 0 stop the program
    else:
      break
  #show the encoded message
  showInformation(string)
  
#Run the program

#Prompt user to either encode or extract a message
number = requestIntegerInRange("Choose 1 to encode message or 2 to extract message", 1, 2)
#if user enters 1 then run program to encode message 
if (number == 1):
  showInformation("pick a sound file to encode your message into")
  #prompt user to pick a sound file
  fname = pickAFile()
  #make the file into a sound
  sound = makeSound(fname)
  explore (sound)
  #run function to smooth the sound values
  smoothSound(sound)
  explore (sound)
  #run function to encode the message into the sound
  encode(sound)
  showInformation("pick a file to save your encoded message to, then run program again to extract message")
  #prompt user to pick a file to save the encoded sound to
  fname2 = pickAFile()
  #save the encoded sound to the selected file
  writeSoundTo(sound, fname2)
#if user does noot select 1 then run program to extract the message
else:
  showInformation("pick the file with the encoded message")
  #prompt user to pick the file to extract the message from
  fname = pickAFile()
  #make the file into a sound
  sound = makeSound(fname)
  #run function to extract the message
  extractMess(sound)