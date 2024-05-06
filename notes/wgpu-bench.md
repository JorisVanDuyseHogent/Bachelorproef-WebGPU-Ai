# wgpu-bench by fleetwood
> om deze benchmark werkende te krijgen moest torch worden gedowngrade worden van v2.3.0 naar 2.0.0

## cargo bench --bench naive
LayerNorm/LayerNorm/0   time:   [153854.2238 ns 153969.6750 ns 154094.2157 ns]
                        thrpt:  [101.3990 GiB/s 101.4810 GiB/s 101.5572 GiB/s]
                 change:
                        time:   [-0.2648% -0.1311% -0.0014%] (p = 0.05 < 0.05)
                        thrpt:  [+0.0014% +0.1313% +0.2655%]
                        Change within noise threshold.


LayerNorm/LayerNorm/0   time:   [153897.9578 ns 154032.7275 ns 154183.0714 ns]
                        thrpt:  [101.3406 GiB/s 101.4395 GiB/s 101.5283 GiB/s]
                 change:
                        time:   [-0.0744% +0.0410% +0.1591%] (p = 0.51 > 0.05)
                        thrpt:  [-0.1588% -0.0409% +0.0744%]
                        No change in performance detected.

## cargo bench --bench naive_onepass
    Finished `bench` profile [optimized] target(s) in 0.52s
     Running benches/layernorm/naive_onepass.rs (target\release\deps\naive_onepass-cd66f40ba58d64cf.exe)
Gnuplot not found, using plotters backend
thread 'main' panicked at benches/layernorm/naive_onepass.rs:96:51:
called `Result::unwrap()` on an `Err` value: 1048576 samples not close - AVGE=NaN MAE=-1 at [0]
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: bench failed, to rerun pass `--bench naive_onepass`

## cargo bench --bench naive_vectorized
LayerNormVectorized/LayerNormVectorized/0
                        time:   [24048.9674 ns 24067.2847 ns 24087.7485 ns]
                        thrpt:  [43.5315 GFLOP/s 43.5685 GFLOP/s 43.6017 GFLOP/s]
                 change:
                        time:   [+0.6267% +0.7357% +0.8388%] (p = 0.00 < 0.05)
                        thrpt:  [-0.8318% -0.7303% -0.6228%]
                        Change within noise threshold.

LayerNormVectorized/LayerNormVectorized/0
                        time:   [24065.3594 ns 24078.4612 ns 24093.6141 ns]
                        thrpt:  [43.5209 GFLOP/s 43.5483 GFLOP/s 43.5720 GFLOP/s]
                 change:
                        time:   [-0.0582% +0.0464% +0.1454%] (p = 0.37 > 0.05)
                        thrpt:  [-0.1451% -0.0464% +0.0583%]
                        No change in performance detected.

## cargo bench --bench naive_vectorized_onepass
    Finished `bench` profile [optimized] target(s) in 0.52s
     Running benches/layernorm/naive_vectorized_onepass.rs (target\release\deps\naive_vectorized_onepass-174154872e625e91.exe)
Gnuplot not found, using plotters backend
thread 'main' panicked at benches/layernorm/naive_vectorized_onepass.rs:96:51:
called `Result::unwrap()` on an `Err` value: 1048576 samples not close - AVGE=NaN MAE=-1 at [0]
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: bench failed, to rerun pass `--bench naive_vectorized_onepass`

## cargo bench --bench qgemm
QGEMMBenchmark/QGEMMBenchmark/0
                        time:   [3207017.5817 ns 3210538.2500 ns 3214239.7700 ns]
                        thrpt:  [5344.9246 GFLOP/s 5351.0869 GFLOP/s 5356.9613 GFLOP/s]
                 change:
                        time:   [-0.5818% -0.4053% -0.2272%] (p = 0.00 < 0.05)
                        thrpt:  [+0.2277% +0.4069% +0.5852%]
                        Change within noise threshold.

QGEMMBenchmark/QGEMMBenchmark/0
                        time:   [3221096.2300 ns 3224361.5500 ns 3227654.9285 ns]
                        thrpt:  [5322.7094 GFLOP/s 5328.1460 GFLOP/s 5333.5473 GFLOP/s]
                 change:
                        time:   [+0.2782% +0.4306% +0.5830%] (p = 0.00 < 0.05)
                        thrpt:  [-0.5797% -0.4287% -0.2775%]
                        Change within noise threshold.

## cargo bench --bench qgemv
QGEMVBenchmark/QGEMVBenchmark/0
                        time:   [351756.9591 ns 352665.3200 ns 353664.0500 ns]
                        thrpt:  [148.2446 GFLOP/s 148.6645 GFLOP/s 149.0484 GFLOP/s]
                 change:
                        time:   [+0.2421% +0.5258% +0.8131%] (p = 0.00 < 0.05)
                        thrpt:  [-0.8066% -0.5230% -0.2415%]
                        Change within noise threshold.

QGEMVBenchmark/QGEMVBenchmark/0
                        time:   [353417.7484 ns 354379.8400 ns 355419.7495 ns]
                        thrpt:  [147.5123 GFLOP/s 147.9452 GFLOP/s 148.3480 GFLOP/s]
                 change:
                        time:   [+0.0764% +0.4862% +0.8683%] (p = 0.02 < 0.05)
                        thrpt:  [-0.8608% -0.4838% -0.0763%]
                        Change within noise threshold.

## cargo bench --bench rope
mlx.core missing in inline python code

## cargo bench --bench sgemm
SGEMMBenchmark/SGEMMBenchmark/0
                        time:   [14267.3932 ns 14274.4704 ns 14282.1556 ns]
                        thrpt:  [2349.3955 GFLOP/s 2350.6604 GFLOP/s 2351.8264 GFLOP/s]
                 change:
                        time:   [-0.3274% -0.2360% -0.1411%] (p = 0.00 < 0.05)
                        thrpt:  [+0.1413% +0.2366% +0.3285%]

SGEMMBenchmark/SGEMMBenchmark/0
                        time:   [14276.5572 ns 14283.1676 ns 14290.5496 ns]
                        thrpt:  [2348.0155 GFLOP/s 2349.2290 GFLOP/s 2350.3168 GFLOP/s]
                 change:
                        time:   [-0.0093% +0.0609% +0.1307%] (p = 0.10 > 0.05)
                        thrpt:  [-0.1305% -0.0609% +0.0093%]
                        No change in performance detected.

## cargo bench --bench sgemv
Caused by:
    Parent device is lost

note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: bench failed, to rerun pass `--bench sgemv`

## cargo bench --bench welford_scalar
    Finished `bench` profile [optimized] target(s) in 0.53s
     Running benches/layernorm/welford_scalar.rs (target\release\deps\welford_scalar-cab3f4d52200628a.exe)
Gnuplot not found, using plotters backend
[2024-05-05T13:43:43Z ERROR wgpu_core::device::global] Device::create_shader_module error:
    Shader validation error:
       ┌─ :94:5
       │
    94 │     subgroupBarrier();
       │     ^^^^^^^^^^^^^^^ missing capability for this operation


[2024-05-05T13:43:43Z ERROR wgpu::backend::wgpu_core] Handling wgpu errors as fatal by default
thread 'main' panicked at cargo\registry\src\index.crates.io-6f17d22bba15001f\wgpu-0.20.0\src\backend\wgpu_core.rs:2996:5:
wgpu error: Validation Error

Caused by:
    In Device::create_shader_module

Shader validation error:
   ┌─ :94:5
   │
94 │     subgroupBarrier();
   │     ^^^^^^^^^^^^^^^ missing capability for this operation


    Entry point main at Compute is invalid
    Shader requires capability Capabilities(SUBGROUP | SUBGROUP_BARRIER)


note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: bench failed, to rerun pass `--bench welford_scalar`

## cargo bench --bench welford_vectorized
    Finished `bench` profile [optimized] target(s) in 0.51s
     Running benches/layernorm/welford_vectorized.rs (target\release\deps\welford_vectorized-9a6598be8df18854.exe)
Gnuplot not found, using plotters backend
[2024-05-05T13:44:15Z ERROR wgpu_core::device::global] Device::create_shader_module error:
    Shader validation error:
        ┌─ :100:5
        │
    100 │     subgroupBarrier();
        │     ^^^^^^^^^^^^^^^ missing capability for this operation


[2024-05-05T13:44:15Z ERROR wgpu::backend::wgpu_core] Handling wgpu errors as fatal by default
thread 'main' panicked at cargo\registry\src\index.crates.io-6f17d22bba15001f\wgpu-0.20.0\src\backend\wgpu_core.rs:2996:5:
wgpu error: Validation Error

Caused by:
    In Device::create_shader_module

Shader validation error:
    ┌─ :100:5
    │
100 │     subgroupBarrier();
    │     ^^^^^^^^^^^^^^^ missing capability for this operation


    Entry point main at Compute is invalid
    Shader requires capability Capabilities(SUBGROUP | SUBGROUP_BARRIER)


note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: bench failed, to rerun pass `--bench welford_vectorized`

## Results on M3 Max 14 core:

Naive Onepass (precision FAIL)
time:   [88680.6021 ns 92554.9586 ns 95756.6363 ns]
thrpt:  [40.7935 GiB/s 42.2047 GiB/s 44.0485 GiB/s]

Naive
time:   [115698.3828 ns 116433.8667 ns 117343.1857 ns]
thrpt:  [33.2891 GiB/s 33.5491 GiB/s 33.7624 GiB/s]

Naive Vectorized
time:   [113990.1512 ns 114341.8859 ns 114775.5896 ns]
thrpt:  [34.0338 GiB/s 34.1629 GiB/s 34.2683 GiB/s]

Welford Scalar
time:   [74209.2818 ns 74668.5137 ns 75306.7653 ns]
thrpt:  [51.8712 GiB/s 52.3146 GiB/s 52.6383 GiB/s]

Welford Vectorized
time:   [48744.7028 ns 48831.9797 ns 48933.0603 ns]
thrpt:  [79.8284 GiB/s 79.9937 GiB/s 80.1369 GiB/s]

