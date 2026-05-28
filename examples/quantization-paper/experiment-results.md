# Experiment Results

> Quantitative results for dynamic quantization experiments.

---

## Datasets

### ETTh1 (Electricity Transformer Temperature - Hourly)
- Samples: 17,420
- Features: 7
- Prediction horizon: 96, 192, 336, 720

### ETTh2
- Samples: 17,420
- Features: 7
- Prediction horizon: 96, 192, 336, 720

### ETTm1 (Electricity Transformer Temperature - 15min)
- Samples: 69,680
- Features: 7
- Prediction horizon: 96, 192, 336, 720

---

## Baselines

1. **PatchTST** (2023) - Current SOTA for time-series forecasting
2. **iTransformer** (2024) - Attention-based approach
3. **TimesNet** (2023) - Multi-scale method
4. **Static 2-bit** - Uniform 2-bit quantization
5. **Static 4-bit** - Uniform 4-bit quantization

---

## Main Results

### ETTh1 Dataset

| Method | MSE (96) | MSE (192) | MSE (336) | MSE (720) | Model Size |
|--------|----------|-----------|-----------|-----------|------------|
| PatchTST | 0.370 | 0.413 | 0.422 | 0.436 | 12.0 MB |
| iTransformer | 0.376 | 0.420 | 0.432 | 0.445 | 11.5 MB |
| TimesNet | 0.384 | 0.428 | 0.440 | 0.458 | 13.2 MB |
| Static 2-bit | 0.412 | 0.458 | 0.472 | 0.490 | 3.0 MB |
| Static 4-bit | 0.389 | 0.435 | 0.448 | 0.465 | 6.0 MB |
| **Our Method** | **0.361** | **0.405** | **0.415** | **0.430** | **8.4 MB** |

**Improvement over PatchTST**: 2.4% (96), 1.9% (192), 1.7% (336), 1.4% (720)

### ETTh2 Dataset

| Method | MSE (96) | MSE (192) | MSE (336) | MSE (720) | Model Size |
|--------|----------|-----------|-----------|-----------|------------|
| PatchTST | 0.274 | 0.342 | 0.361 | 0.382 | 12.0 MB |
| iTransformer | 0.280 | 0.348 | 0.368 | 0.390 | 11.5 MB |
| TimesNet | 0.288 | 0.356 | 0.376 | 0.400 | 13.2 MB |
| Static 2-bit | 0.312 | 0.385 | 0.408 | 0.435 | 3.0 MB |
| Static 4-bit | 0.292 | 0.360 | 0.382 | 0.408 | 6.0 MB |
| **Our Method** | **0.269** | **0.335** | **0.355** | **0.376** | **8.4 MB** |

**Improvement over PatchTST**: 1.8% (96), 2.0% (192), 1.7% (336), 1.6% (720)

### ETTm1 Dataset

| Method | MSE (96) | MSE (192) | MSE (336) | MSE (720) | Model Size |
|--------|----------|-----------|-----------|-----------|------------|
| PatchTST | 0.292 | 0.335 | 0.358 | 0.382 | 12.0 MB |
| iTransformer | 0.298 | 0.342 | 0.365 | 0.390 | 11.5 MB |
| TimesNet | 0.308 | 0.352 | 0.375 | 0.400 | 13.2 MB |
| Static 2-bit | 0.335 | 0.385 | 0.412 | 0.440 | 3.0 MB |
| Static 4-bit | 0.312 | 0.358 | 0.382 | 0.408 | 6.0 MB |
| **Our Method** | **0.285** | **0.328** | **0.350** | **0.375** | **8.4 MB** |

**Improvement over PatchTST**: 2.4% (96), 2.1% (192), 2.2% (336), 1.8% (720)

---

## Efficiency Analysis

### Model Size

| Method | Parameters | Size (MB) | Compression Ratio |
|--------|-----------|-----------|-------------------|
| PatchTST | 12.5M | 12.0 | 1.0x |
| Static 2-bit | 3.1M | 3.0 | 4.0x |
| Static 4-bit | 6.3M | 6.0 | 2.0x |
| **Our Method** | **8.8M** | **8.4** | **1.4x** |

### Inference Speed (GPU)

| Method | Latency (ms) | Throughput (samples/s) |
|--------|-------------|----------------------|
| PatchTST | 15.2 | 65.8 |
| Static 2-bit | 8.5 | 117.6 |
| Static 4-bit | 11.3 | 88.5 |
| **Our Method** | **12.9** | **77.5** |

**Speedup**: 15.1% faster than PatchTST

---

## Ablation Study

### Component Analysis

| Configuration | MSE (ETTh1-96) | Improvement |
|---------------|----------------|-------------|
| Full Model | 0.361 | 2.4% |
| w/o Attention Guidance | 0.375 | 0.0% |
| w/o Dynamic Allocation | 0.370 | 0.5% |
| w/o Straight-Through | 0.368 | 0.3% |
| w/o Both | 0.382 | -0.5% |

**Key Finding**: Attention guidance contributes 1.9% of the 2.4% improvement.

### Threshold Sensitivity

| Threshold | MSE | Model Size | Compression |
|-----------|-----|------------|-------------|
| 0.5 | 0.365 | 9.2 MB | 1.3x |
| 0.6 | 0.363 | 8.8 MB | 1.4x |
| 0.7 | 0.361 | 8.4 MB | 1.4x |
| 0.8 | 0.368 | 7.6 MB | 1.6x |
| 0.9 | 0.378 | 6.8 MB | 1.8x |

**Optimal**: Threshold = 0.7 (best accuracy-compression trade-off)

---

## Statistical Significance

### Paired t-test Results

Comparison with PatchTST on ETTh1:

| Horizon | Mean Diff | Std Error | t-stat | p-value | Significant? |
|---------|-----------|-----------|--------|---------|--------------|
| 96 | -0.009 | 0.003 | -3.00 | 0.003 | Yes (p < 0.01) |
| 192 | -0.008 | 0.004 | -2.00 | 0.048 | Yes (p < 0.05) |
| 336 | -0.007 | 0.004 | -1.75 | 0.083 | Marginal |
| 720 | -0.006 | 0.005 | -1.20 | 0.233 | No |

**Note**: Improvement is statistically significant for short-term forecasting (96, 192).

---

## Failure Cases

### When Our Method Struggles

1. **Highly noisy data**: Attention weights become unreliable
2. **Very short sequences**: Insufficient attention patterns
3. **Sudden distribution shifts**: Dynamic allocation may lag

### Mitigation Strategies

1. **Noise filtering**: Preprocess data with smoothing
2. **Minimum sequence length**: Require ≥ 96 time steps
3. **Adaptive threshold**: Adjust based on data statistics

---

## Summary

### Strengths
- ✅ Consistent improvement across datasets
- ✅ Significant compression (30% size reduction)
- ✅ Faster inference (15% speedup)
- ✅ Statistically significant for short-term forecasting

### Weaknesses
- ⚠️ Marginal improvement for long-term forecasting
- ⚠️ Sensitivity to threshold choice
- ⚠️ Limited to forecasting tasks

---

*Experiment Results - Quantization Paper Example*