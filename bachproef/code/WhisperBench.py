import whisper
import time
import torch
from collections import defaultdict
import statistics

BEGIN_TIME = time.time()
VRAM_REQUIRED = {
  "tiny" : 1_700_000_000
  , "base" : 2_700_000_000
  , "small" : 3_500_000_000
  , "medium" : 6_100_000_000
  , "large" : 10_000_000_000
}
PARAMS = {
  "tiny" : 39
  , "base" : 74
  , "small" : 244
  , "medium" : 769
  , "large" : 1550
}

def main():
  # Defines how many runs each model on each device must do.
  # Allows for more data to be generated.
  number_of_runs = 1
   
  # Allows to select which models should be tested.
  # If a model can't run on a cuda device, it will be skipped.
  models_to_test = [
    # "tiny"
    # , "base"
    # , "small"
     "medium"
    # "large"
  ]

  # Selected devices that will be tested,
  # If CUDA is not supported, it will be not be tested.
  devices_to_test = [
    "cuda"
    , "cpu"
  ]
  results = runBenchMark(models_to_test, devices_to_test, number_of_runs)
  printResultsToTerminal(results)
  generateDatFilesForLatex(results)

def runBenchMark(models_to_test: list, devices_to_test: list, n: int) -> defaultdict:
  results = defaultdict(list)
  cuda_available = torch.cuda.is_available()
  if not cuda_available:
    print('CUDA not available, skipping CUDA, install toch with CUDA enabled!')
    devices_to_test.remove("cuda")

  audio = whisper.load_audio("./IHaveSeenThings.m4a")
  for device_name in devices_to_test:
    for model_name in models_to_test:
      print(f"Started testing model {model_name.upper()} on {device_name.upper()} {str(n)} times")

      if cuda_available and torch.cuda.mem_get_info()[0] < VRAM_REQUIRED.get(model_name) and device_name == "cuda":
        print(f"Skipping {device_name}_{model_name} because of insufficient memory: ~{str(VRAM_REQUIRED.get(model_name) - torch.cuda.mem_get_info()[0])}")
        continue


      model = whisper.load_model(model_name, device_name)
      for i in range(n):
        before_inference = time.time()
        result = model.transcribe(audio)
        after_inference_time = time.time()
        
        print(f"\tRan {device_name}_{model_name} ({i + 1}/{n}), remaining time: {round((after_inference_time - before_inference) * (n - (i + 1)))}s")

        results[device_name + '_' + model_name].append(
          (after_inference_time - before_inference) * 1000
        )
      del model
      torch.cuda.empty_cache()
      print(f"Finished testing model {model_name.upper()} on {device_name.upper()} {str(n)} times")
  return results

# Print test results
def printResultsToTerminal(results: defaultdict):
  for test_key in results.keys():
    print(f"result for {test_key}:")
    temp_results = results.get(test_key)
    fastest = min(temp_results)
    slowest = max(temp_results)
    median = statistics.median(temp_results)
    for result in temp_results:
      print(f"\t-\t{round(result)} ms")
    print(f"\tlow: {round(fastest)} high: {round(slowest)}\n\tlow%: {round((median-fastest) * 100 / median, 2)}% high%: {round((slowest-median) * 100 / slowest, 2)}%\n")
  print(f"total time ran: {str(round(time.time() - BEGIN_TIME))} seconds")

# Generate .dat files for latex
def generateDatFilesForLatex(results: defaultdict):
  averages_dat_file = open("WhisperBench_averages.dat", "w")
  scatter_dat_file = open("WhisperBench_scatter.dat", "w")
  result_keys = list(results.keys())

  averages_dat_file.write(f"x\ty\n")
  scatter_dat_file.write(f"x\ty\tlabel\n") 

  for test_key in result_keys:
    id_letter = chr(97 + result_keys.index(test_key))
    temp_results = results.get(test_key)
    average = round(statistics.mean(temp_results))
    model_name = str(test_key).split('_')[1]
    model_params = PARAMS.get(model_name)
    averages_dat_file.write(f"{model_params}\t{average}\n")

    temp_results = results.get(test_key)
    for result in temp_results:
      scatter_dat_file.write(f"{model_params}\t{round(result)}\t{id_letter}\n")

  averages_dat_file.close()
  scatter_dat_file.close()

if __name__ == '__main__':
    main()