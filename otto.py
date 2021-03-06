###############################################################################
#Otto is an emotional robot that answers accordingly to what you say to her
###############################################################################
from lib import record, speech_to_text, tone_analyzer, output

#record what user has to say and save to ./records/user-record.wav
record.record()

#send the audio to the ibm speech-to-text api and get their json response
transcript=speech_to_text.stt()

#pass the transcript to the tone analyzer api, which recognizes emotions
emotion=tone_analyzer.getPredominantEmotion(transcript)

output.sound(emotion)