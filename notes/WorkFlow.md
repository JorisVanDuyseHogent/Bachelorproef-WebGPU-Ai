Onderdelen bachelorproefKijk goed na of alle gevraagde onderdelen aanwezig zijn:
[ x ] - Omslag
[ ] - Samenvatting/ Abstract
[ ] - Inhoudsopgave
[ ] - Lijst van figuren
[ ] - Lijst van tabellen
[ ] - Inleiding met duidelijke probleemstelling en onderzoeksvraag
[ ] - Literatuurstudie
[ ] - Methodologie
[ ] - Resultaten
[ ] - Discussie en conclusies
[ ] - Referentielijst

Testen van WebLLM
[ ] - token per seconden voor intel hd graphics
[ ] - token per seconden voor nvidia gtx 1080 ti
[ ] - token per seconden voor AMD Radeon Pro 5500M 4 GB

Veiligheids aspecten beschrijven zoals side channel aanvallen en security chellenges vergelijken met WebGL.


## Hugginface transformer benchmark
Transformers.js WebGPU Benchmark
This benchmark measures the execution time of BERT-based embedding models using the WASM and WebGPU execution providers across different batch sizes.

### Goliath
GTX 1080
124.0.6367.92 (Official Build) (64-bit)

Model: Xenova/all-MiniLM-L6-v2
Tests run: WASM (fp32), WebGPU (fp32)
Sequence length: 512
Browser: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
GPU: vendor=nvidia, architecture=pascal, device=, description=

1	956.30	    29.10
2	1995.50	    92.30
4	3920.60	    69.50
8	7716.80	    196.30
16	15541.70	282.00
32	30951.80	664.50
64	62227.60	794.70

1	944.60	    27.70
2	1903.30	    57.20
4	3804.20	    60.00
8	7652.10	    123.10
16	15821.50	187.30
32	31018.90	565.60
64	61617.10	776.70

1	942.80	    27.30
2	1910.30	    57.90
4	3785.50	    113.90
8	7688.90	    132.00
16	15451.70	415.70
32	30487.10	236.10
64	61439.90	762.10

1	947.00	    31.70
2	1909.80	    58.40
4	3789.60	    108.80
8	7630.80	    65.50
16	15398.60	122.10
32	31061.70	477.40
64	61740.10	718.50

1	940.00	    24.30
2	1896.70	    25.60
4	3784.60	    36.50
8	7576.40	    65.10
16	15259.60	122.90
32	30987.50	372.20
64	61915.30	643.80

### QweckCrookPro
124.0.6367.93 (Official Build) (x86_64)
Model: Xenova/all-MiniLM-L6-v2
Tests run: WASM (fp32), WebGPU (fp32)
Sequence length: 512
Browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
GPU: vendor=intel, architecture=gen-9, device=, description=

i9 hd graphics
1	738.30	    196.00
2	1542.90	    379.30
4	3031.10	    726.80
8	6120.60	    1445.80
16	11841.00	2856.30
32	23640.60	5748.80
64	47463.70	11404.40

1	725.50	    193.90
2	1458.40	    357.80
4	2900.60	    696.90
8	5744.00	    1375.70
16	11602.30	2725.20
32	23204.90	5447.20
64	48728.00	10807.90

1	731.90	    190.60
2	1504.40	    361.50
4	2972.40	    696.10
8	6061.70	    1386.80
16	12064.70	2729.40
32	24551.80	5446.00
64	47165.50	10878.80

1	729.00	    191.40
2	1407.20	    369.00
4	3047.20	    695.10
8	6001.40	    1381.00
16	12046.50	2731.00
32	24289.10	5440.00
64	47491.50	10916.30

1	810.80	    196.40
2	1587.00	    361.90
4	3120.60	    701.30
8	5854.20	    1376.30
16	11484.00	2721.40
32	24921.40	5471.70
64	47997.00	10822.80