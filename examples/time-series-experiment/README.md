# 时间序列预测实验分析示例

## 概述

本示例展示了如何使用 GradAgent Kit 分析时间序列预测实验结果。实验对比了 PatchTST 基线方法与 Our Method 在 ETTh1 和 ETTh2 数据集上的表现。

## 文件结构

```
time-series-experiment/
├── README.md              # 本文件
├── results.csv            # 实验结果数据
├── config.yaml            # 实验配置参数
├── train.log              # 训练过程日志
└── expected-analysis.md   # 预期的分析输出示例
```

## 实验设置

### 数据集

| 数据集 | 描述 | 变量数 | 时间粒度 | 预测长度 |
|--------|------|--------|----------|----------|
| ETTh1  | 电力变压器温度（站点1） | 7 | 小时 | 96, 192, 336, 720 |
| ETTh2  | 电力变压器温度（站点2） | 7 | 小时 | 96, 192, 336, 720 |

### 方法对比

- **PatchTST**: 基于 Patch 的时间序列 Transformer，使用 channel-independent 策略
- **Our Method**: 轻量化改进版本，引入参数高效微调机制

### 评估指标

- **MSE (Mean Squared Error)**: 均方误差，越低越好
- **MAE (Mean Absolute Error)**: 平均绝对误差，越低越好

## 使用方式

### 1. 使用 GradAgent 分析

```bash
# 进入项目目录
cd gradagentkit

# 运行分析
gradagent analyze --input examples/time-series-experiment/

# 指定分析类型
gradagent analyze --input examples/time-series-experiment/ --type experiment
```

### 2. 编程方式调用

```python
from gradagent import ExperimentAnalyzer

# 初始化分析器
analyzer = ExperimentAnalyzer(
    config_path="examples/time-series-experiment/config.yaml",
    results_path="examples/time-series-experiment/results.csv",
    log_path="examples/time-series-experiment/train.log"
)

# 运行分析
report = analyzer.analyze()

# 输出报告
print(report.to_markdown())
```

## 预期输出

分析完成后，将生成包含以下内容的报告：

1. **性能对比表**: 各方法在不同数据集和预测长度上的 MSE/MAE
2. **性能提升分析**: Our Method 相对于 PatchTST 的改进百分比
3. **训练效率分析**: 参数量、训练时间、收敛速度对比
4. **统计显著性检验**: 配对 t 检验结果
5. **可视化图表**: 性能对比柱状图、学习曲线等

详见 `expected-analysis.md`。

## 扩展说明

### 添加新方法

在 `results.csv` 中添加新方法的数据行，保持相同的列结构即可。

### 添加新数据集

1. 在 `config.yaml` 中添加数据集配置
2. 在 `results.csv` 中添加对应的结果数据
3. 在 `train.log` 中添加训练日志

### 自定义分析

修改 `config.yaml` 中的 `analysis` 部分来自定义分析选项：

```yaml
analysis:
  significance_test: true
  confidence_level: 0.95
  generate_plots: true
  plot_format: png
```

## 引用

如果本示例对您的研究有帮助，请引用：

```bibtex
@article{your_paper,
  title={Lightweight Time Series Forecasting with Parameter-Efficient Fine-Tuning},
  author={Your Name},
  journal={arXiv preprint},
  year={2026}
}
```

## 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件至 your.email@example.com
