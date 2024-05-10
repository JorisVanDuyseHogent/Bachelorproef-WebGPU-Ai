## Whisper + load audio + load model
x     y               label
769   57.788052       a
769   58.6448482      a
769   58.614227       a
769   58.6115474      a
769   59.0725315      a
769   58.3733585      a
769   34.039          b
769   34.735          b
769   34.572          b
769   34.290          b
769   34.231          b
769   34.697          b
769   17.6023325      c
769   17.063286       c
769   17.3775252      c
769   17.3979507      c
769   17.4567227      c
769   17.5137898      c

## Whisper Turbo GTX 1080 Ti
9709
9696
9714
9774
9750
10032

### inladen model op whisper turbo in ms
2600
2588
2564
2487
2594
2537

(3, 57788.052)(3, 58644.8482)(3, 58614.227)(3, 58611.5474)(3, 59072.5315)(3, 58373.3585)

## Whisper + Ratchet GTX 1080 Ti + WebGPU
8513
8272
8496
8633
8569
8105

## Whisper + Ratchet + Intel UHD graphics 630 + WebGPU
183262
183504
183467
183535

## Whisper CUDA + GTX 1080 Ti
avg_audio_load: 322.33421007792157 ms
avg_model_load: 5877.479434013367 ms
avg_inference: 3885.40252049764 ms

avg_audio_load: 323.17010561625165 ms
avg_model_load: 6073.374629020691 ms 
avg_inference: 3966.3426876068115 ms

avg_audio_load: 322.06010818481445 ms
avg_model_load: 5897.611538569133 ms
avg_inference: 3847.371459007263 ms

avg_audio_load: 321.48873805999756 ms
avg_model_load: 5857.141852378845 ms
avg_inference: 3822.498083114624 ms

avg_audio_load: 317.67483552296954 ms
avg_model_load: 5870.639403661092 ms
avg_inference: 3843.759775161743 ms

avg_audio_load: 318.2560205459595 ms
avg_model_load: 6069.873094558716 ms
avg_inference: 3911.6304318110147 ms


## Intel Xeon E5-2680 v2
avg_audio_load: 342.9399331410726 ms
avg_model_load: 5667.810161908467 ms
avg_inference: 18694.576660792034 ms

avg_audio_load: 341.1167462666829 ms
avg_model_load: 5432.727138201396 ms
avg_inference: 18592.004418373108 ms

avg_audio_load: 339.1610383987427 ms
avg_model_load: 5551.305532455444 ms
avg_inference: 18619.591514269512 ms

avg_audio_load: 342.6486651102702 ms
avg_model_load: 5436.391274134318 ms
avg_inference: 18729.684789975483 ms

avg_audio_load: 343.8936074574788 ms
avg_model_load: 5414.945642153422 ms
avg_inference: 18586.12863222758 ms

avg_audio_load: 337.42082118988037 ms
avg_model_load: 5395.05664507548 ms
avg_inference: 18658.95489851634 ms

## 2x Intel Xeon E5-2680 v3
avg_audio_load: 201.44975185394287 ms
avg_model_load: 6065.361022949219 ms
avg_inference: 4371.318777402242 ms

avg_audio_load: 193.51565837860107 ms
avg_model_load: 3612.543741861979 ms
avg_inference: 4382.500569025676 ms

avg_audio_load: 196.31218910217285 ms
avg_model_load: 3562.13907400767 ms
avg_inference: 4475.47459602356 ms

avg_audio_load: 190.7054583231608 ms
avg_model_load: 3601.4477411905923 ms
avg_inference: 4507.242838541667 ms

avg_audio_load: 199.43352540334067 ms
avg_model_load: 3563.637137413025 ms
avg_inference: 4224.069635073344 ms

avg_audio_load: 192.79090563456217 ms
avg_model_load: 3587.614138921102 ms
avg_inference: 4360.912998517354 ms

## GTX 1050 Ti CUDA
avg_audio_load: 194.73683834075928 ms
avg_model_load: 4159.605065981547 ms
avg_inference: 3530.2109718322754 ms

avg_audio_load: 198.0601946512858 ms
avg_model_load: 4165.197889010112 ms
avg_inference: 3571.945389111837 ms

avg_audio_load: 199.2314656575521 ms
avg_model_load: 4218.34655602773 ms
avg_inference: 3642.8603728612266 ms

avg_audio_load: 197.79860973358154 ms
avg_model_load: 4187.9507303237915 ms
avg_inference: 3546.4319785435996 ms

avg_audio_load: 198.39676221211752 ms
avg_model_load: 4189.300775527954 ms
avg_inference: 3598.004619280497 ms

