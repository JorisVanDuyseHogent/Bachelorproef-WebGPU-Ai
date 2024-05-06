# Nvidia Geforce GTX 1080 Ti
```PS
PS> Measure-Command { whisper .\IHaveSeenThings.m4a --language English --model small  --device cuda }
```

TotalSeconds      : 17.6023325
TotalSeconds      : 17.063286
TotalSeconds      : 17.3775252
TotalSeconds      : 17.3979507
TotalSeconds      : 17.4567227
TotalSeconds      : 17.5137898

## Xeon E5-2680 v2
```PS
PS> Measure-Command { whisper .\IHaveSeenThings.m4a --language English --model small  --device cpu }
```

TotalSeconds      : 57.788052   
TotalSeconds      : 58.6448482
TotalSeconds      : 58.614227
TotalSeconds      : 58.6115474
TotalSeconds      : 59.0725315
TotalSeconds      : 58.3733585


PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\transcribe.py:124: UserWarning: Performing inference on CPU when CUDA is available
  warnings.warn("Performing inference on CPU when CUDA is available")
PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\transcribe.py:126: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")


# Intel Core i9
```sh
hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
```
Time (abs ≡):        34.039 s
Time (abs ≡):        34.735 s
Time (abs ≡):        34.572 s
Time (abs ≡):        34.290 s
Time (abs ≡):        34.231 s
Time (abs ≡):        34.697 s


% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.039 s               [User: 63.629 s, System: 6.187 s]
 
% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.735 s               [User: 64.777 s, System: 6.372 s]
 
% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.572 s               [User: 63.886 s, System: 6.605 s]
 
% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.290 s               [User: 62.782 s, System: 6.998 s]
 
% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.231 s               [User: 63.028 s, System: 6.673 s]
 
% hyperfine --runs 1 --export-markdown ./WhisperTest.md --show-output 'whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu'
Benchmark 1: whisper ./IHaveSeenThings.m4a --language English --model small  --device cpu
/usr/local/lib/python3.11/site-packages/whisper/transcribe.py:115: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:09.000]  I've seen things that you people wouldn't believe.
[00:09.000 --> 00:16.000]  Attack ships on fire off the shoulder of a lion.
[00:16.000 --> 00:26.000]  I watched sea beans glitter in the dark near the 10-houser gate.
[00:26.000 --> 00:35.000]  All those moments will be lost in time.
[00:35.000 --> 00:46.000]  Like tears in rain.
[00:46.000 --> 00:50.000]  Time to die.
  Time (abs ≡):        34.697 s               [User: 63.956 s, System: 6.825 s]
