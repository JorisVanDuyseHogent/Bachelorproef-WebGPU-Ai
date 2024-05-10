import whisper
import time
import torch
from collections import defaultdict
import statistics

n = 5
models_to_test = ["tiny", "base", "small", "medium", "large"]
devices_to_test = ["cuda", "cpu"]
vram_requirements = {
  "tiny" : 1_700_000_000
  , "base" : 2_700_000_000
  , "small" : 3_500_000_000
  , "medium" : 6_100_000_000
  , "large" : 10_000_000_000
}

results = defaultdict(list)

if not torch.cuda.is_available():
  print('CUDA not available, skipping CUDA')
  devices_to_test.remove("cuda")

begin = time.time()
audio = whisper.load_audio("./IHaveSeenThings.m4a")
for device_name in devices_to_test:
  for model_name in models_to_test:
    if torch.cuda.mem_get_info()[0] < vram_requirements.get(model_name) and device_name == "cuda":
      print(f"Skipping {device_name}_{model_name} because of insufficient memory: ~{str(vram_requirements.get(model_name) - torch.cuda.mem_get_info()[0])}")
      continue

    model = whisper.load_model(model_name, device_name)
    for i in range(n):
      before_inference = time.time()
      result = model.transcribe(audio)
      after_inference_time = time.time()

      results[device_name + '_' + model_name].append(
        (after_inference_time - before_inference) * 1000
      )
    del model
    torch.cuda.empty_cache()
    print(f"Done testing {str(n)} times model: {model_name} on device {device_name}")

# Print test results
for test_key in results.keys():
  print(f"result for {test_key}:")
  temp_results = results.get(test_key)
  fastest = min(temp_results)
  slowest = max(temp_results)
  median = statistics.median(temp_results)
  for result in temp_results:
    print(f"\t-\t{round(result)} ms")
  print(f"\tlow: {round(fastest)} high: {round(slowest)}\n\tlow%: {round((median-fastest) * 100 / median, 2)}% high%: {round((slowest-median) * 100 / slowest, 2)}%\n")
print(f"total time ran: {str(round(time.time() - begin))} seconds")