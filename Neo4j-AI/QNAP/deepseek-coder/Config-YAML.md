```yaml
name: Multi-Model Assistant 
version: 1.0.0 
schema: v1 
models: 
# Your current working model 
# Alternative for comparison 
- name: Qwen2.5 Coder 1.5B 
	provider: ollama 
	model: qwen2.5-coder:1.5b 
	apiBase: http://10.0.3.2:11434 
	roles: [chat, edit, apply, autocomplete]
```