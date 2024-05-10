> pip3 install torch torchvision==0.15.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu117


## Intel Xeon E5-2680 v2
Done testing 5 times model: tiny on device cpu
Done testing 5 times model: small on device cpu
Done testing 5 times model: medium on device cpu
result for cpu_tiny:
        11388.813018798828 ms
        9762.03179359436 ms  
        6787.021160125732 ms
        9846.840620040894 ms
        9827.588081359863 ms
result for cpu_small:
        17668.397903442383 ms
        17925.168752670288 ms
        18300.84538459778 ms
        18210.004568099976 ms
        17923.45380783081 ms
result for cpu_medium:
        49472.808837890625 ms
        50202.45671272278 ms
        49460.856437683105 ms
        49535.13717651367 ms
        49705.63054084778 ms

result for cuda_large:
        -       18279 ms
        low: 18279 high: 18279
        low%: 0.0% high%: 0.0%

result for cpu_large:
        -       117852 ms
        low: 117852 high: 117852
        low%: 0.0% high%: 0.0%

total time ran: 206 seconds

Done testing 5 times model: tiny on device cuda
Done testing 5 times model: base on device cuda
Done testing 5 times model: small on device cuda
Done testing 5 times model: medium on device cuda
Done testing 5 times model: large on device cuda
C:\Users\qwertic\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\transcribe.py:124: UserWarning: Performing inference on CPU when CUDA is available
  warnings.warn("Performing inference on CPU when CUDA is available")
C:\Users\qwertic\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\transcribe.py:126: UserWarning: FP16 
is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
Done testing 5 times model: tiny on device cpu
Done testing 5 times model: base on device cpu
Done testing 5 times model: small on device cpu
Done testing 5 times model: medium on device cpu
Done testing 5 times model: large on device cpu
result for cuda_tiny:
        -       6867 ms
        -       6600 ms
        -       7400 ms
        -       3836 ms
        -       3461 ms
        low: 3461 high: 7400      
        low%: 47.57% high%: 10.81%

result for cuda_base:
        -       2634 ms
        -       2568 ms
        -       2600 ms
        -       2560 ms
        -       2560 ms
        low: 2560 high: 2634      
        low%: 0.31% high%: 2.52%  

result for cuda_small:
        -       3638 ms
        -       3629 ms
        -       3637 ms
        -       3632 ms
        -       3602 ms
        low: 3602 high: 3638
        low%: 0.83% high%: 0.14%

result for cuda_medium:
        -       7845 ms
        -       7738 ms
        -       7865 ms
        -       7684 ms
        -       7821 ms
        low: 7684 high: 7865
        low%: 1.75% high%: 0.57%

result for cuda_large:
        -       28017 ms
        -       22733 ms
        -       39174 ms
        -       22103 ms
        -       38586 ms
        low: 22103 high: 39174
        low%: 21.11% high%: 28.48%

result for cpu_tiny:
        -       9503 ms
        -       8631 ms
        -       9156 ms
        -       9556 ms
        -       10114 ms
        low: 8631 high: 10114
        low%: 9.18% high%: 6.04%

result for cpu_base:
        -       6575 ms
        -       6646 ms
        -       6740 ms
        -       6588 ms
        -       6580 ms
        low: 6575 high: 6740
        low%: 0.2% high%: 2.27%

result for cpu_small:
        -       18657 ms
        -       18447 ms
        -       18708 ms
        -       18667 ms
        -       18383 ms
        low: 18383 high: 18708
        low%: 1.46% high%: 0.28%

result for cpu_medium:
        -       51120 ms
        -       51651 ms
        -       52147 ms
        -       51672 ms
        -       50691 ms
        low: 50691 high: 52147
        low%: 1.86% high%: 0.95%

result for cpu_large:
        -       118547 ms
        -       118525 ms
        -       201059 ms
        -       144454 ms
        -       142315 ms
        low: 118525 high: 201059
        low%: 16.72% high%: 29.22%

total time ran: 1522 seconds

## 2x Xeon E5-2680 V3 + GTX 1050 Ti
result for cuda_tiny:
        -       2555 ms
        -       1557 ms
        -       1574 ms
        -       1569 ms
        -       1557 ms
        low: 1557 high: 2555
        low%: 0.78% high%: 38.59%

result for cuda_base:
        -       2023 ms
        -       2003 ms
        -       2012 ms
        -       2003 ms
        -       2002 ms
        low: 2002 high: 2023
        low%: 0.07% high%: 0.96%

result for cuda_small:
        -       3819 ms
        -       3796 ms
        -       3807 ms
        -       3810 ms
        -       3802 ms
        low: 3796 high: 3819
        low%: 0.29% high%: 0.32%

result for cpu_tiny:
        -       2385 ms
        -       3493 ms
        -       4062 ms
        -       4296 ms
        -       4001 ms
        low: 2385 high: 4296
        low%: 40.39% high%: 6.87%

result for cpu_base:
        -       2554 ms
        -       2221 ms
        -       2291 ms
        -       2224 ms
        -       2228 ms
        low: 2221 high: 2554
        low%: 0.32% high%: 12.75%

result for cpu_small:
        -       4797 ms
        -       4799 ms
        -       4554 ms
        -       4865 ms
        -       4404 ms
        low: 4404 high: 4865
        low%: 8.19% high%: 1.4%

result for cpu_medium:
        -       14498 ms
        -       12806 ms
        -       12680 ms
        -       12382 ms
        -       11678 ms
        low: 11678 high: 14498
        low%: 7.9% high%: 12.54%

result for cpu_large:
        -       34987 ms
        -       39026 ms
        -       49144 ms
        -       53651 ms
        -       29573 ms
        low: 29573 high: 53651
        low%: 24.22% high%: 27.26%