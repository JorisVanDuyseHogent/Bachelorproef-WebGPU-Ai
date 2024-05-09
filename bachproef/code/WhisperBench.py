import whisper
import time
n = 6
total_audio_load = 0
total_model_load = 0
total_inference = 0

for i in range(n):
  before_load_audio = time.time()
  audio = whisper.load_audio("./IHaveSeenThings.m4a")
  after_load_audio = time.time()

  before_load_model = time.time()
  model = whisper.load_model("small")
  after_load_model = time.time()

  before_inference = time.time()
  result = model.transcribe(audio)
  after_inference_time = time.time()

  total_audio_load += after_load_audio - before_load_audio
  total_model_load += after_load_model - before_load_model
  total_inference += after_inference_time - before_inference

print(result["text"])
print(
  'avg_audio_load: ' + str(total_audio_load * 1000 / n) + ' ms\n'
  'avg_model_load: ' + str(total_model_load * 1000 / n) + ' ms\n'
  'avg_inference: ' + str(total_inference * 1000 / n) + ' ms\n'
)