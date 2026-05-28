# Method Description

> Dynamic quantization for time-series Transformer models

---

## Overview

Our method introduces **dynamic bit-width quantization** for time-series Transformer models. Unlike static quantization that applies uniform bit-width across all time steps, our approach uses attention weights to determine the importance of each time step and allocates precision accordingly.

---

## Key Innovation

**Attention-Guided Bit Allocation**: We observe that attention weights in Transformer models naturally capture the importance of different time steps. By leveraging these weights, we can dynamically allocate higher precision (8-bit) to important time steps and lower precision (2-bit) to less important ones.

---

## Architecture

### 1. Attention Weight Computation

In each Transformer layer, we compute attention weights:

```python
# Standard attention
Q = X @ W_Q
K = X @ W_K
V = X @ W_V

attention_weights = softmax(Q @ K.T / sqrt(d_k))
```

### 2. Importance Score Calculation

We aggregate attention weights across heads to get importance scores:

```python
# Average across attention heads
importance = mean(attention_weights, dim=heads)

# Normalize to [0, 1]
importance = (importance - min(importance)) / (max(importance) - min(importance))
```

### 3. Bit-Width Allocation

Based on importance scores, we allocate bit-widths:

```python
# Threshold-based allocation
high_precision_mask = importance > threshold  # e.g., 0.7

# Allocate bit-widths
bit_width = where(high_precision_mask, 8, 2)
```

### 4. Dynamic Quantization

We apply quantization with allocated bit-widths:

```python
# Quantize each time step with its allocated bit-width
for t in range(seq_len):
    if bit_width[t] == 8:
        X_quantized[t] = quantize_8bit(X[t])
    else:
        X_quantized[t] = quantize_2bit(X[t])
```

### 5. Straight-Through Estimator

For training, we use straight-through estimator to handle non-differentiable quantization:

```python
# Forward: quantize
X_quantized = quantize(X, bit_width)

# Backward: straight-through
X_grad = X_quantized.grad  # Pass gradient through
```

---

## Training Procedure

### Loss Function

```python
L_total = L_forecast + λ * L_compression

where:
- L_forecast = MSE loss for time-series prediction
- L_compression = regularization for model size
- λ = trade-off parameter
```

### Optimization

```python
optimizer = Adam(model.parameters(), lr=1e-3)
scheduler = CosineAnnealingLR(optimizer, T_max=100)

for epoch in range(100):
    for batch in dataloader:
        loss = model(batch)
        loss.backward()
        optimizer.step()
        scheduler.step()
```

---

## Complexity Analysis

### Time Complexity
- Standard Transformer: O(n²d)
- Our method: O(n²d + n)  [negligible overhead]

### Space Complexity
- Standard Transformer: O(n² + nd)
- Our method: O(n² + nd × (2/8))  [4x compression on average]

---

## Advantages

1. **Adaptive**: Adjusts to input patterns dynamically
2. **Efficient**: Minimal computational overhead
3. **Effective**: Significant compression with little accuracy loss
4. **General**: Applicable to various time-series tasks
5. **Interpretable**: Attention weights provide insights

---

## Limitations

1. **Threshold sensitivity**: Performance depends on threshold choice
2. **Training overhead**: Requires careful tuning of λ
3. **Hardware support**: 2-bit quantization may need specialized hardware
4. **Task-specific**: Optimized for forecasting, may need adaptation for other tasks

---

*Method Description - Quantization Paper Example*