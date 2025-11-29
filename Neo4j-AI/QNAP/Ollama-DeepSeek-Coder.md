# Q:
does Ollama support deepseek-coder?
# A: 
Yes, Ollama supports DeepSeek-Coder models! Here's a detailed breakdown:

### Ollama DeepSeek-Coder Support

1. Available Models:
- `deepseek-coder:6.7b`
- `deepseek-coder:6.7b-base`
- `deepseek-coder:1.3b`
- `deepseek-coder:1.3b-base`

### Quick Installation on QNAP NAS

```bash
# SSH into your NAS
ollama pull deepseek-coder:6.7b

# Run the model
ollama run deepseek-coder:6.7b
```

### Compatibility Check
- ✅ CPU-based inference
- ✅ Works with your Intel Xeon D-1602
- ✅ Compatible with Container Station
- ✅ No special GPU configuration needed

### Recommendation
Given your NAS specs (128GB RAM, Intel Xeon), the `6.7b` model would likely perform well for coding tasks.

Would you like a detailed walkthrough of setting up Ollama on your QNAP NAS?